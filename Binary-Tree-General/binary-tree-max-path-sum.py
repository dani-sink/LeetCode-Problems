"""
Problem 124 from Top 150 Interview: Binary Tree Maximum Path Sum

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes 
in the sequence has an edge connecting them. A node can only appear in the sequence 
at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

Example 1:

Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:

Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

 

Constraints:

    The number of nodes in the tree is in the range [1, 3 * 104].
    -1000 <= Node.val <= 1000

"""

class Solution(object):

    # Depth-first search to find bot the max path with split allowed and without split allowed
    def dfs(self, root):
        if not root:
            return 0, float('-inf')
        
        leftMax, wsl = self.dfs(root.left) # compute the max path w/ and w/out split for the left subtree
        rightMax, wsr = self.dfs(root.right) # compute the max path w/ and w/out split for the right subtree

        # adding a node or subpath of nodes to the path should not decrease the current max path. So only add
        # when the subpath yields a positive value. Do this for both subtrees
        leftMax = max(leftMax, 0) #
        rightMax = max(rightMax, 0)

        # we compute the maximum of the left subtree max path, the right subtree max path and the current 
        # max path with split allowed
        res = max(wsl, wsr, root.val + leftMax + rightMax)

        # we return both the max path with split and the max path without split 
        return root.val + max(leftMax, rightMax), res

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        without_split, with_split = self.dfs(root)
        return max(without_split, with_split)
        