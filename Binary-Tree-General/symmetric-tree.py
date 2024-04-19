"""
Problem 101 from Top 150 Interview:  Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:

Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:

Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    -100 <= Node.val <= 100

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution(object):
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        if root.left is None and root.right is None:
            return True

        if root.left is None or root.right is None:
            return False
        

        leftSubtree = root.left
        rightSubtree = self.invertTree(root.right)
        if self.isSameTree(leftSubtree, rightSubtree):
            return True
        else:
            return False
            
    
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return

        if root.left is None:
            if root.right is None:
                return root
            else:
                root.left = root.right
                root.right = None
                self.invertTree(root.left)
                return root

        if root.right is None:
            root.right = root.left
            root.left = None
            self.invertTree(root.right)
            return root

        temp = root.right
        root.right = root.left
        root.left = temp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None:
            if q is not None:
                return False
            return True

        if q is None:
            if p is not None:
                return False
            return True

        if q.val != p.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)