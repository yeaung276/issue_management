from datetime import datetime
from typing import List,Optional
from pydantic import BaseModel

class ItemBase(BaseModel):
    title:str
    description:Optional[str]=None
    issues:str
    sources:str
    department:str
    root_cause:str
    issue_type:str
    short_term_solution:Optional[str]=None
    long_term_solution:Optional[str]=None
    start_date:datetime
    close_date:Optional[datetime] = None
    number_of_days:Optional[int]=None
    priority:Optional[str]=None
    status:str
   
    

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id:int
    owner_id:int
    
    class Config:
        orm_mode=True
        
class UserBase(BaseModel):
    email:str

class UserCreate(UserBase):
    password:str

class User(UserBase):
    id:int
    is_active:bool
    items:List[Item] = []
    
    class Config:
        orm_mode =True