"""
Problem 114 from Top 150 Interview: Flatten Binary Tree to Linked List

Given the root of a binary tree, flatten the tree into a "linked list":

    . The "linked list" should use the same TreeNode class where the right child pointer 
    points to the next node in the list and the left child pointer is always null.
    
    . The "linked list" should be in the same order as a pre-order traversal of the binary tree.

 

Example 1:

Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [0]
Output: [0]

 

Constraints:

    The number of nodes in the tree is in the range [0, 2000].
    -100 <= Node.val <= 100

"""

# Definition for a binary tree node.

# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):

    # Helper function to get the tree as a preorder array
    def preorderArr(self, root, arr):
        if not root:
            return
        arr.append(root)
        self.preorderArr(root.left, arr)
        self.preorderArr(root.right, arr)
        return arr
        
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        preorder_arr = self.preorderArr(root, []) # get the preorder array representation of the tree
        cur_node = root # start at the root
        for i in range(len(preorder_arr[1:])): # since root is already added, we don't need to add it again
            if cur_node.left is not None: # If there is a left child at the current node
                cur_node.left = None # remove it
            cur_node.right = preorder_arr[1:][i] # the right child of the current node is the next node in the preorder traversal of the tree.
            cur_node = cur_node.right # move to the right child for the next iteration