from datetime import date

from sqlalchemy import ForeignKey
from models.base import Base, Mapped, int_pk, mapped_column

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int_pk]
    order_date: Mapped[date]
    
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"))