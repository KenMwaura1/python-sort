import numpy as np
import timeit

tic = timeit.default_timer()
size = 15
random_list = np.random.randint(10, 1000, size)

print(random_list)

ordered_random_list = np.sort(random_list)

print(ordered_random_list)

toc = timeit.default_timer()
print(f'The processes took {toc-tic} seconds to complete')

