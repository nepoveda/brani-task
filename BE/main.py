from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import crud
import models
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root(db: Session = Depends(get_db)):
    return crud.get_orders(db)


@app.get("/bla")
async def bla(db: Session = Depends(get_db)):
    return crud.create_order(db)
