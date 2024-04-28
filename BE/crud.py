from sqlalchemy.orm import Session
from sqlalchemy_utils.types import uuid
import models


def get_order(db: Session, order_id: uuid):
    return db.query(models.Order).get(models.Order.id == order_id)


def get_orders(db: Session):
    return db.query(models.Order).all()


def create_order(db: Session):
    order = models.Order(email="bla@co.bla")
    db.add(order)
    db.commit()
    db.refresh(order)
    return order
