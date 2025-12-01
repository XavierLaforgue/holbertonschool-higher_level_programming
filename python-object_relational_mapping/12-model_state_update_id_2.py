#!/usr/bin/python3
"""Start link class to table in database and change name of a State."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    """Change name of a State object from the database
    hbtn_0e_6_usa."""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
            ),
        pool_pre_ping=True,
        echo=False
        )
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        state_to_change = session.get(State, 2)
        if state_to_change:
            state_to_change.name = 'New Mexico'
        session.commit()
