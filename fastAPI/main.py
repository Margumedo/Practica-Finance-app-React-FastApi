from fastapi import FastAPI, HTTPException, Depends
from database import Base, engine, get_db
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from models import Transaction
from typing import List
from schemas import TransactionBase, TransactionShow, TransationUpdate

app = FastAPI(docs_url="/")

origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['GET','DELETE','POST','PUT'],
    allow_headers = ['*']
)

Base.metadata.create_all(bind=engine)

@app.get("/hello")
async def hello():
    return {"Message":"Welcome to your fucking fastAPI working"}

@app.get("/transactions", response_model=List[TransactionShow], status_code=200)
async def get_transactions(db: Session = Depends(get_db), skip: int=0, limit: int=100):
    transactions = db.query(Transaction).offset(skip).limit(limit).all()
    return transactions

@app.post("/transaction", response_model=TransactionShow, status_code=201)
async def create_transaction(transaction: TransactionBase, db: Session = Depends(get_db)):
    new_transaction = Transaction(**transaction.model_dump())

    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return new_transaction

@app.patch("/transaction{transaction_id}", response_model=TransactionShow, status_code=202)
async def update_transaction(transaction_id: int, payload: TransationUpdate, db: Session = Depends(get_db)):
    db_transaction = db.query(Transaction).filter(Transaction.id == transaction_id)
    result = db_transaction.first()
    if not result:
        raise HTTPException(status_code=404, detail="transaction not found")
    
    db_transaction.update(payload.model_dump(exclude_unset=True))
    db.commit()
    db.refresh(result)
    return result

@app.put("/transaction{transaction_id}", response_model=TransactionShow, status_code=202)
async def update_transaction(transaction_id: int, payload: TransationUpdate, db: Session = Depends(get_db)):
    db_transaction = db.query(Transaction).filter(Transaction.id == transaction_id)
    result = db_transaction.first()
    if not result:
        raise HTTPException(status_code=404, detail="transaction not found")
    
    db_transaction.update(payload.model_dump())
    db.commit()
    db.refresh(result)
    return result

@app.delete("/transaction{transaction_id}", status_code=204)
async def delete_transaction(transaction_id: int, db: Session = Depends(get_db)):
    db_transaction = db.query(Transaction).filter_by(id = transaction_id).first()
    if not db_transaction:
        raise HTTPException(status_code=404, detail="Transaction Not Found")
    
    db.delete(db_transaction)
    db.commit()
    return None