#!/usr/bin/python3
"""
List cities from db
"""
import sys
from model_state import Base, State
from model_city import City

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
        results = session.query(City, State).join(
                State, City.state_id == State.id
                ).order_by(City.id).all()

        for row in results:
            print("{}: ({}) {}".format(
                row.State.name,
                row.City.id,
                row.City.name
            ))


if __name__ == "__main__":
    main()
