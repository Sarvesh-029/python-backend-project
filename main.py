from fastapi import FastAPI  , Depends
from fastapi.middleware.cors import CORSMiddleware
from database import session , engine
from models import Product
import db_models
from sqlalchemy.orm import Session

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:3000"],
    allow_methods=["*"]
)

db_models.Base.metadata.create_all(bind = engine)

@app.get("/")
def sarvesh():
    return "yooo"

products = [
    Product(id=1,name='mobile',description='gaming',price='9999',quantity=9),
    Product(id=2,name='laptop',description='gaming',price='99999',quantity = 5),
    Product(id=5,name='laptop',description='ppt',price='19999' , quantity = 3)
]

def get_db():
    db = session()
    try :
        yield db 
    finally :
        db.close()
       

def init_db():
    db = session()
    count = db.query(db_models.Product).count()
    if count == 0 :
        for product in products :
            db.add(db_models.Product(**product.model_dump()))
        db.commit()

init_db()


@app.get("/products")                                                         #home page 
def product(db : Session = Depends(get_db)):
    db_products = db.query(db_models.Product).all()
    return db_products

@app.get("/products/{id}")                                                 #search product by id 
def product_id(id:int ,db : Session = Depends(get_db) ):
    db_product = db.query(db_models.Product).filter(db_models.Product.id == id).first()
    if db_product :
        return db_product
    return "product not found"

@app.post("/products")                                                            #add product
def add_product(product : Product , db : Session = Depends(get_db)) :
    db.add(db_models.Product(**product.model_dump()))
    db.commit()
    return products

@app.put("/products/{id}")                                                                #update product
def update_products(id : int , product : Product ,  db : Session = Depends(get_db)):
    db_product = db.query(db_models.Product).filter(db_models.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return "product updated succesfully"
    else:
        return "No product found"

@app.delete("/products/{id}")                                                            #delete product
def delete_product(id : int , db : Session = Depends(get_db)):
    db_product = db.query(db_models.Product).filter(db_models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "product deleted succesfully"
    else:
        return "product not found"