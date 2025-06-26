"""
Module name: model_state.

Contains a class definition that inherits from Base.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class that will be mapped to a table in a database."""

    __tablename__ = 'states'
    id = Column(
        "id",
        Integer,
        autoincrement="auto",
        nullable=False,
        unique=True,
        primary_key=True
        )
    name = Column(
        "name",
        String(128),
        nullable=False
        )
