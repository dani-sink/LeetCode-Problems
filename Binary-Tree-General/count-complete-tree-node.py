"""
Problem 222 from Top 150 Interview:  Count Complete Tree Nodes

Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a 
complete binary tree, and all nodes in the last level are as far left as possible. It can 
have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.


Example 1:

Input: root = [1,2,3,4,5,6]
Output: 6

Example 2:

Input: root = []
Output: 0

Example 3:

Input: root = [1]
Output: 1

Constraints:

    The number of nodes in the tree is in the range [0, 5 * 104].
    0 <= Node.val <= 5 * 104
    The tree is guaranteed to be complete.

"""

class Solution(object):

    def helperCounter(self, root, count):
        if not root:
            return 0
        
        # Recursively count the number of nodes in the left and right subtrees of the tree
        return 1 + self.helperCounter(root.left, count) + self.helperCounter(root.right, count)

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        return self.helperCounter(root, 0)