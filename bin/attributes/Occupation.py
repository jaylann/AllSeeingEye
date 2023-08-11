from bin.attributes.BaseAttribute import BaseAttribute
from bin.objects.Proof import Proof

from bin.utils.date import convert_to_date


class Occupation(BaseAttribute):
    def __init__(self, job_title: str, company_name: str, industry: str, years_experience: int, start_date, end_date, proof: Proof):
        super().__init__(proof)
        self.job_title = job_title
        self.company_name = company_name
        self.industry = industry
        self.years_experience = years_experience
        self.start_date = start_date  # Will call the setter method
        self.end_date = end_date      # Will call the setter method

    # Other properties as before

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = convert_to_date(value)  # Validate and convert to datetime

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = convert_to_date(value)    # Validate and convert to datetime

    # Rest of the class as before
