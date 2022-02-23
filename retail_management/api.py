import frappe
@frappe.whitelist()
def get_price(product_name):
    # print("assdsds")
    doc = frappe.db.get_value("RM Product", product_name,"price")
    return doc
