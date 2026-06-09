# Given the head of a sorted linked list, delete all duplicates such that each element appears only once
# Return the linked list sorted as well.
class solution:
    def deleteDuplicates(self, head):
        if head is None:
            return head
        curr=head
        while curr.next!=None:
            if curr.val==curr.next.val:
                curr.next=curr.next.next
            else:
                curr=curr.next
        return head