from bin.attributes.BaseAttribute import BaseAttribute
from bin.objects.Proof import Proof


class Address(BaseAttribute):
    def __init__(self, street: str, city: str, state: str, country: str, postal_code: int, proof: Proof):
        super().__init__(proof)
        self.street = street
        self.city = city
        self.state = state
        self.country = country
        self.postal_code = postal_code

    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, value):
        self._street = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value

    @property
    def postal_code(self):
        return self._postal_code

    @postal_code.setter
    def postal_code(self, value):
        self._postal_code = value

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.country} - {self.postal_code}"
