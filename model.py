from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class Product(Base):
    # TODO: complete this class

    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    seller = Column(String)
    buyer = Column(String)
    quantity = Column(Integer)
    price = Column(Integer)
    



