import time

# function with argument of n
# Linear implemantation

def sum_of_n_2(n):
    # capture the current time at start
    start = time.time()

    # initialise the_sum to 0
    the_sum = 0

    # for every count + to the sum
    for i in range(1, n + 1):
        the_sum = the_sum + i

    # capture the current time at the end
    end = time.time()

    # return 'the_sum' and the time it took to run
    return the_sum, end - start

# run function 5 times and show results
for i in range(5):
    print("Sum is %d required %10.7f seconds" % sum_of_n_2(100000))


