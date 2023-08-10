from datetime import datetime


class Person:
    def __init__(self, dob):
        self.DOB = dob

    @property
    def age(self):
        today = datetime.today()
        age = today.year - self.DOB.year - ((today.month, today.day) < (self.DOB.month, self.DOB.day))
        return age

    @age.setter
    def age(self, value):
        # Calculate the DOB based on the given age
        today = datetime.today()
        birth_year = today.year - value
        # Assuming the same month and day as the current DOB
        self.DOB = datetime(birth_year, self.DOB.month, self.DOB.day)
