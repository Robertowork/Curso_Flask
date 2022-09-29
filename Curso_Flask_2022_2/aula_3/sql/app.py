# UTF-8

import sqlalchemy
engine = sqlalchemy.create_engine('sqlite:///db.sqlite', echo=True)

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

# crindo uma classe usuario
class User(Base):
    tablename = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    age = Column(Integer)

    def repr(self):
        return "<User(name={}, fullname={}, age={})>".format(self.name, self.fullname, self.age)

# criando o banco e instanciando o objeto 
Base.metadata.create_all(engine)

roberto = User(name="Roberto", fullname="Roberto Junior", age=22)

