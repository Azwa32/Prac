# Dictionaries

# the below program runs a comparison of acessing data from a list vs accessing data through a Dict
# as you can see the list access is O(n) or linear however the Dict access is O(1) constant

import timeit
import random

print(f"{'n':10s}{'list':>10s}{'dict':>10s}")
for i in range(10_000, 1_000_001, 20_000):
    t = timeit.Timer(f"random.randrange({i}) in x",
    "from __main__ import random, x")
    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j: None for j in range(i)}
    dict_time = t.timeit(number=1000)
    print(f"{i:<10,}{lst_time:>10.3f}{dict_time:>10.3f}")