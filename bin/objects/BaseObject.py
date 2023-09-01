from bin.handlers.mongodb import AllSeeingEye
from bson import ObjectId
connector = AllSeeingEye()

class BaseObject:
    COLLECTION_NAME = None  # Should be overridden by child class

    def __init__(self):
        self.uid = ObjectId()

    def save(self):
        """
        Save the object to the database.
        """
        if not self.COLLECTION_NAME:
            raise ValueError("COLLECTION_NAME must be defined in child class.")
        data = self.to_dict()
        connector.insert_one(self.COLLECTION_NAME, data)

    def remove(self):
        """
        Remove the object from the database.
        """
        if not hasattr(self, 'uid') or not self.uid:
            raise ValueError("Object doesn't have a valid 'uid' attribute.")
        connector.delete_one(self.COLLECTION_NAME, {"_id": self.uid})

    @classmethod
    def find_by_attributes(cls, **kwargs):
        """
        Retrieve objects based on the provided filters.

        Args:
        - kwargs (dict): Dictionary of filters.

        Returns:
        - list[BaseObject]: List of objects of the class type.
        """
        query = cls._form_query(kwargs)
        query_result = connector.find(cls.COLLECTION_NAME, query)
        return [cls.from_dict(obj_dict) for obj_dict in query_result]

    @classmethod
    def _form_query(cls, filters):
        """
        Helper function to form a MongoDB query based on filters.

        Args:
        - filters (dict): Dictionary of filters.

        Returns:
        - dict: The formed query.
        """
        query = {}
        for key, value in filters.items():
            if value is not None:
                if isinstance(value, (int, str, float, bool, bytes)):  # Check for basic data types
                    query[key] = value
                else:
                    query.update(
                        {f"{key}.{sub_key}": sub_value for sub_key, sub_value in cls._build_query(value).items()})
        return query

    @classmethod
    def _build_query(cls, attribute_obj):
        """
        Helper function to build MongoDB query based on an attribute object.

        Args:
        - attribute_obj (obj): The attribute object.

        Returns:
        - dict: The query dictionary.
        """
        query = {}
        if attribute_obj is not None:
            for key, value in attribute_obj.__dict__().items():
                if value:
                    query[key] = value
        return query

    def to_dict(self):
        """
        Convert the object to a dictionary. 
        Should be implemented by child classes to return a dictionary representation of the object.
        """
        raise NotImplementedError("to_dict() should be implemented in child classes.")

    @classmethod
    def from_dict(cls, obj_dict):
        """
        Convert dictionary back to the object.
        Should be implemented by child classes to reconstruct the object from a dictionary.
        """
        raise NotImplementedError("from_dict() should be implemented in child classes.")
