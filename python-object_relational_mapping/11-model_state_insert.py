#!/usr/bin/python3
"""
Add a States in db
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
    if len(sys.argv) != 4:
        print("Usage: ./script.py <user> <passwd> <db>")
        sys.exit(1)

    username, password, database = sys.argv[1:4]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            username, password, database
        ), pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    with Session() as session:
        new_state = State(name="Louisiana")
        session.add(new_state)
        session.commit()

        state = session.query(State).where(
            State.name == "Louisiana"
            ).first()

        print(state.id)


if __name__ == "__main__":
    main()
