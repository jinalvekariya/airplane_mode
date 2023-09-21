# Copyright (c) 2023, Jinal Balar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class AirplaneTicket(Document):
    def validate(self):
        if self.status != "Boarded":
            frappe.throw("Airplane Ticket cannot be submitted unless the status is 'Boarded'.")
            
    def calculate_total_amount(self):
        flight_price = self.flight_price
        total_amount = flight_price + sum(add_ons.amount for add_ons in self.add_ons)
        self.total_amount = total_amount
    def before_save(self):
        self.calculate_total_amount()
