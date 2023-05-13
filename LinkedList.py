class Node:
    """
    Every single Node has a value ( that can be every type of data) and a next value, that refers to the following Node in the list.
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class List:
    """
    Methods that can be used in Linked Lists
    """
    def __init__(self, head:Node = None):
        self.head = head
    
    def append(self, data):
        """
        Function to add a node at the front of a list

        :data: any data type to add to the Node's value section 
        """
        new_node = Node(data) # creates a new node, with the data given
        new_node.next = self.head 
        self.head = new_node # reassigns the head

    def append_list(self, list:list):
        """
        Function to add a complete list to a Linked List

        :list: list of data (it can any data type and also different between themselves)
        """
        for element in list:
            self.append(element)

    def print_list(self):
        """
        Funtion to print the whole Linked List
        """
        current = self.head
        while current != None: # loops to the last node
            print(current.value, end = " -> ")
            current = current.next
        print("NULL")

    def create_cycle(self, index: int):
        """
        Function to create a cycle in the Linked List. It links the last node to the one passed by argument, creating a loop

        :index: index of the element that the last node will point to
        """
        current = self.head
        counter = 0
        while counter < index: # moves the pointer "counter" to the node to be pointed to
            current = current.next
            counter += 1
        last = self.head
        while last.next: # moves the pointer "last" to the last node
            last = last.next
        last.next = current #assigns as next of the last node, the node that closes the cycle