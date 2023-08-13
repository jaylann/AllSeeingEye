from bin.attributes.BaseAttribute import BaseAttribute
from bin.objects.Proof import Proof


class Gender(BaseAttribute):
    def __init__(self, gender: str, proof: Proof=None):
        super().__init__(proof)
        self.gender = gender

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        if value not in ['Male', 'Female', 'Other']:
            raise ValueError("Gender must be one of 'Male', 'Female', or 'Other'")
        self._gender = value

    def __str__(self):
        return f"Gender: {self.gender}"

    def __dict__(self):
        return {
            'gender': self.gender,
            'proof': [proof.__dict__() for proof in self.proof] if self.proof else None # Assuming proof is defined in the BaseAttribute class
        }
