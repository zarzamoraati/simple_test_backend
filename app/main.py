from fastapi import FastAPI, Depends
from pymongo.database import Database
from connection import retrieve_db
import crud
from models import Contact


app=FastAPI()

## TODO GET all 
@app.get("/contacts")
def get_contacts(db:Database=Depends(retrieve_db)):
    return crud.get_all_contacts(db)    

## TODO CREATE one

@app.post("/contacts")
def create_contact(contact:Contact,db:Database=Depends(retrieve_db)):
    return crud.create_contact(contact=contact,db=db)


