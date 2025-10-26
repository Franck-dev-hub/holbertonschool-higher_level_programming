#!/usr/bin/python3
"""
List all States objects from the arg
"""
import sys
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound


def main():
    """
    main  - Main function
    Return: Void
    """
    if len(sys.argv) != 5:
        print("Usage: ./script.py <user> <passwd> <db> <state>")
        sys.exit(1)

    username, password, database, state = sys.argv[1:5]

    if "'" in state:
        sys.exit()

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            username, password, database
        ), pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    with Session() as session:
        try:
            states = session.query(State).where(
                State.name == state
            ).order_by(State.id).limit(1).one()
        except NoResultFound:
            print("Not found")
        else:
            print("{}".format(states.id))


if __name__ == "__main__":
    main()
