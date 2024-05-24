"""
Problem 106 from Top 150 Interview: Construct Binary Tree from Inorder and Postorder Traversal

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary 
tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

Example 1:

Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]

 

Constraints:

    . 1 <= inorder.length <= 3000
    
    . postorder.length == inorder.length
    
    . -3000 <= inorder[i], postorder[i] <= 3000
    
    . inorder and postorder consist of unique values.
    
    . Each value of postorder also appears in inorder.
    
    . inorder is guaranteed to be the inorder traversal of the tree.
    
    . postorder is guaranteed to be the postorder traversal of the tree.
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None

        start = TreeNode(postorder[-1]) # root is always the last element in post array so create root first
        mid = inorder.index(postorder[-1]) # get index of root in the inorder array
        
        
        # Recursively build the left subtree. In both the postorder and inorder arrays, all the elements before the mid 
        # index are part of the left subtree, so only take those elements.
        start.left = self.buildTree(inorder[:mid], postorder[:mid])
        
        # Recursively build the right subtree. In postorder, the right subtree starts at the mid index and ends just before
        # the last index since the last index is the root, which we always traverse last in postorder. In inorder,
        # all the elements after the mid index are in the right subtree, so only take those elements.
        start.right = self.buildTree(inorder[mid + 1:], postorder[mid:-1])
        
        return start # Now that we recursively built the left subtree and right subtree, we return the root.