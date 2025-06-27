#!/usr/bin/python3
"""Start link class to table in database and add Louisiana to State."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, select, insert
from sqlalchemy.orm import Session


if __name__ == "__main__":
    """Add the State object 'Louisiana' to the database
    hbtn_0e_6_usa."""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
            ),
        pool_pre_ping=True,
        echo=False
        )
    Base.metadata.create_all(engine)

    # with Session(engine) as session:
    #     stmt = insert(State).values(name='Louisiana')
    #     inserted_id = session.execute(stmt).inserted_primary_key
    #     session.commit()

    # if inserted_id:
    #     print(f"{inserted_id[0]}")

    with Session(engine) as session:
        new_state = State(name='Louisiana')
        session.add(new_state)
        session.commit()
        print(new_state.id)
