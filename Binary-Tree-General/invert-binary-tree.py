"""
Problem 226 from Top 150 Interview: Invert Binary Tree

Given the root of a binary tree, invert the tree, and return its root.

Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:

Input: root = [2,1,3]
Output: [2,3,1]

Example 3:

Input: root = []
Output: []

 

Constraints:

    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
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