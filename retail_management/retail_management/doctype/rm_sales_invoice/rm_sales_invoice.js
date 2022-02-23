// Copyright (c) 2022, Shubham and contributors
// For license information, please see license.txt

frappe.ui.form.on("RM Sales Invoice",{ 
	before_save: function(frm) {
		let total = 0.0;
		frm.doc.product.forEach(function(d) {total += d.price});
		frm.set_value("total_amount", total)
		frm.refresh_field("total_amount")
	},
	onload: function(frm) {
		frm.set_query("customer",function(){
			return {
				"filters":{
					"is_walk_in":"1"
				}
			// print("fgdh")
			}
		})
	}
})


frappe.ui.form.on("RM Product Details", {
	product_name: function(frm,cdt,cdn) {
		var d = locals[cdt][cdn]
	
		frappe.call({
			method: "retail_management.api.get_price",
			args:{
				"product_name":d.product_name
			},
			callback: function(r) {
				d.price = r.message 
				frm.refresh_field("product")
			}
		})
	}
});

