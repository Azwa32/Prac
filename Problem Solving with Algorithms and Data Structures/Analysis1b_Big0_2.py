# constant time implementation

import time

def sum_of_n_3(n):
    # capture the start time
    start = time.time()
    # run alg and capture run time
    return (n * (n + 1)) / 2, time.time() - start

# create value list
values = [10000, 100000, 1000000, 10000000, 100000000]
# run each value in list through the function
for value in values:
    print("Sum is %d required %10.7f seconds" % sum_of_n_3(value))