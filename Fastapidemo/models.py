from sqlalchemy.orm import declarative_base  
#declartive class identify models
#create tables
#map Python classes to database tables
from sqlalchemy import Column,Integer,String,Float
Base=declarative_base()

from pydantic import BaseModel
class Products(Base):
    __tablename__="products"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    desc=Column(String)
    price=Column(Float)
    