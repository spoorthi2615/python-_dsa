#Given the head of a singly linked list, reverse the list, and return the reversed list.
class solution:
    def reverseList(self, head):
        prev=None
        curr=head
        while curr!=None:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        return prev