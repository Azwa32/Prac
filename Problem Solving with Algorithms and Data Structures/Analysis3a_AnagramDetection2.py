# anagram detection, Sort and compare

# At first glance you may be tempted to think that this algorithm is O(n), 
# since there is one simple iteration to compare the n characters after the sorting process. 
# However, the two calls to the Python sort method are not without their own cost. As we will see in Chapter 5, 
# sorting is typically either O(n2) or O(n log n), so the sorting operations dominate the iteration. 
# In the end, this algorithm will have the same order of magnitude as that of the sorting process.


def anagram_solution_2(s1, s2):
    # initialise both words to a list each
    a_list_1 = list(s1)
    a_list_2 = list(s2)

    # sort each list in ascending order. If the words are anagrams they should be a match at this point
    a_list_1.sort()  # adds a time complexity cost
    a_list_2.sort()  # adds a time complexity cost

    # initialist start search position and matches
    pos = 0
    matches = True

    # run while position is less than the length of the s1 string and meets these cond.
    while pos < len(s1) and matches:
        # if the position in the 2 lists matches then iterate the position, otherwise set to False
        if a_list_1[pos] == a_list_2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches


print(anagram_solution_2("apple", "pleap"))  # expected: True
print(anagram_solution_2("abcd", "dcba"))  # expected: True
print(anagram_solution_2("abcd", "dcda"))  # expected: False