from pythonds3.basic import Stack


def balance_checker(symbol_string):
    s = Stack()

    for symbol in symbol_string:
        # if symbol is (, [ or { then add to stack
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                return False
            # otherwise pop from stack
            else:
                # check if closed bracket has its match at the top of the stack
                if not matches(s.pop(), symbol):
                    return False

    # return boolean if stack is empty or not
    return s.is_empty()

# check that the index of the brackets is the same for opening and closing
def matches(sym_left, sym_right):
    all_lefts = "([{"
    all_rights = ")]}"
    return all_lefts.index(sym_left) == all_rights.index(sym_right)


print(balance_checker('{({([][])}())}'))
print(balance_checker('[{()]'))
print(balance_checker('{({([][)]}())}'))