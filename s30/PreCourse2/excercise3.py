# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    """
    Algorithm:

    Initialized the temp variable as head
    Initialized count to Zero
    Take loop till head will become Null(i.e end of the list) and increment
    the temp node when count is odd only, in this way temp will traverse
    till mid element and head will traverse all linked list.
    Print the data of temp.
    """

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Function to get the middle of
    # the linked list
    def printMiddle(self):
        temp = self.head
        count = 0

        while self.head:
            # Only update when count is odd

            if count & 1:
                temp = temp.next
            self.head = self.head.next

            count = count + 1

        print(temp.data)


# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()
