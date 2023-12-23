from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TransactionBase(BaseModel):
    amount: float
    category: str
    description: str
    is_income: bool

class TransactionShow(TransactionBase):
    id: int
    date: datetime

    class Config:
        orm_mode = True

class TransationUpdate(BaseModel):
    amount: Optional[float] = None
    category: Optional[str] = None
    description: Optional[str] = None
    is_income: Optional[bool] = None