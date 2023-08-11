from bin.attributes.BaseAttribute import BaseAttribute
from datetime import datetime

from bin.utils.date import convert_to_date


class DOB(BaseAttribute):
    def __init__(self, dob: str or datetime, proof):
        super().__init__(proof)
        self.DOB = convert_to_date(dob) if type(dob) == str else dob

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



