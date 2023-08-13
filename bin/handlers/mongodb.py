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

person = Person(dob, name_obj, addr, phone_number, nationality, email, gender,employment_history,
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

    def get_persons(self, person_id=None, DOB=None, name=None, address=None, phone_number=None, nationality=None,
                    email=None, employment_history=None, gender=None, occupation=None, relationship_status=None):
        query = {}
        if person_id:
            query["_id"] = {"$oid": person_id}

        if DOB:
            for key, value in DOB.__dict__().items():
                if value:
                    query[f"DOB.{key}"] = value

        if name:
            for key, value in name.__dict__().items():
                if value:
                    query[f"name.{key}"] = value

        if address:
            for key, value in address.__dict__().items():
                if value:
                    query[f"address.{key}"] = value

        if phone_number:
            for key, value in phone_number.__dict__().items():
                if value:
                    query[f"phone_number.{key}"] = value

        if nationality:
            for key, value in nationality.__dict__().items():
                if value:
                    query[f"nationality.{key}"] = value

        if email:
            for key, value in email.__dict__().items():
                if value:
                    query[f"email.{key}"] = value

        if employment_history:
            pass
        # Handle employment_history fields as needed
        # (May require special handling if employment_history is a list)

        if gender:
            for key, value in gender.__dict__().items():
                if value:
                    query[f"gender.{key}"] = value

        if occupation:
            for key, value in occupation.__dict__().items():
                if value:
                    query[f"occupation.{key}"] = value

        if relationship_status:
            for key, value in relationship_status.__dict__().items():
                if value:
                    query[f"relationship_status.{key}"] = value
        query_result = self.persons_collection.find(query)
        return [person_from_dict(person) for person in query_result]

    def remove_person(self, person_id):
        result = self.persons_collection.delete_one({"_id": person_id})
        return result.deleted_count

test = AllSeeingEye()
print(test.get_persons(name=name_obj))