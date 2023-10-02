# Copyright (c) 2023, Jinal Balar and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    columns = [
        {
            "label": "Add Ons",
            "fieldname": "add_ons",
            "fieldtype": "Link",
            "options": "Airplane Ticket Add-on Item",
            "width": 200
        },
        {
            "label": "Sold Count",
            "fieldname": "sold_count",
            "fieldtype": "Int",
            "width": 120
        },
    ]
    data = get_addon_data(filters)
    return columns, data

def get_addon_data(filters):
    data = {}

    airplane_tickets = frappe.get_all("Airplane Ticket",
                                      filters={},  # Add filters as needed
                                      fields=["name"]
                                      )

    for ticket in airplane_tickets:
        ticket_doc = frappe.get_doc("Airplane Ticket", ticket.name)

        for addon_item in ticket_doc.add_ons:
            add_on = addon_item.item

            if add_on in data:
                data[add_on]["sold_count"] += 1
            else:
                data[add_on] = {"add_ons": add_on, "sold_count": 1}

    data_list = list(data.values())

    data_list.sort(key=lambda x: x["sold_count"], reverse=True)

    return data_list

