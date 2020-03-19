import numpy as np
import time
import sqlalchemy as sa
from sqlalchemy import Column, Integer

from settings import engine, metadata, Base, Session, connection

session = Session(autocommit=True, autoflush=True)


class Arr(Base):
    __tablename__ = "sort"
    id = Column(Integer, primary_key=True)
    numbers = Column(Integer())
    """
    def __init__(self, numbers):
        self.numbers = numbers
        """


"""    
def insert_db(arr):
    table = sa.Table('numbers',metadata,autoload=True,autoload_with=engine)
    try:
        num = Column('numbers',Integer)
        table.insert().values(arr)
    except Exception as e:
        raise NotImplementedError
        print(e)
"""

numbers = sa.Table('sort', metadata,
                   Column('Id', Integer()),
                   Column('numbers', Integer())

                   )
metadata.create_all(engine)
tic = time.perf_counter()
number = 10
arr = np.random.randint(1, 100, number)
print(f"This is the unsorted - {arr}")

sorted_array = np.sort(arr)
unique = np.unique(sorted_array)

print(f"sorted array - {sorted_array}")
for e in enumerate(unique, start=1):
    # print(e[0])
    # main_arr = Arr(id = e[0],numbers = e[1])
    insert = sa.insert(numbers).values(Id=e[0], numbers=int(e[1]))
    # result = connection.execute(insert)
    # session.commit()
    main_arr = Arr(numbers=int(e[1]))
    session.add(main_arr)

    print(main_arr.numbers)
    # session.commit()

session.add(main_arr)
# session.commit()


session.close()
toc = time.perf_counter()
# all = session.query(Arr).all()
print(f"This block of code took {toc - tic:0.4f} seconds")

print(engine)
