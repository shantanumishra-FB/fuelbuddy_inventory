# Copyright (c) 2026, Fuelbuddy and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def validate_tank_transfer(doc, method=None):
	if doc.purpose != "Material Transfer":
		return
	if not any(row.s_warehouse and row.s_warehouse == row.t_warehouse for row in doc.items):
		return
	if not (doc.custom_from_tank and doc.custom_to_tank):
		frappe.throw(
			_("A transfer within one warehouse moves fuel between tanks: set From Tank and To Tank.")
		)
	if doc.custom_from_tank == doc.custom_to_tank:
		frappe.throw(
			_("From Tank and To Tank are both {0}. Pick two different tanks.").format(doc.custom_from_tank)
		)
