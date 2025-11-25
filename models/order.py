from datetime import date
from models.base import Base, Mapped, int_pk

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int_pk]
    order_date: Mapped[date]
    # TODO customer id on thursday