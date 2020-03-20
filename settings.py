import sqlalchemy as db
import sqlite3
from sqlalchemy import create_engine

# url = 'localhost:3306/test'
localdb = 'sqlite:////numbers.db'
# sqlite_db = create_engine('sqlite:////numbers.db', echo=True)
engine = create_engine("pymysql://scott:tiger@localhost/test")
metadata = db.MetaData(bind=create_engine())

print(engine)
