#!/usr/bin/python3
"""Start link class to table in database."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session


def model_state_fetch_first():
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
            ),
        pool_pre_ping=True,
        echo=False
        )
    Base.metadata.create_all(engine)

    session = Session(engine)
    stmt = select(State)
    state = session.scalars(stmt).first()
    if state:
        print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    model_state_fetch_first()
