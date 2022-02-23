# Copyright (c) 2022, Shubham and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class RMSalesInvoice(Document):
	@frappe.whitelist()
	def get_price(self):
		return "helloo"	