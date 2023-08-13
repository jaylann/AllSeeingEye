import json
import os
from typing import Optional

from bin.attributes.BaseAttribute import BaseAttribute
from bin.objects.Proof import Proof


class Address(BaseAttribute):
    def __init__(self, street: Optional[str] = None, city: Optional[str] = None, state: Optional[str] = None,
                 country: Optional[str] = None, postal_code: Optional[int] = None, proof: Optional[Proof] = None):
        """
        Initializes an Address object with the provided attributes.

        :param street: Street name, default is None.
        :param city: City name, default is None.
        :param state: State name, default is None.
        :param country: Country name, default is None.
        :param postal_code: Postal code, default is None.
        :param proof: Proof object, default is None.
        """
        super().__init__(proof)
        self._street = street
        self._city = city
        self._state = state
        self._postal_code = postal_code
        self._country_codes = self._load_country_codes()
        self._country = self._convert_country_to_code(country)

    def _load_country_codes(self) -> dict:
        """Loads country codes from a JSON file."""
        file_path = os.path.join(self.get_content_root(), '_internal', 'mappings', 'country_codes.json')
        with open(file_path, "r") as file:
            return json.load(file)

    def get_content_root(self) -> str:
        """
        Retrieves the project root directory.

        :return: Path to the project root directory.
        """
        # Get the directory of the current file
        current_file_path = os.path.abspath(__file__)
        # Navigate up to the project root (modify as needed for your directory structure)
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_file_path)))
        return project_root

    def _convert_country_to_code(self, country_name: Optional[str]) -> Optional[str]:
        """
        Converts a country name to its corresponding country code if found.

        :param country_name: Name of the country.
        :return: Country code if found, otherwise the original country name.
        """
        if not country_name:
            return None

        for code, names in self._country_codes.items():
            if country_name.lower() in [name.lower() for name in names]:
                return code
        return country_name

        # Property for street with getter and setter
    @property
    def street(self) -> Optional[str]:
        return self._street

    @street.setter
    def street(self, value: Optional[str]):
        self._street = value

    # Property for city with getter and setter
    @property
    def city(self) -> Optional[str]:
        return self._city

    @city.setter
    def city(self, value: Optional[str]):
        self._city = value

    # Property for state with getter and setter
    @property
    def state(self) -> Optional[str]:
        return self._state

    @state.setter
    def state(self, value: Optional[str]):
        self._state = value

    # Property for country with getter and setter
    @property
    def country(self) -> Optional[str]:
        return self._country

    @country.setter
    def country(self, value: Optional[str]):
        self._country = self._convert_country_to_code(value) if value else None

    # Property for postal_code with getter and setter
    @property
    def postal_code(self) -> Optional[int]:
        return self._postal_code

    @postal_code.setter
    def postal_code(self, value: Optional[int]):
        self._postal_code = value

    def __str__(self) -> str:
        return f"{self._street or ''}, {self._city or ''}, {self._state or ''}, {self._country or ''} - {self._postal_code or ''}"

    def __dict__(self) -> dict:
        return {
            'street': self._street,
            'city': self._city,
            'state': self._state,
            'country': self._country,
            'postal_code': self._postal_code,
            'proof': [proof.__dict__() for proof in self.proof] if self.proof else None
            # Assuming proof is defined in the BaseAttribute class
        }
