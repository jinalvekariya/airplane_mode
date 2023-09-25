// Copyright (c) 2023, Jinal Balar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Airplane Ticket', {
    refresh: function(frm) {
        frm.add_custom_button(__('Select Seat'), function() {
            frappe.prompt({
                fieldname: 'seat_number',
                label: __('Enter the seat number:'),
                fieldtype: 'Data',
                reqd: 1
            }, function(values) {
                if (values.seat_number) {
                    frm.set_value('seat', values.seat_number);
                }
            }, __('Seat Number'), __('OK'));
        });
    }
});
