from sqlalchemy import DECIMAL, ForeignKey
from models.base import Base, Mapped, mapped_column, int_pk

class OrderProducts(Base):
    __tablename__ = "orders_products"

    unit_price: Mapped[float] = mapped_column(DECIMAL(10, 2))
    quantity: Mapped[int]
    discount: Mapped[float]

    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"), primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), primary_key=True)