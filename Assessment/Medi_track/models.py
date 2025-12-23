import re

class BillingCalculator:
    @staticmethod
    def generate_bill(consultation, meds, tax_rate=0.10):
        try:
            subtotal = float(consultation) + float(meds)
            tax = subtotal * tax_rate
            return round(subtotal + tax, 2)
        except (ValueError, TypeError):
            raise ValueError("Please enter valid numbers for charges.")

class ReportGenerator:
    @staticmethod
    def filter_records(pattern, records):
        
        try:
            regex = re.compile(pattern, re.IGNORECASE)
            return [r for r in records if regex.search(r)]
        except re.error:
            raise ValueError("Invalid Regex Pattern. Please check your syntax.")