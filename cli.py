# cli.py
import click
from tabulate import tabulate  # Import tabulate for nice table formatting
from lib.database import init_db, db_session
from lib.client import Client
from lib.content import Content
from lib.marketer import Marketer

@click.group()
def cli():
    pass

@cli.command()
def initialize_database():
    """Initialize the database."""
    init_db()
    print("Database initialized with initial marketers.")

@cli.command()
def add_client():
    """Add a new client."""
    name = click.prompt("Enter client name")
    content_type = click.prompt("Enter the type of content to be marketed")

    marketers = db_session.query(Marketer).all()
    click.echo("Available Marketers:")
    for i, marketer in enumerate(marketers, start=1):
        click.echo(f"{i}. {marketer.name}")

    marketer_choice = click.prompt("Choose a marketer (enter the corresponding number)", type=int)
    chosen_marketer = marketers[marketer_choice - 1]

    new_client = Client(name=name)
    db_session.add(new_client)
    db_session.commit()

    new_content = Content(campaign_name=content_type, client_id=new_client.client_id)
    new_content.marketer = chosen_marketer

    db_session.add(new_content)
    db_session.commit()

    click.echo(f"{name} added to the database with their content, {content_type}, marketed by {chosen_marketer.name}.")

@cli.command()
def remove_client():
    """Remove a client and associated content."""
    client_id = click.prompt("Enter the ID of the client to remove", type=int)
    
    client = db_session.query(Client).get(client_id)
    if client:
        # Remove associated content first
        content = db_session.query(Content).filter_by(client_id=client_id).first()
        if content:
            db_session.delete(content)

        # Remove the client
        db_session.delete(client)
        db_session.commit()

        click.echo(f"Client {client.name} (ID: {client.client_id}) and associated content removed from the database.")
    else:
        click.echo(f"No client found with ID {client_id}.")

@cli.command()
def query_and_print_client():
    """Query and print a client."""
    client = db_session.query(Client).first()
    click.echo(client)

@cli.command()
def display_tables():
    """Display contents of clients, contents, and marketers tables."""
    clients = db_session.query(Client).all()
    contents = db_session.query(Content).all()
    marketers = db_session.query(Marketer).all()

    click.echo("Clients Table:")
    click.echo(tabulate([(client.client_id, client.name) for client in clients], headers=["Client ID", "Name"], tablefmt="grid"))

    click.echo("\nContents Table:")
    click.echo(tabulate([(content.content_id, content.campaign_name, content.client_id) for content in contents], headers=["Content ID", "Campaign Name", "Client ID"], tablefmt="grid"))

    click.echo("\nMarketers Table:")
    click.echo(tabulate([(marketer.marketer_id, marketer.name) for marketer in marketers], headers=["Marketer ID", "Name"], tablefmt="grid"))

if __name__ == "__main__":
    cli()
