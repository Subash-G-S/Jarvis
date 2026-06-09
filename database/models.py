from sqlalchemy import (
    Column,
    Integer,
    String
)
from sqlalchemy import Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Memory(Base):

    __tablename__ = "memories"

    id = Column(
        Integer,
        primary_key=True
    )

    category = Column(
        String
    )

    key = Column(
        String,
        unique=True
    )

    value = Column(
        String
    )
    
class Task(Base):

    __tablename__ = "tasks"

    id = Column(
        Integer,
        primary_key=True
    )

    title = Column(
        String
    )

    completed = Column(
        Boolean,
        default=False
    )