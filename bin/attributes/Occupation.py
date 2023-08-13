import datetime
from typing import Optional, Union
from bin.attributes.BaseAttribute import BaseAttribute
from bin.objects.Proof import Proof
from bin.utils.date import convert_to_date
from dateutil.relativedelta import relativedelta


class Occupation(BaseAttribute):
    """
    Occupation class that extends BaseAttribute.
    It represents a person's occupation, including job title, company name, industry, experience, and employment dates.

    Attributes:
        job_title (str): The job title.
        company_name (str): The company name.
        industry (str): The industry of the company.
        years_experience (int): The years of experience.
        start_date (datetime): The start date of the occupation.
        end_date (datetime): The end date of the occupation.
    """

    def __init__(self, job_title: Optional[str] = None, company_name: Optional[str] = None,
                 industry: Optional[str] = None,
                 years_experience: int = 0, start_date: Optional[Union[str, datetime.datetime]] = None,
                 end_date: Optional[Union[str, datetime.datetime]] = None, proof: Optional[Proof] = None):
        """
        Initializes the Occupation object.

        Args:
            job_title (Optional[str], default=None): The job title.
            company_name (Optional[str], default=None): The company name.
            industry (Optional[str], default=None): The industry of the company.
            years_experience (int, default=0): The years of experience.
            start_date (Optional[Union[str, datetime.datetime]], default=None): The start date, either as a string or a datetime object.
            end_date (Optional[Union[str, datetime.datetime]], default=None): The end date, either as a string or a datetime object.
            proof (Optional[Proof], default=None): Proof associated with the occupation.
        """
        super().__init__(proof)
        self.job_title = job_title
        self.company_name = company_name
        self.industry = industry
        self.years_experience = years_experience
        self.start_date = start_date
        self.end_date = end_date

    @property
    def start_date(self) -> Optional[datetime.datetime]:
        """Returns the start date of the occupation."""
        return getattr(self, '_start_date', None)

    @start_date.setter
    def start_date(self, value: Optional[Union[str, datetime.datetime]]):
        """
        Sets the start date of the occupation, converting from a string if necessary.

        Args:
            value (Optional[Union[str, datetime.datetime]]): The start date.

        Raises:
            ValueError: If the start date is after the end date.
        """
        value = convert_to_date(value) if isinstance(value, str) else value
        if value and self.end_date and value > self.end_date:
            raise ValueError("Start date cannot be after end date.")
        self._start_date = value

    @property
    def end_date(self) -> Optional[datetime.datetime]:
        """Returns the end date of the occupation."""
        return getattr(self, '_end_date', None)

    @end_date.setter
    def end_date(self, value: Optional[Union[str, datetime.datetime]]):
        """
        Sets the end date of the occupation, converting from a string if necessary.

        Args:
            value (Optional[Union[str, datetime.datetime]]): The end date.

        Raises:
            ValueError: If the end date is before the start date.
        """
        value = convert_to_date(value) if isinstance(value, str) else value
        if value and self.start_date and value < self.start_date:
            raise ValueError("End date cannot be before start date.")
        self._end_date = value

    @property
    def years_at_company(self) -> float:
        """Calculates the years at the company based on start and end dates, accounting for leap years."""
        if self.start_date and self.end_date:
            delta = relativedelta(self.end_date, self.start_date)
            return delta.years + delta.months / 12 + delta.days / 365.25
        return 0

    def __str__(self) -> str:
        """Returns the string representation of the occupation."""
        return (f"{self.job_title} at {self.company_name}, {self.industry} industry - {self.years_experience} years of "
                f"experience from {self.start_date} to {self.end_date}")

    def __dict__(self) -> dict:
        """Returns a dictionary representation of the Occupation object, including proofs if available."""
        return {
            'job_title': self.job_title,
            'company_name': self.company_name,
            'industry': self.industry,
            'years_experience': self.years_experience,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'proof': [proof.__dict__() for proof in self.proof] if self.proof else None
        }
