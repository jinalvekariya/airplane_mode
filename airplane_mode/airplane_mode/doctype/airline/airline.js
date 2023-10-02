// Copyright (c) 2023, Jinal Balar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Airline', {
    refresh: function(frm) {
        // Add a custom button to open the airline's website
        if (frm.doc.website) {
            frm.add_custom_button(__('Open Website'), function() {
				console.log(frm.doc.website)
                window.open(frm.doc.website, '_blank');
            }).addClass('btn-primary');
        }
    }
});
