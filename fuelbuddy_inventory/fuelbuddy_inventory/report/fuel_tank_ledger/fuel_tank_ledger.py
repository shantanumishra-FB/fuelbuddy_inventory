# Copyright (c) 2026, Fuelbuddy and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.utils import flt, getdate


def execute(filters=None):
	filters = frappe._dict(filters or {})
	if not (filters.company and filters.from_date and filters.to_date and filters.fuel_tank):
		frappe.throw(_("Company, From Date, To Date and Fuel Tank are required."))
	if getdate(filters.from_date) > getdate(filters.to_date):
		frappe.throw(_("From Date must be on or before To Date."))
	return get_columns(), get_data(filters)


def get_columns():
	return [
		{"fieldname": "posting_datetime", "label": _("Date"), "fieldtype": "Datetime", "width": 160},
		{"fieldname": "voucher_type", "label": _("Voucher Type"), "fieldtype": "Data", "width": 130},
		{
			"fieldname": "voucher_no",
			"label": _("Voucher No"),
			"fieldtype": "Dynamic Link",
			"options": "voucher_type",
			"width": 180,
		},
		{
			"fieldname": "other_tank",
			"label": _("Other Tank"),
			"fieldtype": "Link",
			"options": "Fuel Tank",
			"width": 180,
		},
		{"fieldname": "item_code", "label": _("Item"), "fieldtype": "Link", "options": "Item", "width": 120},
		{"fieldname": "in_qty", "label": _("In Qty"), "fieldtype": "Float", "width": 110},
		{"fieldname": "out_qty", "label": _("Out Qty"), "fieldtype": "Float", "width": 110},
		{"fieldname": "balance_qty", "label": _("Balance Qty"), "fieldtype": "Float", "width": 120},
	]


def get_data(filters):
	precision = frappe.get_precision("Stock Ledger Entry", "actual_qty")
	opening = {row.item_code: row.qty for row in get_opening(filters)}
	entries = get_entries(filters)

	items = sorted(set(opening) | {sle.item_code for sle in entries})
	data = [
		{"voucher_type": _("Opening"), "item_code": item, "balance_qty": flt(opening.get(item, 0), precision)}
		for item in items
	]
	for sle in entries:
		from_tank, to_tank = sle.from_tank or sle.to_tank, sle.to_tank or sle.from_tank
		other_tank = None if from_tank == to_tank else (to_tank if sle.actual_qty < 0 else from_tank)
		data.append(
			{
				"posting_datetime": sle.posting_datetime,
				"voucher_type": sle.voucher_type,
				"voucher_no": sle.voucher_no,
				"other_tank": other_tank,
				"item_code": sle.item_code,
				"in_qty": flt(sle.actual_qty, precision) if sle.actual_qty > 0 else 0,
				"out_qty": flt(-sle.actual_qty, precision) if sle.actual_qty < 0 else 0,
				"balance_qty": flt(opening.get(sle.item_code, 0) + sle.running_qty, precision),
			}
		)
	return data


def get_opening(filters):
	return frappe.db.sql(
		f"""
		select straight_join sle.item_code, sum(sle.actual_qty) as qty
		{tank_entries(filters)}
			and sle.posting_date < %(from_date)s
		group by sle.item_code
		""",
		filters,
		as_dict=True,
	)


def get_entries(filters):
	return frappe.db.sql(
		f"""
		select straight_join sle.posting_datetime, sle.voucher_type, sle.voucher_no, sle.item_code,
			sle.actual_qty, voucher.from_tank, voucher.to_tank,
			sum(sle.actual_qty) over (
				partition by sle.item_code order by sle.posting_datetime, sle.creation, sle.name
			) as running_qty
		{tank_entries(filters)}
			and sle.posting_date between %(from_date)s and %(to_date)s
		order by sle.posting_datetime, sle.creation, sle.name
		""",
		filters,
		as_dict=True,
	)


def tank_entries(filters):
	# Callers use straight_join: prod's extra SLE indexes otherwise make MariaDB read every SLE row.
	# Out rows leave From Tank, in rows enter To Tank; a document naming one tank uses it for both.
	item_condition = "and sle.item_code = %(item_code)s" if filters.item_code else ""
	return f"""
		from (
			select 1 as kind, name, custom_from_tank as from_tank, custom_to_tank as to_tank
			from `tabDelivery Note`
			where docstatus = 1 and %(fuel_tank)s in (custom_from_tank, custom_to_tank)
			union all
			select 2, name, custom_from_tank, custom_to_tank
			from `tabPurchase Receipt`
			where docstatus = 1 and %(fuel_tank)s in (custom_from_tank, custom_to_tank)
			union all
			select 3, name, custom_from_tank, custom_to_tank
			from `tabStock Entry`
			where docstatus = 1 and %(fuel_tank)s in (custom_from_tank, custom_to_tank)
		) voucher
		join `tabStock Ledger Entry` sle on sle.voucher_no = voucher.name
		where voucher.kind = case sle.voucher_type
				when 'Delivery Note' then 1 when 'Purchase Receipt' then 2 when 'Stock Entry' then 3
			end
			and sle.is_cancelled = 0
			and sle.company = %(company)s
			and %(fuel_tank)s = case when sle.actual_qty < 0
				then coalesce(nullif(voucher.from_tank, ''), voucher.to_tank)
				else coalesce(nullif(voucher.to_tank, ''), voucher.from_tank)
			end
			{item_condition}
		"""
