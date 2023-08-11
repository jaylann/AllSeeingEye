from bin.attributes.BaseAttribute import BaseAttribute
from bin.objects.Proof import Proof


class Gender(BaseAttribute):
    def __init__(self, gender: str, proof: Proof):
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
