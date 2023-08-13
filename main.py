import click

from bin.attributes.Address import Address
from bin.attributes.DOB import DOB
from bin.attributes.Email import Email
from bin.attributes.Gender import Gender
from bin.attributes.Name import Name
from bin.attributes.Nationality import Nationality
from bin.attributes.Occupation import Occupation
from bin.attributes.PhoneNumber import PhoneNumber
from bin.entities.Person import Person
from bin.handlers.InputHandlers import get_user_input
from bin.handlers.mongodb import AllSeeingEye

database = AllSeeingEye()


@click.group()
def cli():
    """Main command group for managing persons and records."""
    pass


@click.group()
def person():
    """Commands related to persons."""
    pass


cli.add_command(person)

from typing import Dict, Any


def get_attribute_input(attribute_name: str, required: bool = False) -> Dict[str, Any]:
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
                       ('industry', 'Enter industry', str), ('years_of_experience', 'Enter years of experience', int),
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
        attribute: cls(**get_attribute_input(attribute, required=(attribute in ['dob', 'email', 'gender'])))
        for attribute, (flag, cls) in attribute_mapping.items() if flag
    }

    uid = database.add_person(Person(**attributes_obj))
    click.echo(f"Person added successfully with Unique ID: {uid}")


@person.command()
@click.argument('id', type=str, required=True)
def remove(id):
    """Remove a person by ID."""
    click.echo(f"Removing person with ID: {id}")


@person.group()
@click.argument('identifier')
def modify(identifier):
    """Modify a person's attributes by name or ID."""
    click.echo(f"Modifying person with ID or name: {identifier}")


@modify.command()
@click.argument('address')
def Addraess(address):
    """Add or modify address."""
    click.echo(f"Setting address to {address}")


# Repeat for other attributes...

@modify.command()
@click.argument('relationship_status')
def RelationshipStatus(relationship_status):
    """Add or modify relationship status."""
    click.echo(f"Setting relationship status to {relationship_status}")


@person.command()
@click.argument('identifier', type=str, required=True)
@click.argument('attribute', type=str, required=True)
@click.argument('proof', type=str, required=True)
def add_attribute(identifier, attribute, proof):
    """Add an attribute to a person by ID or name, with proof."""
    click.echo(f"Adding attribute {attribute} with proof {proof} to person with ID or name: {identifier}")


@person.command()
@click.argument('identifier')
@click.argument('attribute')
@click.argument('proof')
def remove_attribute(identifier, attribute, proof):
    """Remove an attribute from a person."""
    click.echo(f"Removing attribute {attribute} with proof {proof} from person {identifier}.")


@person.command()
@click.argument('identifier')
@click.argument('data')
def add_data(identifier, data):
    """Add data to a person."""
    click.echo(f"Adding data {data} to person {identifier}.")


@click.group()
def record():
    """Commands related to records."""
    pass


cli.add_command(record)


@record.command()
@click.argument('type', type=click.Choice(['text', 'audio', 'video', 'image']))
def add(type):
    """Add a record of a given type."""
    click.echo(f"Adding {type} record.")


@record.command()
@click.argument('recordid')
def remove(recordid):
    """Remove a record by ID."""
    click.echo(f"Removing record with ID: {recordid}")


if __name__ == "__main__":
    cli()
