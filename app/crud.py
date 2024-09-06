from connection import retrieve_db
from models import Contact
from pymongo.database import Database
from fastapi import HTTPException
from fastapi import Depends

def get_all_contacts(db:Database):
    try:
        collection=db["selenium_collection"]
        contacts=list(collection.find({}))
        if len(contacts)==0:
            return []
        contacts_norm=[]
        for contact in contacts:
            contact["_id"]=str(contact["_id"])
            contacts_norm.append(contact)
        return contacts_norm
    except Exception as e:
        return {"error:":e}     

def create_contact(contact:Contact, db:Database):
    try:
        dic_contact=contact.model_dump()
        collection=db["selenium_collection"]
        response=collection.insert_one(dic_contact)
        if not response.inserted_id:
            raise HTTPException(status_code=503,detail="There was a problem writingc the contact")
        return {"id":str(response.inserted_id)}
     
    except Exception as e:
        return e
    
    
       