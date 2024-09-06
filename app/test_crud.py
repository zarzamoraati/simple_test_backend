import os
import pytest
from bson import ObjectId
from fastapi.testclient import TestClient
from pymongo import MongoClient
from main import app
from dotenv import load_dotenv

load_dotenv()

client=TestClient(app)

db_name=os.getenv("DB_NAME")
uri=os.getenv("MONGO_URI")

@pytest.fixture(scope="module")
def mongodb():
    # Setup: Define mongodb client

    mongo_client=MongoClient(uri)
    db=mongo_client[db_name]
    collection=db["selenium_collection"]
    
    # Override the global client 
    app.client = mongo_client
    app.db = db
    app.collection = collection

    ## Yield collection
    yield collection
    
    ## Teardown : Drop collection 
    mongo_client.drop_database(db_name)
    

def test_get_all(mongodb):
    # Insert one document
    mongodb.insert_one({"name":"John","phone":"100-20-08-10"})
    
    response= client.get("/contacts")
    assert response.status_code == 200
    contacts=response.json()
    assert isinstance(contacts,list)
    print(contacts)
    assert len(contacts) == 1
    assert isinstance(contacts[0],dict)
    assert "name" in contacts[0]
    assert "phone" in contacts[0]
    