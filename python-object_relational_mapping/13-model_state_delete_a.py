#!/usr/bin/python3
"""Start link class to table in database and delete a State object."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, delete
from sqlalchemy.orm import Session


if __name__ == "__main__":
    """Delete all State objects with a name containing the leter 'a'
    from the database hbtn_0e_6_usa."""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
            ),
        pool_pre_ping=True,
        echo=False
        )
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        stmt = delete(State).where(State.name.like('%a%'))
        session.execute(stmt)
        session.commit()
