from pymongo  import MongoClient
import os
from pymongo.database import Database
from dotenv import load_dotenv

load_dotenv()

uri=os.getenv("MONGO_URI")
db_name=os.getenv("DB_NAME")

def retrieve_db()-> Database|Exception:
    try:
        client=MongoClient(uri)
        db=client[db_name]
        return db
    except Exception as e:
        return e