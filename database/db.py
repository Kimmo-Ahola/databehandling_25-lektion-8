from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# connection string to MySQL

mysql_url = "mysql+pymysql://user:user123@localhost:3306/delete_me"
engine = create_engine(mysql_url)

My_Session = sessionmaker(engine)