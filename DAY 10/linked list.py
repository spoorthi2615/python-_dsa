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

#create delete from begining in linked list
def delete_from_begining(self):
    if self.head is None:
        return
    self.head = self.head.next

#create delete from end in linked list
def delete_from_end(self):
    if self.head is None:
        return
    if self.head.next is None:
        self.head = None
        return
    second_last = self.head
    while second_last.next.next:
        second_last = second_last.next
    second_last.next = None

#sum of all the nodes in the linked list
def sum_of_nodes(self):
    current = self.head
    total_sum = 0
    while current:
        total_sum += current.data
        current = current.next
    return total_sum







