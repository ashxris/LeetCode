# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        # Check if the trees match starting from the current root node
        if self.sameTree(root, subRoot):
            return True
        
        # Otherwise, check the left and right subtrees of root
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def sameTree(self, s: TreeNode | None, t: TreeNode | None) -> bool:
        # If both are None, they match
        if not s and not t:
            return True
        # If one is None and the other isn't, or values don't match
        if s and t and s.val == t.val:
            return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
        
        return False