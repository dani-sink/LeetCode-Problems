"""
Problem 129 from Top 150 Interview: Sum Root to Leaf Numbers

You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

    For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.

Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.


Example 1:

Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:

Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.

 

Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    0 <= Node.val <= 9
    The depth of the tree will not exceed 10.

"""


# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):

    # Helper function to compute all the root-to-leaf paths of the tree and store them in an array
    def paths(self, root, arr, path):
        if not root:
            return
        if not root.left and not root.right: # if at a leaf node
            path += str(root.val) # add leaf node to the current root-to-leaf path
            arr.append(path) # add the current root-to-leaf path to the array of root-to-leaf paths
            return arr # return the current state of the array of root-to-leaf paths
        
        # Otherwise
        path += str(root.val) # add current node to the root-to-leaf path
        self.paths(root.left, arr, path) # recursively explore the left subpath to find the rest of the path
        self.paths(root.right, arr, path) # recursively explore the right subpath to find the rest of the path
        return arr # When done, return the entire array of root-to-leaf paths
        

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        all_paths = self.paths(root, [], "") # get all root-to-leaf paths of the tree
        sum_all = sum([int(s) for s in all_paths]) # sum the integer each integer value yielded by each path with all other values
        return sum_all # return the total sum