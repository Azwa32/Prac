import time
from random import randrange

def findMin(alist):
    # initialise the minimum value to the first element in the list
    overallmin = alist[0]
    # iterate through each element of the list
    for i in alist:
        # assume that the current element is the smallest
        issmallest =True

        # compare the current element with every other element
        for j in alist:
            # if therew is an element smaller than the current element
            if i > j:
                # set issmallest to False
                issmallest = False
        
        # If issmallest is still true after comparing with every other element,
        # update the overallmin variable to the current element
        if issmallest:
            overallmin = i
    # return the overall min element
    return overallmin

### uncomment to run logarithmic algorithim
'''
def findMin(alist):
    minsofar = alist[0]
    for i in alist:
        if i < minsofar:
            minsofar = i
    return minsofar

print(findMin([5,4,3,2,1,0]))
print(findMin([0,4,1,3,2,5]))
'''

# iterate through a range of between 1000 to 10001 at 1000 intervals eg: 1000 2000 3000 4000 etc
for listSize in range(1000, 10001, 1000):
    # using list comprehension
    # randrange() creates a random int between 0 & 100000
    # range() creates a consecutive list of ints the length of the argument (min 10000 ints in this case)
    # 'alist' creates an array of randrange() applied a range() number of times
    alist = [randrange(100000) for x in range(listSize)]
    # record the start time of the function call
    start = time.time()
    # call the findMin function on the list and print the result
    print(findMin(alist))
    # record the end time of the function
    end = time.time()
    # print the time taken
    print("size: %d time: %f" % (listSize, end-start))