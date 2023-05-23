class Node(object):
    def __init__ (self, d, n = None):
        self.data = d
        self.next_node = n

    def get_next (self): 
        return self.next_node
    
    def set_next (self, n):
        self.next_node = n

    def get_data (self): 
        return self.data
    
    def set_data (self, d):
        self.data = d

class LinkedList (object):
    def __init__ (self, r = None):
        self.root = r
        self.size = 0

    def get_size (self):
        return self.size
    
    def add (self, d):
        new_node = Node (d, self.root)
        self.root = new_node
        self.size += 1

    def remove (self, d):
        this_node = self.root
        prev_node = None

        # while we are not at the end of the list   
        while this_node is not None:
            #if we find the data we are looking for
            if this_node.get_data() == d:
                # if we are not in the root node
                if prev_node is not None:
                    # set the prev node next node to this nodes next node
                    prev_node.set_next(this_node.get_next())
                else:
                    # set the pointer to the node after the root
                    self.root = this_node.get_next()
                # decrement by one and return true
                self.size -= 1
                return True     # data removed
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False            # data not found
    
    def find (self, d):
        # 
        this_node = self.root
        # iterate through list to see if we can find the data
        while this_node is not Node:
            if this_node.get_data() == d:
                # if so return data 
                return d 
            elif this_node.get_next() == None:
                # if empty return false
                return False
            else:
                # if neither of the above happen continue to the next node
                this_node = this_node.get_next()

def main():
    myList = LinkedList()
    myList.add(5)
    myList.add(9)
    myList.add(3)
    myList.add(8)
    myList.add(9)
    print("size="+str(myList.get_size()))
    myList.remove(8)
    print("size="+str(myList.get_size()))
    print("Remove 15", myList.remove(15))
    print("size="+str(myList.get_size()))
    print("Find 25", myList.find(25))
    



