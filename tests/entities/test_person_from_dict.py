import unittest
from datetime import datetime

from bin.entities.Person import Person


class TestPersonFromDict(unittest.TestCase):

    def test_person_from_dict_normal_case(self):
        person_dict = {
            'DOB': {'DOB': datetime(1990, 8, 15), 'proof': [{'reason': 'placeholder'}]},
            'name': {'name': 'John', 'surname': 'Doe', 'middlenames': ['William'], 'proof': [{'reason': 'placeholder'}]},
            'address': {'street': '123 Main St', 'city': 'New York', 'state': 'NY', 'country': 'US', 'postal_code': 10001, 'proof': [{'reason': 'placeholder'}]},
            'phone_number': {'number': '+12025550172', 'proof': [{'reason': 'placeholder'}]},
            'nationality': {'country': 'US', 'proof': [{'reason': 'placeholder'}]},
            'email': {'email': 'john.doe@example.com', 'proof': [{'reason': 'placeholder'}]},
            'employment_history': {'occupations': [{'job_title': 'Software Engineer', 'company_name': 'Google', 'industry': 'Technology', 'years_experience': 3, 'start_date': datetime(2019, 8, 23), 'end_date': None, 'proof': [{'reason': 'placeholder'}]}]},
            'gender': {'gender': 'Male', 'proof': [{'reason': 'placeholder'}]},
            'occupation': {'job_title': 'Software Engineer', 'company_name': 'Google', 'industry': 'Technology', 'years_experience': 3, 'start_date': datetime(2019, 8, 23), 'end_date': None, 'proof': [{'reason': 'placeholder'}]},
            'relationship_status': {'status': 'Divorced', 'proof': [{'reason': 'placeholder'}]}
        }
        person = Person.from_dict(person_dict)
        assert person.data == person_dict, "Test failed: Normal case"

    def test_person_from_dict_missing_fields(self):
        person_dict = {
            '_id': '64d75e648e361e6c365c75d2',
            'DOB': {'DOB': datetime(1990, 8, 15), 'proof': [{'reason': 'placeholder'}]},
            'name': {'name': 'John', 'surname': 'Doe', 'middlenames': ['William'],
                     'proof': [{'reason': 'placeholder'}]},
            'address': None, 'phone_number': None, 'email': None, 'employment_history': None, 'gender': None,
            'occupation': None, 'relationship_status': None, "nationality": None
        }
        person = Person.from_dict(person_dict)
        self.assertEqual(person.DOB.DOB, datetime(1990, 8, 15), "Test failed: Missing fields")
        self.assertEqual(person.name.name, 'John', "Test failed: Missing fields")
        self.assertIsNone(person.address, "Test failed: Missing fields")
        self.assertIsNone(person.phone_number, "Test failed: Missing fields")
        # Check other missing fields accordingly

    def test_person_from_dict_incorrect_fields(self):
        person_dict = {
            'DOB': '15-08-1990',  # Incorrect: Should be a dictionary with datetime object
            'name': {'name': 'John', 'surname': 'Doe', 'middlenames': 'William', 'proof': 'ID Card'},
            # Incorrect: 'middlenames' should be a list, 'proof' should be a dictionary
            'address': None, 'phone_number': None, 'email': None, 'employment_history': None, 'gender': None,
            'occupation': None, 'relationship_status': None, "nationality": None
        }
        with self.assertRaises(Exception):
            Person.from_dict(person_dict)
            self.fail("Test failed: Incorrect fields")  # Should raise an exception


if __name__ == '__main__':
    unittest.main()
