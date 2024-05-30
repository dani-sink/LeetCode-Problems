"""
Problem 637 from Top 150 Interview: Average of Levels in Binary Tree

Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. 
Answers within 10-5 of the actual answer will be accepted.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].

Example 2:

Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]

 

Constraints:

    The number of nodes in the tree is in the range [1, 104].
    -231 <= Node.val <= 231 - 1

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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

    # Helper method to get the average
    def avg(self, arr):
        return float(sum(arr)) / float(len(arr))

    
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        h = self.height(root) # get height of the tree
        all_levels = [] # where we will store all level arrays
        for i in range(1, h+1): # go through each level of the tree
            all_levels.append(self.getCurrentLevelArray(root, i, [])) # add each level array to the all_levels array

        avg_of_all_levels = [self.avg(level) for level in all_levels] # store the average for each level in an array
        
        return avg_of_all_levels # return the array