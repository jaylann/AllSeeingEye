from typing import Optional
from bin.attributes.BaseAttribute import BaseAttribute
from bin.objects.Proof import Proof


class RelationshipStatus(BaseAttribute):
    """
    RelationshipStatus class that extends BaseAttribute.
    It represents a person's relationship status, which must be one of the predefined valid statuses.

    Attributes:
        status (str): The relationship status.
    """

    # A list of valid relationship statuses
    VALID_STATUSES = [
        'Single', 'Married', 'Divorced', 'Widowed', 'Engaged',
        'In a Relationship', 'Separated', 'Complicated', 'Polyamorous',
        'Friends with Benefits', 'Casually Dating', 'Open Relationship'
    ]

    def __init__(self, status: str, proof: Optional[Proof] = None):
        """
        Initializes the RelationshipStatus object.

        Args:
            status (str): The relationship status, must be one of the valid statuses.
            proof (Optional[Proof], default=None): Proof associated with the relationship status.

        Raises:
            ValueError: If the provided relationship status is not valid.
        """
        super().__init__(proof)
        self.status = status  # Calls the status setter method

    @property
    def status(self) -> str:
        """Returns the relationship status."""
        return self._status

    @status.setter
    def status(self, value: str):
        """
        Sets the relationship status, validating against the predefined valid statuses.

        Args:
            value (str): The relationship status to set.

        Raises:
            ValueError: If the provided relationship status is not valid.
        """
        # Convert the value to the correct capitalization if it is in the list of valid statuses
        matching_status = next((s for s in RelationshipStatus.VALID_STATUSES if s.lower() == value.lower()), None)
        if matching_status is None:
            raise ValueError(
                f"Invalid relationship status. Must be one of: {', '.join(RelationshipStatus.VALID_STATUSES)}")
        self._status = matching_status

    def __str__(self) -> str:
        """Returns the string representation of the relationship status."""
        return f"Relationship Status: {self.status}"

    def __dict__(self) -> dict:
        """Returns a dictionary representation of the RelationshipStatus object, including proofs if available."""
        return {
            'status': self._status,
            # Convert proof objects to dictionaries if proof attribute is defined in the BaseAttribute class
            'proof': [proof.__dict__() for proof in self.proof] if self.proof else None
        }
