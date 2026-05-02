# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = [0]  # Keep track of the count of good nodes
        
        def checkGoodNodes(root, maxValue):
            if not root:
                return
            
            # Check if the current node is a good node
            if root.val >= maxValue:
                good_nodes[0] += 1
            
            # Update the maximum value for the current path
            newMaxValue = max(maxValue, root.val)
            
            # Recurse for left and right children
            checkGoodNodes(root.left, newMaxValue)
            checkGoodNodes(root.right, newMaxValue)
        
        # Start the recursion with the root and its value as the initial max value
        checkGoodNodes(root, root.val)
        return good_nodes[0]
