from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func

engine = create_engine("sqlite:///mydatabase.db")
Session = sessionmaker(bind=engine)
db = Session()
Base = declarative_base()

def initialize_db():
    Base.metadata.create_all(bind=engine)

class Todo(Base):
    # def __init__(self):
    #     self.__tablename__ = "todo"

    #     self.todoId = Column(Integer, primary_key = True)
    #     self.description = Column(String, nullable = False)
    #     self.status = Column(String, nullable = False)


    __tablename__ = "todo"

    todoId = Column(Integer, primary_key = True)
    description = Column(String, nullable = False)
    status = Column(String, nullable = False)

    def serialize(self):
        return {
            "todoId" : self.todoId,
            "description" : self.description,
            "status" : self.status,
        }
