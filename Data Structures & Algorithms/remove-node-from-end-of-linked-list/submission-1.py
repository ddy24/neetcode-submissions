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
        leftpointer.next = leftpointer.next.next# 已经跳出循环了，所以对list是直接修改
        return fakehead.next  #返回了修改后的list