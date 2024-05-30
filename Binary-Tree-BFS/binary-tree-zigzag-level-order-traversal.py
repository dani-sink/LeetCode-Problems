"""
Problem 103 from Top 150 Interview: Binary Tree Zigzag Level Order Traversal

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
(i.e., from left to right, then right to left for the next level and alternate between).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []

 

Constraints:

    The number of nodes in the tree is in the range [0, 2000].
    -100 <= Node.val <= 100

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

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        h = self.height(root) # get height of the tree
        all_levels = [] # where we will store all level arrays
        for i in range(1, h+1): # go through each level of the tree
            all_levels.append(self.getCurrentLevelArray(root, i, [])) # add each level array to the all_levels array
        
        all_levels_zigzag = [] # where we will store the levels in zigzag
        for ind, level in enumerate(all_levels): # go through each level
            if ind % 2 == 0: # for each level with even index
                all_levels_zigzag.append(level) # put the level as it was originally
            else: # otherwise
                all_levels_zigzag.append(reversed(level)) # reverse the list and then add to the array
        return all_levels_zigzag # return the array