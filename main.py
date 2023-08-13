import click

from bin.cli.PersonCommands import get_person_group
from bin.handlers.mongodb import AllSeeingEye

database = AllSeeingEye()
person_group = get_person_group(database)


@click.group()
def cli():
    """Main command group for managing persons and records."""
    pass


cli.add_command(person_group)


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
