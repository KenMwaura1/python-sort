import sqlalchemy as db
from sqlalchemy import create_engine

localdb = 'sqlite:////numbers.db'
# sqlite_db = create_engine('sqlite:////numbers.db') # using absolute path
engine = create_engine("mysql+pymysql://root:@localhost/test", echo=True)
metadata = db.MetaData(engine.connect())
engine.connect()

print(metadata)
