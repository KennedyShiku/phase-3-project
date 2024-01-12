# cli.py
from lib.database import init_db, db_session
from lib.client import Client
from lib.content import Content
from lib.marketer import Marketer

def initialize_database():
    """Initialize the database."""
    init_db()

    existing_marketers = db_session.query(Marketer).count()
    if existing_marketers >= 10:
        print("Database already initialized with initial marketers.")
        return

    initial_marketers = [
        Marketer(name="Kennedy"),
        Marketer(name="Rich"),
        Marketer(name="Lionel"),
        Marketer(name="Sakina"),
        Marketer(name="Majka"),
        Marketer(name="Jude"),
        Marketer(name="Billie"),
        Marketer(name="Jada"),
        Marketer(name="Kendy"),
        Marketer(name="Dorcas"),
    ]

    for marketer in initial_marketers:
        db_session.add(marketer)

    db_session.commit()
    print("Database initialized with initial marketers.")

def add_client():
    """Add a new client."""
    name = input("Enter client name: ")
    content_type = input("Enter the type of content to be marketed: ")
    
    marketers = db_session.query(Marketer).all()
    print("Available Marketers:")
    for i, marketer in enumerate(marketers, start=1):
        print(f"{i}. {marketer.name}")

    marketer_choice = int(input("Choose a marketer (enter the corresponding number): "))
    chosen_marketer = marketers[marketer_choice - 1]

    new_client = Client(name=name)

    db_session.add(new_client)
    db_session.commit()

    new_content = Content(campaign_name=content_type, client_id=new_client.client_id)
    new_content.marketer = chosen_marketer  # Assign the chosen marketer to the content

    db_session.add(new_content)
    db_session.commit()

    print(f"{name} has been added to the database with their content, {content_type}, marketed by {chosen_marketer.name}.")

def query_and_print_client():
    """Query and print a client."""
    client = db_session.query(Client).first()
    print(client)

if __name__ == "__main__":
    initialize_database()
    add_client()
