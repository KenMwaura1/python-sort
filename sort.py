import numpy as np
import timeit

from sqlalchemy import MetaData, Table, Column, DateTime, Boolean, Integer,DECIMAL
from datetime import datetime

from settings import engine, metadata
#metadata = MetaData()
numbers = Table('sort', metadata,
                Column('id', Integer(), primary_key=True),
                Column('numbers', Integer()),
                Column('created_on', DateTime(), default=datetime.now),
                )
runtime = Table('runtime', metadata,
                Column('id', Integer(), primary_key=True),
                Column('size_of_array', Integer()),
                Column('time', DECIMAL()))

metadata.create_all()
tic = timeit.default_timer()
size = 15
random_list = np.random.randint(10, 1000, size)

print(random_list)

ordered_random_list = np.sort(random_list)

print(ordered_random_list)

toc = timeit.default_timer()


print(f'The processes took {toc-tic} seconds to complete')
print(metadata)

