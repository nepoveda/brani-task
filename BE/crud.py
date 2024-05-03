from sqlalchemy import desc, func
from sqlalchemy.orm import Session, joinedload
import models
import schemas


def get_orders(db: Session):
    return (
        db.query(models.Order)
        .options(joinedload(models.Order.tags))
        .order_by(desc(models.Order.created))
        .all()
    )


def create_order(db: Session, order: schemas.OrderBase):
    db_order = models.Order(email=order.email)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def get_tags(db: Session):
    return db.query(models.Tag).options(joinedload(models.Tag.orders)).all()


def create_tag(db: Session, tag: schemas.TagBase):
    db_tag = models.Tag(name=tag.name)
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag


def get_tag_order_associations(db: Session):
    return db.query(models.tag_order_association).all()
