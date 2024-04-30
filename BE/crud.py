from sqlalchemy import desc
from sqlalchemy.orm import Session
import models
import schemas


def get_orders(db: Session):
    return db.query(models.Order).order_by(desc(models.Order.created)).all()


def create_order(db: Session, order: schemas.OrderBase):
    db_order = models.Order(email=order.email)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def get_tags(db: Session):
    return db.query(models.Tag).all()


def create_tag(db: Session, tag: schemas.TagBase):
    db_tag = models.Tag(name=tag.name)
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag
