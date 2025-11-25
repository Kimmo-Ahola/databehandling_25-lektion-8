from sqlalchemy import DECIMAL, Boolean
from models.base import Base, int_pk, Mapped, str_255, mapped_column


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int_pk]
    product_name: Mapped[str_255]
    unit_price: Mapped[float] = mapped_column(DECIMAL(10, 2))
    discontinued: Mapped[bool] = mapped_column(Boolean, default=False)