import json
import os

from bin.attributes.BaseAttribute import BaseAttribute
from bin.objects.Proof import Proof


class Address(BaseAttribute):
    def __init__(self, street: str = None, city: str = None, state: str = None,
                 country: str = None, postal_code: int = None, proof: Proof = None):
        super().__init__(proof)
        self.street = street
        self.city = city
        self.state = state
        self.country = self._convert_country_to_code(country)
        self.postal_code = postal_code

    def _load_country_codes(self):
        file_path = os.path.join(self.get_content_root(), '_internal', 'mappings', 'country_codes.json')
        with open(file_path, "r") as file:
            return json.load(file)

    def get_content_root(self):
        # Get the directory of the current file
        current_file_path = os.path.abspath(__file__)
        # Navigate up to the project root (modify as needed for your directory structure)
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_file_path)))
        return project_root

    def _convert_country_to_code(self, country_name):
        for code, names in self._load_country_codes().items():
            if country_name.lower() in [name.lower() for name in names]:
                return code
        return country_name

    @property
    def street(self):
        return self._street if hasattr(self, '_street') else None

    @street.setter
    def street(self, value):
        self._street = value if value else None

    @property
    def city(self):
        return self._city if hasattr(self, '_city') else None

    @city.setter
    def city(self, value):
        self._city = value if value else None

    @property
    def state(self):
        return self._state if hasattr(self, '_state') else None

    @state.setter
    def state(self, value):
        self._state = value if value else None

    @property
    def country(self):
        return self._country if hasattr(self, '_country') else None

    @country.setter
    def country(self, value):
        self._country = value if value else None

    @property
    def postal_code(self):
        return self._postal_code if hasattr(self, '_postal_code') else None

    @postal_code.setter
    def postal_code(self, value):
        self._postal_code = value if value else None

    def __str__(self):
        return f"{self.street or ''}, {self.city or ''}, {self.state or ''}, {self.country or ''} - {self.postal_code or ''}"
