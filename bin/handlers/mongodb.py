from pymongo import MongoClient

from bin.entities.Person import person_from_dict


class AllSeeingEye:
    """
    A class to interact with the MongoDB database to perform CRUD operations on person data.
    """

    def __init__(self, db_url='mongodb://localhost:27017/', db_name='AllSeeingEye'):
        """
        Initializes the database connection and collections.

        Args:
        - db_url (str): The database connection string.
        - db_name (str): The name of the database.
        """
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.persons_collection = self.db['Persons']
        self.objects_collection = self.db['Objects']

    def add_person(self, person):
        """
        Adds a person to the database.

        Args:
        - person (Person): The person object.

        Returns:
        - ObjectId: The ID of the inserted person.
        """
        result = self.persons_collection.insert_one(person.data)
        return result.inserted_id

    def _build_query(self, attribute_obj):
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

    def get_persons(self, person_id=None, DOB=None, name=None, address=None, phone_number=None, nationality=None,
                    email=None, employment_history=None, gender=None, occupation=None, relationship_status=None):
        """
        Retrieves persons based on the provided filters.

        Args:
        - person_id (ObjectId, optional): The ID of the person.
        - DOB (DOB, optional): Date of birth filter.
        ... [other filters]

        Returns:
        - list[Person]: List of person objects.
        """
        query = self._form_query({
            "_id": person_id,
            "DOB": DOB,
            "name": name,
            "address": address,
            "phone_number": phone_number,
            "nationality": nationality,
            "email": email,
            "gender": gender,
            "occupation": occupation,
            "relationship_status": relationship_status
        })

        # Handle employment_history with custom logic
        if employment_history:
            or_conditions = []
            for occupation in employment_history.occupations:
                occupation_query = self._build_query(occupation)
                if occupation_query:
                    or_conditions.append({"employment_history.occupations": {"$elemMatch": occupation_query}})
            if or_conditions:
                query["$or"] = or_conditions

        query_result = self.persons_collection.find(query)
        return [person_from_dict(person) for person in query_result]

    def _form_query(self, filters):
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
                query.update({f"{key}.{sub_key}": sub_value for sub_key, sub_value in self._build_query(value).items()})
        return query

    def remove_person(self, person_id):
        """
        Removes a person from the database.

        Args:
        - person_id (ObjectId): The ID of the person to remove.

        Returns:
        - int: The count of deleted persons (0 or 1).
        """
        result = self.persons_collection.delete_one({"_id": person_id})
        return result.deleted_count
