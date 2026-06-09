#create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#creating a node
node1 = Node(10)
print(node1.data) #10
print(node1.next) #None

#create a linked list
class LinkedList:
    def __init__(self):
        self.head = None

#creating a linked list
linked_list = LinkedList()
print(linked_list.head) #None
