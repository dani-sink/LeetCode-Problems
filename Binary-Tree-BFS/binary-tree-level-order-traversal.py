"""
Problem 102 from Top 150 Interview: Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []

"""

# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    # Helper method to get the height of the tree
    def height(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        return 1 + max(self.height(root.left), self.height(root.right))


    # Helper method to reunite each element of a given level of a tree as an array
    def getCurrentLevelArray(self, root, level, arr):
        if root is None:
            return
        if level == 1:
            arr.append(root.val)
        elif level > 1:
            self.getCurrentLevelArray(root.left, level-1, arr)
            self.getCurrentLevelArray(root.right, level-1, arr)
        return arr

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        h = self.height(root) # get height of the tree
        all_levels = [] # where we will store all level arrays
        for i in range(1, h+1): # go through each level of the tree
            all_levels.append(self.getCurrentLevelArray(root, i, [])) # add each level array to the all_levels array

        return all_levels