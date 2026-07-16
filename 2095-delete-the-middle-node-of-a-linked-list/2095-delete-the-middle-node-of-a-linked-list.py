# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count=0
        curr=head
        if head.next==None:
            return None
        while curr:
            curr=curr.next
            count+=1
        n=(count//2)
        l=head
        while n-1:
            l=l.next
            n-=1
        l.next=l.next.next
        return head
