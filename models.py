
from sqlalchemy import Boolean,Column,ForeignKey,Integer,String
from sqlalchemy.orm import relationship


from database import Base

class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,index=True)
    email=Column(String,unique=True,index=True)
    hashed_password=Column(String)
    is_active =Column(Boolean,default=True)
    
    items =relationship('Item',back_populates='owner')
    
class Item(Base):
    __tablename__='items'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    issues =Column(String,index=True)
    sources =Column(String,index=True)
    department=Column(String,index=True)
    root_cause=Column(String,index=True)
    issue_type=Column(String,index=True)
    short_term_solution=Column(String,index=True)
    long_term_solution=Column(String,index=True)
    start_date=Column(String,index=True)
    close_date=Column(String,index=True)
    number_of_days=Column(Integer,index=True)
    priority=Column(String,index=True)
    remark=Column(String,index=True)
    
    status=Column(String,index=True)

    owner = relationship("User", back_populates='items')