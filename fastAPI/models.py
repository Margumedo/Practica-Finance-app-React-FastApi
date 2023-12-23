from sqlalchemy import Column, Integer, Float, String, Boolean, DateTime
from database import Base
from datetime import datetime

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    amount = Column(Float)
    category = Column(String)
    description = Column(String)
    is_income = Column(Boolean, default=False)
    date = Column(DateTime, default=datetime.now)