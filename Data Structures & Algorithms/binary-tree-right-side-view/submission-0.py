# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res =[]
        queue = deque([root,])
        while queue:
            #print(queue[-1].val)
            res.append(queue[-1].val)
            levelLen = len(queue)
            for i in range(levelLen):
                head = queue.popleft()
                if head.left:
                    queue.append(head.left)
                if head.right:
                    queue.append(head.right)
            
        return res
            




