#!/usr/bin/python3
"""
List all States objects
"""
import sys
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """
    main  - Main function
    Return: Void
    """
    if len(sys.argv) != 4:
        print("Usage: ./script.py <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1:4]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            username, password, database
        ), pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)

    with Session() as session:
        state = session.query(State).order_by(State.id).first()

        if state is None:
            print("Nothing")
        else:
            print("{}: {}".format(state.id, state.name))


if __name__ == "__main__":
    main()
