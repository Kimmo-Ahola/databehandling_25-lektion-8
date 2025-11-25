import random
from typing import List
from models.base import Base, Mapped, int_pk, str_255, String, mapped_column

class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int_pk]
    first_name: Mapped[str_255]
    last_name: Mapped[str_255]
    email: Mapped[str_255]
    address: Mapped[str_255]
    city: Mapped[str_255]
    postal_code: Mapped[str] = mapped_column(String(20))

    """
    Static method that creates 15 customers.
    """
    @staticmethod
    def create_customers() -> List["Customer"]:
        customers: List[Customer] = []
        first_names = ["Kalle", "Pelle", "Göran", 
                       "Stina", "Lisa", "Kerstin"]
        last_names = ["Andersson", "Svensson", "Johansson",
                      "Pettersson"]
        

        number_to_seed = 15

        for i in range(number_to_seed):
            cust = Customer(
                first_name=random.choice(first_names),
                last_name=random.choice(last_names),
                email=f"test{i}@test.se",
                address=f"storgatan {i}",
                city="Västerås",
                postal_code="700 00")

            customers.append(cust)

        return customers