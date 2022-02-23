# Copyright (c) 2022, Shubham and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class RMCustomer(Document):
	def before_save(self):
		if not self.customer_name:
			frappe.throw("Customer name is required")
		#print("hhhhhh")