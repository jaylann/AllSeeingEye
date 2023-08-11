from bin.attributes.BaseAttribute import BaseAttribute
from bin.objects.Proof import Proof


class Occupation(BaseAttribute):
    def __init__(self, job_title: str, company_name: str, industry: str, years_experience: int, proof: Proof):
        super().__init__(proof)
        self.job_title = job_title
        self.company_name = company_name
        self.industry = industry
        self.years_experience = years_experience

    @property
    def job_title(self):
        return self._job_title

    @job_title.setter
    def job_title(self, value):
        self._job_title = value

    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value

    @property
    def industry(self):
        return self._industry

    @industry.setter
    def industry(self, value):
        self._industry = value

    @property
    def years_experience(self):
        return self._years_experience

    @years_experience.setter
    def years_experience(self, value):
        self._years_experience = value

    def __str__(self):
        return f"{self.job_title} at {self.company_name}, {self.industry} industry - {self.years_experience} years of experience"