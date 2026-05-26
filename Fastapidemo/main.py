from fastapi import FastAPI
from models import Products
from database import engine,SessionLocal
from models import Base,Products
from schemas import Productschema
from sqlalchemy import text
app=FastAPI()
@app.get("/")
def test_db():
    with engine.connect() as connection:
        result=connection.execute(text("select 1"))
    
    return {"message":"welcome to telusko "}


# old_product=[s
#     Products(
#     id=1,name="Laptop",desc="High performance gaming laptop",price=75999.99
# ),
#     Products(
#     id=2,name="Smartphone",desc="5G Android smartphone",price=28999.50
# ),
#     Products(
#     id=3,
#     name="Headphones",
#     desc="Wireless noise cancelling headphones",
#     price=4999.00
# ),

# Products(
#     id=4,
#     name="Smart Watch",
#     desc="Fitness tracking smartwatch",
#     price=7999.75
# ),

# Products(
#     id=5,
#     name="Keyboard",
#     desc="Mechanical RGB keyboard",
#     price=2499.99
# )
    
    
    
# ]
Base.metadata.create_all(bind=engine)
db=SessionLocal()
# for item in old_product:
#     db.add(item)
#     del old_product 
#     db.commit()
    
#get all data
@app.get("/products/")
def get_all_products():
    return db.query(Products).all()
    
#get data from the single id 
@app.get("/product/{id}")
def get_product_by_id(id:int):
    return db.query(Products).filter(Products.id==id).first()


#add the data
@app.post("/product/")
def add_proudct(product:Productschema):
    new_product=Products(
        id=product.id,
        name=product.name,
        desc=product.desc,
        price=product.price
    )
    db.add(new_product)
    db.commit()
    return "product added"

#update the data
@app.put("/product/{id}/") 
def update_data(id:int,updated_product:Productschema):
   product=db.query(Products).filter(Products.id==id).first()
   if product:
       product.name=updated_product.name
       product.desc=updated_product.desc
       product.price=updated_product.price
       db.commit()
       return "Product Updated"
   return "NO PRODUCT FOUND IT"       
 
#delete the data       
@app.delete("/product/{id}/")
def delete_prodcut(id:int):
    product=db.query(Products).filter(Products.id==id).first()
    if product:
        db.delete(product)
        db.commit()
        return "Product deleted "
    return "Product not found"



        
   
        
       

            
            
    
    

 

        
    
    
    