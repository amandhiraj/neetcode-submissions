# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        #check left and right of the current node
        # if left and right == p or q return parent

        # if p or q is node check left and right if q or p return root
        lca = [root]

        def getDescendant(root):
            if not root:
                return 
            
            lca[0] =  root

            if root.val == p.val or root.val == q.val:
                return
            elif root.val > p.val and root.val > q.val:
                getDescendant(root.left)
            elif root.val < p.val and root.val < q.val:
                getDescendant(root.right)
            else:
                return
            
        getDescendant(root)
        return lca[0]

