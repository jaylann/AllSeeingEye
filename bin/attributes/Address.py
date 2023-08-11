from bin.attributes.BaseAttribute import BaseAttribute
from bin.objects.Proof import Proof


class Address(BaseAttribute):
    def __init__(self, street: str = None, city: str = None, state: str = None,
                 country: str = None, postal_code: int = None, proof: Proof = None):
        super().__init__(proof)
        self.street = street
        self.city = city
        self.state = state
        self.country = country
        self.postal_code = postal_code

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
