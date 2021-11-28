from fastapi import FastAPI,Depends,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional,List, final
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import user
import crud,models,schemas
from database import SessionLocal,engine

models.Base.metadata.create_all(bind=engine)

app=FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/items")
def read_all_items(db:Session=Depends(get_db)):
    return crud.get_all_items(db)

@app.get("/items/{id}")
def read_item(id:int, db:Session=Depends(get_db)):
    return crud.get_item(db,id)

@app.post("/items")
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db,item=item.dict())

@app.put("/items/{id}")
def read_items(id:int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    items = crud.update_item(db,id, item=item)
    return items

@app.delete("/items")
def delete_user(id:int,db:Session=Depends(get_db)):
    crud.delete_item(db,id)

