import numpy as np
import timeit

from sqlalchemy import MetaData, Table, Column, DateTime, Boolean, Integer, DECIMAL, insert
from datetime import datetime

from settings import engine, metadata

# metadata = MetaData()

conn = engine.connect()

numbers = Table('sort', metadata,
                Column('id', Integer(), primary_key=True),
                Column('numbers', Integer()),
                Column('created_on', DateTime(), default=datetime.now),
                autoload=True)
runtime = Table('runtime', metadata,
                Column('id', Integer(), primary_key=True),
                Column('size_of_array', Integer()),
                Column('time', DECIMAL(precision=10, scale=5)),
                Column('created_on', DateTime(), default=datetime.now),
                autoload=True)
metadata.drop_all(bind=conn, checkfirst=True)

metadata.create_all(conn)
tic = timeit.default_timer()
size = 15
random_list = np.random.randint(10, 1000, size)

print(random_list)

ordered_random_list = np.sort(random_list)

print(ordered_random_list)

toc = timeit.default_timer()

duration = round(toc - tic, 5)

runtime_ins = insert(runtime)
numbers_ins = insert(numbers)

r = conn.execute(runtime_ins,
                 size_of_array=size,
                 time=duration,
                 created_on=datetime.now(),
                 )
print(r.inserted_primary_key)

for x in ordered_random_list:
    r1 = conn.execute(numbers_ins,
                      numbers=int(x),
                      )
print(f'The processes took {duration} seconds to complete')
