# anagram detection, Checking off

def anagram_solution_1(s1, s2):
    # initialise the bool to be returned to true
    still_ok = True
    # check the string lengths are the same
    if len(s1) != len(s2):
        # if not set False
        still_ok = False

    # set a_list to a list of characters in the s2 arg, this will be the main list
    a_list = list(s2)
    # initialise pos_1 to 0
    pos_1 = 0

    # while pos_1 is not at the end of the list and hasn't detected a false character
    while pos_1 < len(s1) and still_ok:
        # initialise pos_2
        pos_2 = 0
        # initialise found to False
        found = False
        # nested loop to run while scan is not at the end and not found
        while pos_2 < len(a_list) and not found:
            # if arg 1 @ pos_1 is equal to the alist pos
            if s1[pos_1] == a_list[pos_2]:
                # set found to True
                found = True
            # otherwise iterate pos_2
            else:
                pos_2 = pos_2 + 1
        # if found modify location on a_list to none
        if found:
            a_list[pos_2] = None
        # otherwise set location to False
        else:
            still_ok = False
        # iterate to next location
        pos_1 = pos_1 + 1

    return still_ok


print(anagram_solution_1("apple", "pleap"))  # expected: True
print(anagram_solution_1("abcd", "dcba"))  # expected: True
print(anagram_solution_1("abcd", "dcda"))  # expected: False