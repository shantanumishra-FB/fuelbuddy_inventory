app_name = "fuelbuddy_inventory"
app_title = "Fuelbuddy Inventory"
app_publisher = "Fuelbuddy"
app_description = "Fuel stock: the Fuel Tank master and the tank fields on stock documents"
app_email = "shantanu.mishra@fuelbuddy.in"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "fuelbuddy_inventory",
# 		"logo": "/assets/fuelbuddy_inventory/logo.png",
# 		"title": "Fuelbuddy Inventory",
# 		"route": "/fuelbuddy_inventory",
# 		"has_permission": "fuelbuddy_inventory.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/fuelbuddy_inventory/css/fuelbuddy_inventory.css"
# app_include_js = "/assets/fuelbuddy_inventory/js/fuelbuddy_inventory.js"

# include js, css files in header of web template
# web_include_css = "/assets/fuelbuddy_inventory/css/fuelbuddy_inventory.css"
# web_include_js = "/assets/fuelbuddy_inventory/js/fuelbuddy_inventory.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "fuelbuddy_inventory/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "fuelbuddy_inventory/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "fuelbuddy_inventory.utils.jinja_methods",
# 	"filters": "fuelbuddy_inventory.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "fuelbuddy_inventory.install.before_install"
after_install = "fuelbuddy_inventory.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "fuelbuddy_inventory.uninstall.before_uninstall"
# after_uninstall = "fuelbuddy_inventory.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "fuelbuddy_inventory.utils.before_app_install"
# after_app_install = "fuelbuddy_inventory.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "fuelbuddy_inventory.utils.before_app_uninstall"
# after_app_uninstall = "fuelbuddy_inventory.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "fuelbuddy_inventory.build.after_build"

# To hook into the build process of other apps
# The list of apps being built is passed as an argument

# after_app_build = "fuelbuddy_inventory.build.after_app_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "fuelbuddy_inventory.notifications.get_notification_config"

# Awesome Bar
# -----------
# Extra search results: list of dicts with label, description, route, index.
# route: ["List", "ToDo"], "/desk/docs/some/page", or "https://example.com"
# awesomebar_search = ["fuelbuddy_inventory.search.awesomebar_results"]

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Stock Entry": {
		"validate": "fuelbuddy_inventory.stock_entry.validate_tank_transfer",
	},
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"fuelbuddy_inventory.tasks.all"
# 	],
# 	"daily": [
# 		"fuelbuddy_inventory.tasks.daily"
# 	],
# 	"hourly": [
# 		"fuelbuddy_inventory.tasks.hourly"
# 	],
# 	"weekly": [
# 		"fuelbuddy_inventory.tasks.weekly"
# 	],
# 	"monthly": [
# 		"fuelbuddy_inventory.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "fuelbuddy_inventory.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "fuelbuddy_inventory.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "fuelbuddy_inventory.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["fuelbuddy_inventory.utils.before_request"]
# after_request = ["fuelbuddy_inventory.utils.after_request"]

# Job Events
# ----------
# before_job = ["fuelbuddy_inventory.utils.before_job"]
# after_job = ["fuelbuddy_inventory.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"fuelbuddy_inventory.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

