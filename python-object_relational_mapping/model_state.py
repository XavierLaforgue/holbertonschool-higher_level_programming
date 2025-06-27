#!/usr/bin/python3
"""
Module name: model_state.

Contains a class definition that inherits from Base.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass


class State(Base):
    """Class that will be mapped to a table in a database."""

    __tablename__ = 'states'
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
