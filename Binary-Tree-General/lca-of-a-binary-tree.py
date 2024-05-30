"""
Problem 236 from Top 150 Interview: Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1

 

Constraints:

    The number of nodes in the tree is in the range [2, 105].
    -109 <= Node.val <= 109
    All Node.val are unique.
    p != q
    p and q will exist in the tree.

"""

# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def lcaHelper(self, root, p, q):

        # if we reach a leaf node without finding either p or q, then the last saved root is the lca, so return root
        # if the root is either p or q, it will be the lca of both p and q by default, so return root
        if not root or root == p or root == q:
            return root
        
        # Otherwise
        left = self.lcaHelper(root.left, p, q) # recursively search the left subtree
        right = self.lcaHelper(root.right, p, q) # recursively search the right subtree
        if left and right: # if both left and right are not null, it means that p and q are in either the left subtree or the right subtree
            return root # so the current root must be the lca, hence return it.
        elif not left: # if neither p nor q was found in the left subtree, then they must either be in the right subtree or not exist at all in the tree.
            return right # either way, return the result of recursively going into the right subtree
        else: # in any other instances, we check the left subtree
            return left # we return the result of recursively going into the left subtree

            

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.lcaHelper(root, p, q)