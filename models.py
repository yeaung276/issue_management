
from sqlalchemy import Column,Integer,String
from sqlalchemy.sql.sqltypes import DateTime

from database import Base
class Item(Base):
    __tablename__='items'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    issues =Column(String,)
    sources =Column(String)
    department=Column(String)
    root_cause=Column(String)
    issue_type=Column(String)
    short_term_solution=Column(String)
    long_term_solution=Column(String)
    start_date=Column(DateTime)
    close_date=Column(DateTime)
    number_of_days=Column(Integer)
    priority=Column(String)
    remark=Column(String)
    status=Column(String)