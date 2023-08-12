from bin.attributes.Occupation import Occupation


class EmploymentHistory:
    def __init__(self, occupations: list[Occupation]):
        self.occupations = sorted(occupations, key=lambda x: x.start_date)

    @property
    def occupations(self):
        return self._occupations

    @occupations.setter
    def occupations(self, value):
        self._occupations = value

    def add_occupation(self, occupation: Occupation):
        self._occupations.append(occupation)
        self._occupations.sort(key=lambda x: x.start_date)

    def remove_occupation(self, occupation: Occupation):
        self._occupations.remove(occupation)

    def __str__(self):
        return "\n".join(str(occupation) for occupation in self._occupations)

    def __dict__(self):
        return {
            'occupations': [occupation.__dict__() if hasattr(occupation, '__dict__') else str(occupation) for occupation
                            in self._occupations]
        }