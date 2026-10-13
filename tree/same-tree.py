# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        # If both nodes are None, the trees are identical so far
        if not p and not q:
            return True
        
        # If one of them is None or their values don't match, they are not the same
        if not p or not q or p.val != q.val:
            return False
        
        # Recursively check both the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        