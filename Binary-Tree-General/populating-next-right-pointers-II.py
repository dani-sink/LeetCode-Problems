"""Problem 117 from Top 150 Interview: Populating Next Right Pointers in Each Node II

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 
Example 1:

Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its 
next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with 
'#' signifying the end of each level.

Example 2:

Input: root = []
Output: []

 

Constraints:

    The number of nodes in the tree is in the range [0, 6000].
    -100 <= Node.val <= 100

"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

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
            arr.append(root)
        elif level > 1:
            self.getCurrentLevelArray(root.left, level-1, arr)
            self.getCurrentLevelArray(root.right, level-1, arr)
        return arr

    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        h = self.height(root) # get height of the tree
        all_levels = [] # where we will store all level arrays
        for i in range(1, h+1): # go through each level of the tree
            all_levels.append(self.getCurrentLevelArray(root, i, [])) # add each level array to the all_levels array

        for level in all_levels: # for each level array
            for j in range(len(level) - 1): # up until before the last element
                level[j].next = level[j+1] # set the next pointer of the current node to the next node in the level
        return root # return the root