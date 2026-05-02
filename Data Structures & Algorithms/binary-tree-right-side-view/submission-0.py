# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        que = deque([root])
        output = []

        while que:
            rightSide = None
            for _ in range(len(que)):
                node = que.popleft()
                if node:
                    rightSide = node
                    que.append(node.left)
                    que.append(node.right)
            if rightSide:
                output.append(rightSide.val)
        return output
