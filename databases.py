from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def create_product(seller, buyer, quantity, price):
	
	product_object = Product(
		seller = seller,
		buyer = buyer,
		quantity = quantity,
		price = price)

	session.add(product_object)
	session.commit()

create_product("John", "Mike", 3, 40.75)

def update_product():
  #TODO: complete the functions (you will need to change the function's inputs)
  pass

def delete_product(id):
	session.query(Product).filter_by(
		seller="John the seller").delete()
	session.commit()
delete_product("John the seller")

 

def get_product(id):
  pass

