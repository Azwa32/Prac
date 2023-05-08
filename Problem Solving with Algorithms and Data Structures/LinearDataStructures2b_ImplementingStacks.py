# Write a function rev_string(my_str) that uses a stack to reverse the characters in a string.


from pythonds3.basic import Stack

# initialise
def rev_string(my_str):
    stack = Stack()
    string_list = list(my_str)
    rev = ''

    # put characters into stack
    for char in range(len(string_list)):
        stack.push(string_list[char])

    # remove from stack into a string
    while not stack.size() == 0:
        rev += stack.pop()

    return rev

print(rev_string("apple"))

