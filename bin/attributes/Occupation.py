from bin.attributes.BaseAttribute import BaseAttribute
from bin.objects.Proof import Proof

from bin.utils.date import convert_to_date


class Occupation(BaseAttribute):
    def __init__(self, job_title: str = None, company_name: str = None, industry: str = None,
                 years_experience: int = 0, start_date=None, end_date=None, proof: Proof = None):
        super().__init__(proof)
        self.job_title = job_title
        self.company_name = company_name
        self.industry = industry
        self.years_experience = years_experience
        self.start_date = start_date  # Will call the setter method
        self.end_date = end_date  # Will call the setter method

    @property
    def start_date(self):
        return self._start_date if hasattr(self, '_start_date') else None

    @start_date.setter
    def start_date(self, value):
        if value is not None:
            self._start_date = convert_to_date(value)  # Validate and convert to datetime
        else:
            self._start_date = None

    @property
    def end_date(self):
        return self._end_date if hasattr(self, '_end_date') else None

    @end_date.setter
    def end_date(self, value):
        if value is not None:
            self._end_date = convert_to_date(value)  # Validate and convert to datetime
        else:
            self._end_date = None

    @property
    def job_title(self):
        return self._job_title if hasattr(self, '_job_title') else None

    @job_title.setter
    def job_title(self, value):
        self._job_title = value

    @property
    def company_name(self):
        return self._company_name if hasattr(self, '_company_name') else None

    @company_name.setter
    def company_name(self, value):
        self._company_name = value

    @property
    def industry(self):
        return self._industry if hasattr(self, '_industry') else None

    @industry.setter
    def industry(self, value):
        self._industry = value

    @property
    def years_experience(self):
        return self._years_experience if hasattr(self, '_years_experience') else 0

    @years_experience.setter
    def years_experience(self, value):
        self._years_experience = int(value) if value is not None else 0

    @property
    def years_at_company(self):
        if self.start_date and self.end_date:
            delta = self.end_date - self.start_date
            return delta.days / 365.25  # Dividing by 365.25 to account for leap years
        return 0

    def __str__(self):
        return (f"{self.job_title} at {self.company_name}, {self.industry} industry - {self.years_experience} years of "
                f"experience from {self.start_date} to {self.end_date}")
