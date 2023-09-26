# Copyright (c) 2023, Jinal Balar and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
    columns = [
        {
            "fieldname": "airline",
            "label": _("Airline"), 
            "fieldtype": "Link", 
            "options": "Airline", 
            "width": 150
        },
        {
            "fieldname": "revenue", 
            "label": _("Revenue"), 
            "fieldtype": "Currency", 
            "width": 150
        },
    ]

    data = []

    airlines = frappe.get_all("Airline", filters={"docstatus": 1}, fields=["name"])

    for airline in airlines:
        revenue = calculate_airline_revenue(airline.name)
        data.append({"airline": airline.name, "revenue": revenue})

    chart = {
        "data": {
            "labels": [row["airline"] for row in data],
            "datasets": [
                {
                    "name": _("Revenue"),
                    "values": [row["revenue"] for row in data],
                }
            ],
        },
        "type": "donut",
    }

    summary = {
        "total_revenue": sum([row["revenue"] for row in data]),
    }

    return columns, data, None, chart, summary

def calculate_airline_revenue(airline):
    tickets = frappe.get_all(
        "Airplane Tickets",
        filters={"airline": airline, "docstatus": ["in", [0, 1]]},
        fields=["flight_price"],
    )
    
    revenue = sum(ticket.flight_price for ticket in tickets)
    return revenue
















