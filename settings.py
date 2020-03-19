from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy as db

# create sqlalchemy engine
engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="",
                               db="test"))

metadata = MetaData(bind=engine, info=[engine])
connection = engine.connect()
Session = sessionmaker(bind=engine)

emp = db.Table('emp', metadata,
               db.Column('Id', db.Integer()),
               db.Column('name', db.String(255), nullable=False),
               db.Column('salary', db.Float(), default=100.0),
               db.Column('active', db.Boolean(), default=True)
               )
# Inserting record one by one
query = db.insert(emp).values(Id=1, name='naveen', salary=60000.00, active=True)
ResultProxy = connection.execute(query)

metadata.create_all(engine)  # Creates the table

Base = declarative_base()
metadata.create_all(engine)

print(metadata)
