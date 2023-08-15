from pymongo import MongoClient

from bin.attributes.Address import Address
from bin.attributes.DOB import DOB
from bin.attributes.Email import Email
from bin.attributes.EmploymentHistory import EmploymentHistory
from bin.attributes.Gender import Gender
from bin.attributes.Name import Name
from bin.attributes.Nationality import Nationality
from bin.attributes.Occupation import Occupation
from bin.attributes.PhoneNumber import PhoneNumber
from bin.attributes.RelationshipStatus import RelationshipStatus
from bin.entities.Person import Person
from bin.objects.Proof import Proof
from bin.entities.Person import person_from_dict

proof = Proof("ID Card")  # Assuming Proof class is defined
dob = DOB("15-08-1990", proof)
name = "John"
surname = "Doe"
middlenames = ["William"]
name_obj = Name(name="Justin", surname="Lanfermann")
addr = Address("123 Main St", "New York", "NY", "USA", 10001, proof=proof)
phone_number = PhoneNumber("+1-202-555-0172", proof=proof)
email = Email("john.doe@example.com", proof=proof)
occupation = Occupation("Software Engineer", "Google", "Technology", 3, "23.08.2019", None, proof=proof)
employment_history = EmploymentHistory([occupation])
nationality = Nationality(addr.country, proof=proof)
relationship = RelationshipStatus("Divorced", proof=proof)
gender = Gender("Male", proof=proof)

person = Person(dob, name_obj, addr, phone_number, nationality, email, gender, employment_history,
                occupation, relationship)


class AllSeeingEye:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['AllSeeingEye']
        self.persons_collection = self.db['Persons']
        self.objects_collection = self.db['Objects']

    def add_person(self, person):
        # Convert DOB to a datetime object if provided as a string

        result = self.persons_collection.insert_one(person.data)
        return result.inserted_id

    def _build_query(self, attribute_obj):
        """Helper function to build MongoDB query based on an attribute object."""
        query = {}
        if attribute_obj:
            for key, value in attribute_obj.__dict__().items():
                if value:
                    query[key] = value
        return query

    def get_persons(self, person_id=None, DOB=None, name=None, address=None, phone_number=None, nationality=None,
                    email=None, employment_history=None, gender=None, occupation=None, relationship_status=None):
        query = {}

        if person_id:
            query["_id"] = {"$oid": person_id}

        query.update({"DOB." + k: v for k, v in self._build_query(DOB).items()})
        query.update({"name." + k: v for k, v in self._build_query(name).items()})
        query.update({"address." + k: v for k, v in self._build_query(address).items()})
        query.update({"phone_number." + k: v for k, v in self._build_query(phone_number).items()})
        query.update({"nationality." + k: v for k, v in self._build_query(nationality).items()})
        query.update({"email." + k: v for k, v in self._build_query(email).items()})
        query.update({"gender." + k: v for k, v in self._build_query(gender).items()})
        query.update({"occupation." + k: v for k, v in self._build_query(occupation).items()})
        query.update({"relationship_status." + k: v for k, v in self._build_query(relationship_status).items()})

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


    def remove_person(self, person_id):
        result = self.persons_collection.delete_one({"_id": person_id})
        return result.deleted_count


test = AllSeeingEye()
print(test.get_persons(name=name_obj))
