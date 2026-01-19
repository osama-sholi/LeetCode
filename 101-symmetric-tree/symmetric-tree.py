# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.result = True

    def is_symmetric(self, l, r):
        if not l and not r:
            return
        
        if l and r:
            if l.val != r.val:
                self.result = False
                return
    
            if not self.result:
                return
            
            self.is_symmetric(l.left, r.right)
            self.is_symmetric(l.right, r.left)
        else:
            self.result = False
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        self.is_symmetric(root, root)
        return self.result
            
