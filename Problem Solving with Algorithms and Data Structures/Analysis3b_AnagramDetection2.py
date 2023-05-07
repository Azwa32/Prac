# anagram detection, Count and Compare
# this approach counts the number of times each letter occours in each string

# creates 2 lists the size of the alphabet
def anagram_solution_4(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    # update c1 & c2 arrays with the position of each 
    # alphabet letter showing the number of times it occours in the anagram

    # for each character in s1
    for i in range(len(s1)):
        # initialise pos to the characters ascii #
        pos = ord(s1[i]) - ord("a")
        # add 1 to the ascii location in the c1 array
        c1[pos] = c1[pos] + 1
        print(c1)

    # same as above for s2/c2
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord("a")
        c2[pos] = c2[pos] + 1

    # compare the c1 & c2 alphabet lists to one another, if any differences then False

    # initialise variables
    j = 0
    still_ok = True
    # iterate through the alphabet list and compare the two
    while j < 26 and still_ok:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            # set to false if the lists are different
            still_ok = False

    return still_ok


print(anagram_solution_4("apple", "pleap"))  # expected: True
print(anagram_solution_4("abcd", "dcba"))  # expected: True
print(anagram_solution_4("abcd", "dcda"))  # expected: False