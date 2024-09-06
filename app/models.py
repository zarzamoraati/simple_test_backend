from pydantic import BaseModel, Field, field_validator
from typing import Optional
from uuid import uuid4
from datetime import datetime
from fastapi import HTTPException

class Contact(BaseModel):
    id:Optional[str]=Field(default_factory=lambda :str(uuid4()))
    date:Optional[datetime]=Field(default_factory=lambda: datetime.today())
    name:str
    phone:str

    # @field_validator("name")
    # @classmethod
    # def valid_name(cls,name):
    
    #     if not isinstance(name,str) or name == "":
    #         raise HTTPException(status_code=401,detail="Field 'name' is invalid")
        