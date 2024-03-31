"""
Problem 61 from Top 150 Interview: Rotate List

Given the head of a linked list, rotate the list to the right by k places.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:

Input: head = [0,1,2], k = 4
Output: [2,0,1]

 

Constraints:

    The number of nodes in the list is in the range [0, 500].
    -100 <= Node.val <= 100
    0 <= k <= 2 * 109

"""

# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None: # # edge case where head is empty
            return None
        length = 1
        cur_ptr = head 
        while cur_ptr.next is not None: # iterate until reaching the tail
            length += 1 
            cur_ptr = cur_ptr.next
        if length == 1: # edge case where list has just 1 element
            return head
        rotate_shift = k % length # how much we need to rotate the list
        if rotate_shift == 0: # if 0, then no rotations needed
            return head
        # otherwise
        cur_ptr.next = head # make tail point to the head of the list to make it circular
        prev = None # pointer to keep track of previous node, initally set to None
        rotate_shift = length - k % length + 1 # how much we need to rotate the list, we rotate right from the left
        for i in range(rotate_shift):
            prev = cur_ptr # move previous pointer
            cur_ptr = cur_ptr.next # move current pointer

        # to end to rotation process
        prev.next = None  # set previous pointer to None to turn the circular list back to a normal list
        return cur_ptr # return current pointer