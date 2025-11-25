# installera 
# pip install sqlalchemy 
# pip install pymysql 
# pip install alembic

from database.db import My_Session
from models.category import Category
from models.customer import Customer


"""
different query examples
This is the absolute basics on how to do CRUD:

use My_Session as session:
    session.add(object) # add to db
    session.delete(object) # delete from db

    session.commit() # save changes
"""
with My_Session() as session:
    pass

    ## We add a category the database. categoryname is unique, so we need to check for errors.
    ## try: except: or do a query to check if name exists

    # category = Category(categoryname="Beverage", 
    #                     description="Drinks, soft drinks, hard spirits", 
    #                     picture="www.google.com")
    
    # session.add(category)

    ## get all_users as List[Customer] withh .all()
    # all_users = session.query(Customer).all()
    ## loop through and delete users
    # for user in all_users:
    #     session.delete(user)
    # session.commit()

    ## SELECT COUNT(*) FROM CUSTOMERS -- We get the number of rows in our table
    # count = session.query(Customer).count()

    ## if table is empty: create customers
    # if count == 0:
    #     users = Customer.create_customers()

    #     # for user in users:
    #     #     session.add(user)

    #     session.add_all(users)

    #     session.commit()

    ## find all customers with first_name "Kalle", order by last_name descending
    # query = session.query(Customer)\
    #     .where(Customer.first_name == "Kalle")\
    #     .order_by(Customer.last_name.desc())\
    #     .all()


    ## Find the first row in the category table
    # query = session.query(Category)
    # result = query.first()

    ## .first() returns Category | None so we have to check for that
    # if result is not None:
    #     print(result.id)
    # else:
    #     print("No categories exist")
    # try:
    #     query = session.query(Category).one()
    #     print(query.id)
    # except:
    #     print("error here")

    # session.commit()
    

