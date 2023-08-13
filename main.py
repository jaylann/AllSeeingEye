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
def add(address, dob, email, gender, name, nationality, occupation, phone_number, relationship_status):
    """Add a new person with optional attributes."""

    address_obj = dob_obj = email_obj = gender_obj = name_obj = nationality_obj = occupation_obj = phone_number_obj = relationship_status_obj = None

    if address:
        street = get_user_input('Enter street')
        city = get_user_input('Enter city')
        postal_code = get_user_input('Enter zip code', input_type=int)
        state = get_user_input('Enter state')
        country = get_user_input("Enter country")
        proof = get_user_input('Enter proof reference number')
        address_obj = Address(street=street, city=city, state=state, country=country, postal_code=postal_code,
                              proof=proof)

    if dob:
        dob_value = get_user_input('Enter date of birth (YYYY-MM-DD)', required=True)
        proof = get_user_input('Enter proof reference number')
        dob_obj = DOB(dob=dob_value, proof=proof)

    if email:
        email_value = get_user_input('Enter email', required=True)
        proof = get_user_input('Enter proof reference number')
        email_obj = Email(email=email_value, proof=proof)

    if gender:
        gender_value = get_user_input('Enter gender (Male/Female/Other)', required=True)
        proof = get_user_input('Enter proof reference number')
        gender_obj = Gender(gender=gender_value, proof=proof)

    if name:
        first_name = get_user_input('Enter first name')
        last_name = get_user_input('Enter last name')
        middle_names = get_user_input('Enter middle names (comma separated)')
        proof = get_user_input('Enter proof reference number')
        name_obj = Name(name=first_name, surname=last_name, middlenames=middle_names, proof=proof)

    if nationality:
        nationality_value = get_user_input('Enter nationality', required=True)
        proof = get_user_input('Enter proof reference number')
        nationality_obj = Nationality(country=nationality_value, proof=proof)

    if occupation:
        job_title = get_user_input('Enter job title')
        company_name = get_user_input('Enter company name')
        industry = get_user_input('Enter industry')
        years_experience = get_user_input('Enter years of experience', input_type=int) or None
        start_date = get_user_input('Enter start date (YYYY-MM-DD)')
        end_date = get_user_input('Enter end date (YYYY-MM-DD)')
        proof = get_user_input('Enter proof reference number')
        occupation_obj = Occupation(job_title=job_title, company_name=company_name, industry=industry,
                                    years_experience=years_experience, start_date=start_date, end_date=end_date,
                                    proof=proof)

    if phone_number:
        phone_number_value = get_user_input('Enter phone number', required=True)
        country_context = get_user_input("Enter country context (optional)")
        proof = get_user_input('Enter proof reference number')
        print(phone_number_value)
        phone_number_obj = PhoneNumber(number=phone_number_value, country_context=country_context, proof=proof)

    if relationship_status:
        relationship_status_value = get_user_input('Enter relationship status', required=True)
        proof = get_user_input('Enter proof reference number')
        relationship_status_obj = RelationshipStatus(relationship_status=relationship_status_value, proof=proof)

    uid = database.add_person(Person(
        dob=dob_obj, name=name_obj, address=address_obj, phone_number=phone_number_obj, nationality=nationality_obj,
        email=email_obj, gender=gender_obj, occupation=occupation_obj,
        relationship_status=relationship_status_obj
    ))
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
