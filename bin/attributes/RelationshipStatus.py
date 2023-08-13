from bin.attributes.BaseAttribute import BaseAttribute
from bin.objects.Proof import Proof


class RelationshipStatus(BaseAttribute):
    VALID_STATUSES = [
        'Single', 'Married', 'Divorced', 'Widowed', 'Engaged',
        'In a Relationship', 'Separated', 'Complicated', 'Polyamorous',
        'Friends with Benefits', 'Casually Dating', 'Open Relationship'
    ]

    def __init__(self, status: str, proof: Proof = None):
        super().__init__(proof)
        self.status = status

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value not in RelationshipStatus.VALID_STATUSES:
            raise ValueError(
                f"Invalid relationship status. Must be one of: {', '.join(RelationshipStatus.VALID_STATUSES)}")
        self._status = value

    def __str__(self):
        return f"Relationship Status: {self.status}"

    def __dict__(self):
        return {
            'status': self._status,
            'proof': [proof.__dict__() for proof in self.proof] if self.proof else None # Assuming proof is defined in the BaseAttribute class
        }