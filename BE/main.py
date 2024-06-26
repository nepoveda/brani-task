from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.params import Depends
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

origins = ["http://localhost:3000", "http://localhost:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def orders_list(db: Session = Depends(get_db)):
    return crud.get_orders(db)


@app.post("/")
async def orders_create(order: schemas.OrderBase, db: Session = Depends(get_db)):
    return crud.create_order(db, order)


@app.get("/tags")
async def tags_list(db: Session = Depends(get_db)):
    return crud.get_tags(db)


@app.post("/tags")
async def tags_create(tag: schemas.TagBase, db: Session = Depends(get_db)):
    return crud.create_tag(db, tag)


@app.get("/to")
async def to(db: Session = Depends(get_db)):
    return crud.get_tag_order_associations(db)
