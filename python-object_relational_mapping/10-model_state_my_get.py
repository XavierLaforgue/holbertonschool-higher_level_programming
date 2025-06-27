#!/usr/bin/python3
"""Start link class to table in database and list states with a."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session


if __name__ == "__main__":
    """List all State objects that contain the letter 'a' from the
    database hbtn_0e_6_usa."""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
            ),
        pool_pre_ping=True,
        echo=False
        )
    Base.metadata.create_all(engine)

    state_name = sys.argv[4]
    session = Session(engine)
    stmt = select(State).filter(State.name == state_name)
    state = session.scalar(stmt)
    if state:
        print(f"{state.id}")
    else:
        print("Not found")
