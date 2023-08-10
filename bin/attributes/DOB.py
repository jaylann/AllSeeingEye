from bin.attributes.BaseAttribute import BaseAttribute
from datetime import datetime

class DOB(BaseAttribute):
    def __init__(self, dob, proof):
        super().__init__(proof)
        self.DOB = self.convert_to_date(dob)

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
        # If dob is already a datetime object, simply return it
        if isinstance(dob, datetime):
            return dob

        # Define a list of possible date formats
        date_formats = [
            "%Y-%m-%d",  # Format like "2023-08-10"
            "%d-%m-%Y",  # Format like "10-08-2023"
            "%m/%d/%Y",  # Format like "08/10/2023"
            "%Y/%m/%d",  # Format like "2023/08/10"
            "%d/%m/%Y",  # Format like "10/08/2023"
            "%m-%d-%Y",  # Format like "08-10-2023"
            "%Y.%m.%d",  # Format like "2023.08.10"
            "%d.%m.%Y",  # Format like "10.08.2023"
            "%B %d, %Y",  # Format like "August 10, 2023"
            "%d %B %Y",  # Format like "10 August 2023"
            "%d %b %Y",  # Format like "10 Aug 2023"
            "%A, %d %B %Y",  # Format like "Thursday, 10 August 2023"
            "%a, %d %b %Y",  # Format like "Thu, 10 Aug 2023"
            "%d-%m-%y",  # Format like "10-08-23"
            "%m-%d-%y",  # Format like "08-10-23"
            "%d/%m/%y",  # Format like "10/08/23"
            "%m/%d/%y",  # Format like "08/10/23"
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
