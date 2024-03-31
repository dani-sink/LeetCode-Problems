"""
Problem 19 from Top 150 Interview: Remove Nth Node From End of List


Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]

Constraints:

    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        cur = head 
        index = 1
        length = 0
        while cur is not None: # get length of the list first in the first pass
            cur = cur.next
            length += 1
        wanted_index = length - n + 1 # calculate index of element we want to remove
        dummy = ListNode('0', head) # dummy variable
        prev = dummy # previous node
        cur = head # current node
        index = 1 # reset index to 1
        while cur is not None: # make a second pass through the list
            if index == wanted_index: # if we are at the wanted index
                prev.next = cur.next # set previous pointer to point to the node the current node next pointer points to
                cur.next = None # remove the next pointer of the current node to delete it
                break # exit the loop
            else:
                prev = cur
                cur = cur.next
            index += 1
        return dummy.next # return the head
