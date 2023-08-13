from typing import Dict, Any

import click

from bin.attributes.Address import Address
from bin.attributes.DOB import DOB
from bin.attributes.Email import Email
from bin.attributes.Gender import Gender
from bin.attributes.Name import Name
from bin.attributes.Nationality import Nationality
from bin.attributes.Occupation import Occupation
from bin.attributes.PhoneNumber import PhoneNumber
from bin.attributes.RelationshipStatus import RelationshipStatus
from bin.entities.Person import Person
from bin.handlers.InputHandlers import get_user_input


class PersonCommands:
    def __init__(self, database):
        self.database = database

    def get_attribute_input(self, attribute_name: str, required: bool = False) -> Dict[str, Any]:
        prompt_suffix = ('proof', 'Enter proof reference number', str)
        prompts = {
            'address': [('street', 'Enter street', str), ('city', 'Enter city', str),
                        ('postal_code', 'Enter zip code', int),
                        ('state', 'Enter state', str), ('country', 'Enter country', str)],
            'dob': [('dob', 'Enter date of birth (YYYY-MM-DD)', str)],
            'email': [('email', 'Enter email', str)],
            'gender': [('gender', 'Enter gender (Male/Female/Other)', str)],
            'name': [('name', 'Enter first name', str), ('surname', 'Enter last name', str),
                     ('middlenames', 'Enter middle names (comma separated)', str)],
            'nationality': [('nationality', 'Enter nationality', str)],
            'occupation': [('job_title', 'Enter job title', str), ('company_name', 'Enter company name', str),
                           ('industry', 'Enter industry', str),
                           ('years_of_experience', 'Enter years of experience', int),
                           ('start_date', 'Enter start date (YYYY-MM-DD)', str),
                           ('end_date', 'Enter end date (YYYY-MM-DD)', str)],
            'phone_number': [('number', 'Enter phone number', str),
                             ('country_context', 'Enter country context (optional)', str)],
            'relationship_status': [('relationship_status', 'Enter relationship status', str)],
        }

        # Appending 'proof' to each prompt
        for key in prompts:
            prompts[key].append(prompt_suffix)

        inputs = {
            param_name: get_user_input(prompt, input_type=input_type,
                                       required=(required if param_name != 'proof' else False))
            for param_name, prompt, input_type in prompts[attribute_name]
        }
        return inputs

    def add(self, address: bool, dob: bool, email: bool, gender: bool, name: bool, nationality: bool, occupation: bool,
            phone_number: bool, relationship_status: bool):
        """Add a new person with optional attributes."""
        attribute_mapping = {
            'address': (address, Address),
            'dob': (dob, DOB),
            'email': (email, Email),
            'gender': (gender, Gender),
            'name': (name, Name),
            'nationality': (nationality, Nationality),
            'occupation': (occupation, Occupation),
            'phone_number': (phone_number, PhoneNumber),
            'relationship_status': (relationship_status, RelationshipStatus),
        }

        attributes_obj = {
            attribute: cls(**self.get_attribute_input(attribute, required=(attribute in ['dob', 'email', 'gender'])))
            for attribute, (flag, cls) in attribute_mapping.items() if flag
        }

        uid = self.database.add_person(Person(**attributes_obj))
        click.echo(f"Person added successfully with Unique ID: {uid}")

    def remove(self, uid):
        """Remove a person by ID."""
        click.echo(f"Removing person with ID: {uid}")


def get_person_group(database):
    person_commands = PersonCommands(database)

    @click.group()
    def person():
        """Commands related to persons."""
        pass

    @person.command()
    @click.option('--address', is_flag=True, help='Address of the person.')
    @click.option('--dob', is_flag=True, help='Date of birth of the person.')
    @click.option('--email', is_flag=True, help='Email of the person.')
    @click.option('--gender', is_flag=True, help='Gender of the person.')
    @click.option('--name', is_flag=True, help='Name of the person.')
    @click.option('--nationality', is_flag=True, help='Nationality of the person.')
    @click.option('--occupation', is_flag=True, help='Occupation of the person.')
    @click.option('--phone-number', is_flag=True, help='Phone number of the person.')
    @click.option('--relationship-status', is_flag=True, help='Relationship status of the person.')
    def add(address: bool, dob: bool, email: bool, gender: bool, name: bool, nationality: bool, occupation: bool,
            phone_number: bool, relationship_status: bool):
        """Add a new person with optional attributes."""
        person_commands.add(address, dob, email, gender, name, nationality, occupation, phone_number,
                            relationship_status)

    @person.command()
    @click.argument('id', type=str, required=True)
    def remove(id):
        """Remove a person by ID."""
        person_commands.remove(id)

    # ... other person-related commands and groups ...

    return person
