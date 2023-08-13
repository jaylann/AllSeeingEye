import click

from bin.attributes.DOB import DOB
from bin.entities.Person import Person
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
@click.option('--address', default=None, help='Address of the person.')
@click.option('--dob', default=None, help='Date of birth of the person.')
@click.option('--email', default=None, help='Email of the person.')
@click.option('--employment-history', default=None, help='Employment history of the person.')
@click.option('--gender', default=None, help='Gender of the person.')
@click.option('--name', default=None, help='Name of the person.')
@click.option('--nationality', default=None, help='Nationality of the person.')
@click.option('--occupation', default=None, help='Occupation of the person.')
@click.option('--phone-number', default=None, help='Phone number of the person.')
@click.option('--relationship-status', default=None, help='Relationship status of the person.')
def add(address, dob, email, employment_history, gender, name, nationality, occupation, phone_number, relationship_status):
    """Add a new person with optional attributes."""
    # Process the attributes here
    dob = DOB()
    uid = database.add_person(Person(dob, name, address, phone_number, nationality, email, employment_history, gender, occupation, relationship_status))
    click.echo(f"Adding person with Name: {name}, Address: {address}, DOB: {dob}, Email: {email}, Employment History: {employment_history}, Gender: {gender}, Nationality: {nationality}, Occupation: {occupation}, Phone Number: {phone_number}, Relationship Status: {relationship_status}")
    click.echo(f"Person Unique ID: {uid}")

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
def Address(address):
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
