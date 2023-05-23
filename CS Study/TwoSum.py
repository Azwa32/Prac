# Two Sum: Given an array of integers and a target value, 
# return indices of the two numbers such that they add up to the target.

nums = [2,4,5,6,8]
target = 14

hashmap = {}

# loop through nums, check if compliment is in hashmap, if so return key, if not add to hashmap
for number in range(len(nums)):
    compliment = target - nums[number]
    if compliment in hashmap:
        print(number, hashmap[compliment])
    else:
        hashmap[nums[number]] = number