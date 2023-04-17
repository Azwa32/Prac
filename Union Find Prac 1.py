"""
Imagine you have a group of 10 friends, and you want to keep track of who is friends with whom. You can represent this group as a list of 10 elements, where each element represents a person, and each person is initially not connected to anyone else.
Now, let's say that two of your friends, let's call them Alice and Bob, become friends. To represent this in your list, you can "connect" them by setting their respective elements in the list to have the same "root" element. For example, you could set Alice's element to be the root, and then set Bob's element to also have the root element.
The Union-Find algorithm helps you keep track of these connections efficiently, so you can quickly determine whether two elements are connected or not.
Your task is to write a Python function called is_connected(p1: int, p2: int, connections: List[List[int]]) -> bool, which takes two integer values p1 and p2 (representing two people in your group), and a list of connections connections, where each element of connections is a list of two integers representing a pair of friends who are already connected.
The function should return True if p1 and p2 are connected (either directly or indirectly), and False otherwise.
"""

# Create the disjoint dataset (Union Find)
# create a node for each item set to itself as the parent



# create person nodes
class Node:
    def __init__(self, person):
        self.person = person  # the person whos node this is
        self.parent = self  # initialising this node as its own parent to start with
        self.rank = 0   # initialise the level of this node to 0

    def find(self):
        # set the parent of each node as the nodes are being created
        # the leader is someone who is its own parent
        if self.parent != self:

            

def is_connected(p1: int, p2: int, connections: List[List[int]]):

    #create list of person nodes in connections
    people = {}
    # go through connections, create a node for each person, add each node to the list
    for connection in connections:
        for person in connection:
            if person not in people:
                people.append(Node(person))



    

    

    


connections = [[0, 1], [1, 2], [2, 3], [4, 5], [5, 6], [7, 8]]
is_connected(0, 3, connections)
is_connected(0, 7, connections)
