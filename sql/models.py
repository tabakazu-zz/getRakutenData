from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlAlchemy.base_engine import BaseEngine

#databaseのモデルclass
Base = declarative_base()
Base.metadata.bind=BaseEngine().engine

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    age = Column(Integer)

class Pointsite_Category(Base):
    __tablename__="pointsite_categorylist"
    ID=Column(Integer,primary_key=True)
    pointsite_Name=Column('pointsite_Name',String(128))
    category=Column('category',String(128))
    url=Column('url',String(128))

