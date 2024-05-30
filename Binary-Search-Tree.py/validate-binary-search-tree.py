"""
Problem 98 from Top 150 Interview: Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

    The left
    subtree
    of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

 

Example 1:

Input: root = [2,1,3]
Output: true

Example 2:

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

 

Constraints:

    The number of nodes in the tree is in the range [1, 104].
    -231 <= Node.val <= 231 - 1

"""

# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    
    def inorderArray(self, root, arr):
        if not root:
            return
        
        self.inorderArray(root.left, arr)
        arr.append(root.val)
        self.inorderArray(root.right, arr)
        return arr

    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        inorder_arr = self.inorderArray(root, []) # get the inorder traversal of the bst as an array
        sorted_inorder_arr = sorted(inorder_arr) # sort the array
        for i in range(len(inorder_arr)):
            if inorder_arr[i] != sorted_inorder_arr[i]: # check if the elements of the original array were sorted
                return False # if not, then return False


        # According to the definition provided, no nodes can be equal to each other in the BST, so we must remove duplicates
        
        filtered_list = list(set(inorder_arr)) # create a new array without duplicates

        return len(filtered_list) == len(inorder_arr) # if the length is the same, then the tree is a valid BST, so return true, otherwise return false