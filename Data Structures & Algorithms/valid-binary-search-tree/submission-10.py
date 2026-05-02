# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkTree(node, minn, maxx):
            if not node:
                return True
            
            if not (minn < node.val < maxx):
                return False


            return checkTree(node.left, minn, node.val) and checkTree(
                node.right, node.val, maxx)
        
        return checkTree(root, float("-inf"), float("inf"))

        