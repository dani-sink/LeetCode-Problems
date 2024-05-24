"""
Problem 150 from Top 150 Interview: Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a 
binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]

 

Constraints:

    . 1 <= preorder.length <= 3000
    
    . inorder.length == preorder.length
    
    . -3000 <= preorder[i], inorder[i] <= 3000
    
    . preorder and inorder consist of unique values.
    
    . Each value of inorder also appears in preorder.
    
    . preorder is guaranteed to be the preorder traversal of the tree.
    
    . inorder is guaranteed to be the inorder traversal of the tree.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        
        start = TreeNode(preorder[0]) # root is always first element in preorder array so create root first
        mid = inorder.index(preorder[0]) # get index of root in the inorder array
        
        
        # Recursively traverse the left subtree. In preorder, we skip the first element since it is the root and 
        # partition the preorder array up to the mid index, which corresponds to the end of the left subtree 
        # portion in preorder. In inorder, all the elements before the mid index are part of the left subtree, 
        # so only take those elements
        start.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        
        # Recursively traverse the right subtree. In preorder, all the elements after the element at the mid index
        # are in the right subtree, so only take those elements. In inorder, all the elements after the mid index
        # also correspond to the right subtree in inorder, so only take those elements
        start.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        
        return start # Now that we recursively built the left subtree and right subtree, we return the root.