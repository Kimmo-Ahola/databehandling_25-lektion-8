# installera 
# pip install sqlalchemy 
# pip install pymysql 
# pip install alembic

from datetime import datetime
from typing import List
from database.db import My_Session
from models.category import Category
from models.customer import Customer
from models.order import Order
from models.order_product import OrderProducts
from models.product import Product


with My_Session() as session:
    # category_count = session.query(Category).count()

    # if category_count == 0:
    #     category = Category(categoryname="Beverage", 
    #                         description="Drinks, soft drinks, hard spirits", 
    #                         picture="www.google.com")
        
    #     session.add(category)
    #     session.commit()

    # customer_count = session.query(Customer).count()

    # if customer_count == 0:
    #     customer = Customer(
    #         first_name="Kimmo", 
    #         last_name="Ahola",
    #         email="kimmo@mail.se",
    #         address="Storgatan 1",
    #         city="Uppsala",
    #         postal_code="757 55")
        
    #     session.add(customer)
    #     session.commit()

    # first_customer = session.query(Customer).first()

    # if first_customer:
    #     first_customer.first_name = "Lars"
    #     first_customer.soft_delete()
    #     session.commit()

    # first_customer = session.query(Customer)\
    #     .where(Customer.is_deleted == False)\
    #     .first()

    # product_count = session.query(Product).count()

    # if product_count == 0:
    #     beverage_category = session.query(Category).where(Category.categoryname == "Beverage").one()

    #     p_1 = Product(product_name="Coca-cola", unit_price=20.5, category_id = beverage_category.id)
    #     p_2 = Product(product_name="Fanta", unit_price=10.3, category_id = beverage_category.id)
    #     p_3 = Product(product_name="Kolsyrat vatten", unit_price=2, category_id = beverage_category.id)
    #     p_4 = Product(product_name="Julmust", unit_price=50.5, category_id = beverage_category.id)

    #     session.add_all([p_1, p_2, p_3, p_4])

    #     session.commit()

    # result = session.query(Product, Category).join(Category).all()

    # for product, category in result:
    #     print(product.id, product.product_name, category)

    my_customer = session.query(Customer).one()

    all_products = session.query(Product).all()

    # for product in all_products:
    #     order = Order(customer_id=my_customer.id, order_date=datetime.now())

    #     session.add(order)
    #     session.flush()

    #     order_product = OrderProducts(product_id=product.id,
    #                                   order_id=order.id,
    #                                   unit_price=product.unit_price,
    #                                   quantity=1,
    #                                   discount=0
    #                                   )
        
    #     session.add(order_product)
    #     session.commit()

    print("Tillgängliga produkter: ")

    for product in all_products:
        print("Id: ", product.id, "namn: ", product.product_name)

    customer_choice = input("Vilka produkter vill du ha, ange id med mellanslag: ")

    split = customer_choice.split()

    choices: List[int] = []
    for s in split:
        choices.append(int(s))

    for c in choices:
        product = session.get(Product, c)

        if product:
            # Add to orders and order products...
            pass
    
    