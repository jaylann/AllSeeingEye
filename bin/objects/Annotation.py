class Annotation:
    def __init__(self, indexes, annotation):
        self._annotation = annotation
        self._indexes = indexes

    @property
    def annotation(self):
        return self._annotation

    @annotation.setter
    def annotation(self, value):
        self._annotation = value

    @property
    def indexes(self):
        return self._indexes

    @indexes.setter
    def indexes(self, value):
        if isinstance(value, list) and all(isinstance(i, int) for i in value):
            self._indexes = value
