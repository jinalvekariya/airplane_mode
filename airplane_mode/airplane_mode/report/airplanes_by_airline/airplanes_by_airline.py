# Copyright (c) 2023, Jinal Balar and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    columns = [
        {
            'fieldname': 'airline',
            'label': 'Airline',
            'fieldtype': 'Link',
            'options': 'Airline'
        },
        {
            'fieldname': 'count',
            'label': 'Count',
            'fieldtype': 'Int'
        }
    ]
    return columns

def get_data(filters):
    class_counts = {}
    data = frappe.get_all("Airplane", fields=["airline"])
    for row in data:
        airline = row.get("airline")
        if airline:
            if airline in class_counts:
                class_counts[airline] += 1
            else:
                class_counts[airline] = 1
                
        result_data = []
        
        for airline, count in class_counts.items():
            result_data.append({"airline": airline, "count": count})
        
        return result_data