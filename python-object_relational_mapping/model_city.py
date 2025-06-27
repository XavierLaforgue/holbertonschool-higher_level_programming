#!/usr/bin/python3
"""
Module name: model_city.

Contains a class definition that inherits from Base.
"""
from model_state import Base, State
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.orm import mapped_column


class City(Base):
    """Class that will be mapped to a table in a database."""

    __tablename__ = 'cities'
    id: Mapped[int] = mapped_column(
        "id",
        autoincrement="auto",
        nullable=False,
        unique=True,
        primary_key=True
        )
    name: Mapped[str] = mapped_column(
        "name",
        String(128),
        nullable=False
        )
    state_id: Mapped[int] = mapped_column("state_id",
                                          ForeignKey("states.id"),
                                          nullable=False
                                          )
