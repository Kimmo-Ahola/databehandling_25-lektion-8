from sqlalchemy import DECIMAL
from models.base import Base, Mapped, mapped_column, int_pk

class OrderProducts(Base):
    __tablename__ = "orders_products"

    # TODO primary key
    id: Mapped[int_pk]
    unit_price: Mapped[float] = mapped_column(DECIMAL(10, 2))
    quantity: Mapped[int]
    discount: Mapped[float]