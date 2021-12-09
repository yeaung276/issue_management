from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import mode
import models,schemas

from fastapi import HTTPException,status

def get_all_items(db:Session):
    return db.query(models.Item).all()

def get_item(db:Session,id:int):
    return db.query(models.Item).get(id)

def create_item(db:Session,item:dict):
    new_item = models.Item(**item)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

def update_item(db:Session,id:int,item:dict):
    reqitem = db.query(models.Item).get(id)
    if reqitem is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource not found!")
    for key,value in item.dict().items():
        setattr(reqitem,key,value)
    db.commit()
    db.refresh(item)
    return item

def delete_item(db:Session,id:int):
    item = db.query(models.Item).get(id)
    db.delete(item)
    db.commit()
    return {"detail": "Operation Succeed!"}
    