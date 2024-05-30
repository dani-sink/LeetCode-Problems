"""
Problem 199 from Top 150 Interview: Binary Tree Right Side View

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of 
the nodes you can see ordered from top to bottom.

 
Example 1:

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:

Input: root = [1,null,3]
Output: [1,3]

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


    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        h = self.height(root) # get height of the tree
        all_levels = [] # where we will store all level arrays
        for i in range(1, h+1): # go through each level of the tree
            all_levels.append(self.getCurrentLevelArray(root, i, [])) # add each level array to the all_levels array
        
        last_level_node_values = [level[-1] for level in all_levels] # for each level, get the last node of the array, which corresponds to the right most node in the level, and store it in an array
        return last_level_node_values # return the array

