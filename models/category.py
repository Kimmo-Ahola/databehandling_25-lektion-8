from models.base import Base, mapped_column, Mapped, int_pk
from sqlalchemy import Integer, String, Text

class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int_pk] 
    categoryname: Mapped[str] = mapped_column(String(50), unique=True)
    description: Mapped[str] = mapped_column(Text)
    picture: Mapped[str] = mapped_column(String(1500))

    def __repr__(self) -> str:
        return f"{self.id}, {self.categoryname}, {self.description}, {self.picture}"