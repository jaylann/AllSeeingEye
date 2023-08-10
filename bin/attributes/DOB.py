from bin.attributes.BaseAttribute import BaseAttribute
from datetime import datetime


class DOB(BaseAttribute):
    def __init__(self, dob: str or datetime, proof):
        super().__init__(proof)
        self.DOB = self.convert_to_date(dob) if type(dob) == str else dob

    @property
    def day(self):
        return self.DOB.day

    @day.setter
    def day(self, value):
        self.DOB = datetime(self.DOB.year, self.DOB.month, value)

    @property
    def month(self):
        return self.DOB.month

    @month.setter
    def month(self, value):
        self.DOB = datetime(self.DOB.year, value, self.DOB.day)

    @property
    def year(self):
        return self.DOB.year

    @year.setter
    def year(self, value):
        self.DOB = datetime(value, self.DOB.month, self.DOB.day)

    @staticmethod
    def convert_to_date(dob):

        # Define a list of possible date formats
        date_formats = [
            # Day-Month-Year formats
            "%d-%m-%Y", "%d/%m/%Y", "%d.%m.%Y", "%d %B %Y", "%d %b %Y",
            "%A, %d %B %Y", "%a, %d %b %Y", "%d-%m-%y", "%d/%m/%y",

            # Year-Month-Day formats (universal)
            "%Y-%m-%d", "%Y/%m/%d", "%Y.%m.%d", "%Y %B %d", "%Y %b %d",
            # Add more formats as needed
        ]

        # Try to parse the date string using the defined formats
        for fmt in date_formats:
            try:
                return datetime.strptime(dob, fmt)
            except ValueError:
                pass

        # If none of the formats match, raise an error
        raise ValueError("Invalid date of birth format")
