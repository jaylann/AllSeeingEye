from bin.attributes.BaseAttribute import BaseAttribute
from bin.objects.Proof import Proof


class Nationality(BaseAttribute):
    def __init__(self, country: str, proof: Proof = None):
        super().__init__(proof)
        self.country = country

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value

    def __str__(self):
        return f"{self.country}"

    def __dict__(self):
        return {
            'country': self._country,
            'proof': [proof.__dict__() for proof in self.proof]  # Assuming proof is defined in the BaseAttribute class
        }
