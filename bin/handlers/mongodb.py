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
name_obj = Name(name, surname, middlenames, proof=proof)
addr = Address("123 Main St", "New York", "NY", "USA", 10001, proof=proof)
phone_number = PhoneNumber("+1-202-555-0172", proof=proof)
email = Email("john.doe@example.com", proof=proof)
occupation = Occupation("Software Engineer", "Google", "Technology", 3, "23.08.2019", None, proof=proof)
employment_history = EmploymentHistory([occupation])
nationality = Nationality(addr.country, proof=proof)
relationship = RelationshipStatus("Divorced", proof=proof)
gender = Gender("Male", proof=proof)

person = Person(dob, name_obj, addr, phone_number, nationality, email, employment_history, gender,
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

    def get_person(self, person_id=None, address=None, dob=None, email=None, employment_history=None, gender=None,
                   name=None, nationality=None, occupation=None, phone_number=None, relationship_status=None):
        query = {}
        if person_id:
            query["_id"] = {"$oid": person_id}
        if address:
            query["address"] = address.__dict__()
        if dob:
            query["DOB"] = dob.__dict__()
        if email:
            query["email"] = email.__dict__()
        if employment_history:
            query["employment_history"] = employment_history.__dict__()
        if gender:
            query["gender"] = gender.__dict__()
        if name:
            query["name"] = name.__dict__()
        if nationality:
            query["nationality"] = nationality.__dict__()
        if occupation:
            query["occupation"] = occupation.__dict__()
        if phone_number:
            query["phone_number"] = phone_number.__dict__()
        if relationship_status:
            query["relationship_status"] = relationship_status.__dict__()

        psn = self.persons_collection.find_one(query)
        person = person_from_dict(psn)
        return person

    def remove_person(self, person_id):
        result = self.persons_collection.delete_one({"_id": person_id})
        return result.deleted_count

test = AllSeeingEye()
print(test.get_person(name=name_obj))