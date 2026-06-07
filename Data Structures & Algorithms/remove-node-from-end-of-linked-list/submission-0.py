# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        fakehead = ListNode(0,head)#指向head
        leftpointer = fakehead
        rightpointer = fakehead
        for i in range(n):
            rightpointer = rightpointer.next
        while rightpointer.next:
            leftpointer = leftpointer.next
            rightpointer = rightpointer.next
        leftpointer.next = leftpointer.next.next
        return fakehead.next