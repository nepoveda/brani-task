import uuid

from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType, EmailType, Timestamp

from database import Base, engine

tag_order_association = Table(
    "tag_order_association",
    Base.metadata,
    Column("order_id", UUIDType, ForeignKey("orders.id")),
    Column("tag_id", UUIDType, ForeignKey("tags.id")),
)


class Order(Base, Timestamp):
    __tablename__ = "orders"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    email = Column(EmailType(), nullable=False)
    tags = relationship(
        "Tag",
        secondary=tag_order_association,
        back_populates="orders",
    )


class Tag(Base):
    __tablename__ = "tags"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    orders = relationship(
        "Order", secondary=tag_order_association, back_populates="tags"
    )


Base.metadata.create_all(engine)
