from pythonds3.basic import Stack


def par_checker(symbol_string):
    # initialise stack
    s = Stack()
    # iterate through string of ()()()
    for symbol in symbol_string:
        # if is opening then put symbol into stack
        if symbol == "(":
            s.push(symbol)
        else:
            if s.is_empty():
                return False
            # if != ( then remove from stack
            else:
                s.pop()

    # return boolean for if stack is empty
    return s.is_empty()


print(par_checker("((()))"))  # expected True
print(par_checker("((()()))"))  # expected True
print(par_checker("(()"))  # expected False
print(par_checker(")("))  # expected False