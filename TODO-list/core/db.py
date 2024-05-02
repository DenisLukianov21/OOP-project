from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Boolean, DateTime

sqlite_database = "sqlite:///tasks.db"
engine = create_engine(sqlite_database)
Session = sessionmaker(autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


class TaskDB(Base):
    """
    TaskDB is a SQLAlchemy declarative base class that represents a
    table in the database.
    This class has the following fields:

    - id: Integer, primary key, index.
    - name: String.
    - description: String.
    - status: Boolean.
    - time: DateTime.
    """

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    status = Column(Boolean)
    time = Column(DateTime)


Base.metadata.create_all(bind=engine)
