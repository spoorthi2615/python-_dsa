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

#insertion at begining in linked list
    def insert_at_begining(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

#inerstion at end in linked list
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

#traversal in linked list
    def traverse(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

#creating a linked list
linked_list = LinkedList()
print(linked_list.head) #None


