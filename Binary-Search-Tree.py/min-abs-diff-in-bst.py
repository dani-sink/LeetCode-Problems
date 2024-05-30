"""
Problem 530 from Top 150 Interview: Minimum Absolute Difference in BST

Given the root of a Binary Search Tree (BST), return the minimum absolute difference between 
the values of any two different nodes in the tree. 

Example 1:

Input: root = [4,2,6,1,3]
Output: 1

Example 2:

Input: root = [1,0,48,null,null,12,49]
Output: 1

 

Constraints:

    The number of nodes in the tree is in the range [2, 104].
    0 <= Node.val <= 105

"""

# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):

    def inorderArray(self, root, arr):
        if not root:
            return
        
        self.inorderArray(root.left, arr)
        arr.append(root.val)
        self.inorderArray(root.right, arr)
        return arr

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        in_array = self.inorderArray(root, [])
        abs_differences = []
        for i in range(len(in_array) - 1):
            abs_differences.append(abs(in_array[i] - in_array[i+1]))
        return min(abs_differences)