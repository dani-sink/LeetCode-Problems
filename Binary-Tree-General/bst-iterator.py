"""
Problem 173 from Top 150 Interview: Binary Search Tree Iterator

Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

    BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the 
    constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
    
    boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
    
    int next() Moves the pointer to the right, then returns the number at the pointer.

Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element 
in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal 
when next() is called.

 

Example 1:

Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False

 

Constraints:

    The number of nodes in the tree is in the range [1, 105].
    0 <= Node.val <= 106
    At most 105 calls will be made to hasNext, and next.

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        def get_array(root, arr):
            if not root:
                return

            get_array(root.left, arr)
            arr.append(root.val)
            get_array(root.right, arr)
            return arr

        self.__bst_array = get_array(root, []) # get the inorder traversal as an array
        self.__bst_array_len = len(self.__bst_array) # record the length of that array
        self.pointer = -1 # set the pointer to a negative value initially

    def next(self):
        """
        :rtype: int
        """
        self.pointer += 1 # move pointer to the next position
        return self.__bst_array[self.pointer] if self.pointer < self.__bst_array_len else -1 # get element where the pointer now points to

        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.pointer + 1 >= self.__bst_array_len: # check if the pointer is still within the array indices
            return False #
        else:
            return True