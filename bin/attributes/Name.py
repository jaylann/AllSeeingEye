from bin.attributes.BaseAttribute import BaseAttribute


class Name(BaseAttribute):
    def __init__(self, name, surname, proof, middlenames=None):
        super().__init__(proof)
        self._name = name
        self._surname = surname
        self._middlenames = middlenames if middlenames else []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.strip()

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        self._surname = value.strip()

    @property
    def middlenames(self):
        return self._middlenames

    @middlenames.setter
    def middlenames(self, value):
        if value:
            self._middlenames = [name.strip() for name in value]
        else:
            self._middlenames = []

    def full_name(self):
        """Returns the full name, including all middle names if present."""
        middle_names_str = " ".join(self._middlenames)
        return f"{self._name} {middle_names_str} {self._surname}" if self._middlenames \
            else f"{self._name} {self._surname}"

    def initials(self):
        """Returns the initials of the name."""
        initials = [self._name[0], self._surname[0]]
        initials += [name[0] for name in self._middlenames]
        return ".".join(initials) + "."

    def __str__(self):
        return self.full_name()
