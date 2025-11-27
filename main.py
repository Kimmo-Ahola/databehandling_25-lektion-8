# installera 
# pip install sqlalchemy 
# pip install pymysql 
# pip install alembic

from database.db import My_Session
from models.category import Category
from models.customer import Customer


with My_Session() as session:
    category_count = session.query(Category).count()

    if category_count == 0:
        category = Category(categoryname="Beverage", 
                            description="Drinks, soft drinks, hard spirits", 
                            picture="www.google.com")
        
        session.add(category)
        session.commit()

    customer_count = session.query(Customer).count()

    if customer_count == 0:
        customer = Customer(
            first_name="Kimmo", 
            last_name="Ahola",
            email="kimmo@mail.se",
            address="Storgatan 1",
            city="Uppsala",
            postal_code="757 55")
        
        session.add(customer)
        session.commit()

    