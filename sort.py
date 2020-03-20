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
                Column('time', DECIMAL()),
                #Column('created_on', DateTime(), default=datetime.now),
                autoload=True)

metadata.create_all()
tic = timeit.default_timer()
size = 15
random_list = np.random.randint(10, 1000, size)

print(random_list)

ordered_random_list = np.sort(random_list)

print(ordered_random_list)

toc = timeit.default_timer()

duration = round(toc - tic, 5)

ins = insert(runtime)

r = conn.execute(ins,
                 size_of_array=size,
                 time=duration,
                 created_on=datetime.now(),
                 )
print(r.inserted_primary_key)
print(f'The processes took {duration} seconds to complete')
