from bin.attributes.BaseAttribute import BaseAttribute
from bin.objects.Proof import Proof


class Name(BaseAttribute):

    def __init__(self, name: str = None, surname: str = None, middlenames: str or list = None, proof: Proof = None):
        super().__init__(proof)
        self._name = name.strip() if name else ''
        self._surname = surname.strip() if surname else ''
        self._middlenames = [name.strip() for name in middlenames] if isinstance(middlenames, list) else [
            middlenames.strip()] if middlenames else []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.strip() if value else ''

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        self._surname = value.strip() if value else ''

    @property
    def middlenames(self):
        return self._middlenames

    @middlenames.setter
    def middlenames(self, value):
        if value:
            if isinstance(value, str):
                value = [value]
            self._middlenames = [name.strip() for name in value]
        else:
            self._middlenames = []

    @property
    def full_name(self):
        """Returns the full name, including all middle names if present."""
        middle_names_str = " ".join(self._middlenames)
        return f"{self._name} {middle_names_str} {self._surname}" if self._middlenames \
            else f"{self._name} {self._surname}"

    @property
    def initials(self):
        """Returns the initials of the name."""
        initials = [self._name[0]] if self._name else []
        initials += [name[0] for name in self._middlenames]
        initials.append(self._surname[0]) if self._surname else ''
        return ".".join(initials) + "." if initials else ''

    def __str__(self):
        return self.full_name

    def __dict__(self):
        return {
            'name': self._name,
            'surname': self._surname,
            'middlenames': self._middlenames,
            'proof': [proof.__dict__() for proof in self.proof]  # Assuming proof is defined in the BaseAttribute class
        }