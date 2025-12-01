#!/usr/bin/python3
"""Start link class to table in database and print all City objects."""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine, select, delete
from sqlalchemy.orm import Session


if __name__ == "__main__":
    """Print all City objects from the database hbtn_0e_6_usa."""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
            ),
        pool_pre_ping=True,
        echo=False
        )
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        stmt = select(City, State).join(State,
                                        City.state_id == State.id).\
                                            order_by(City.id.asc())
        for city, state in session.execute(stmt):
            print(f"{state.name}: ({city.id}) {city.name}")
