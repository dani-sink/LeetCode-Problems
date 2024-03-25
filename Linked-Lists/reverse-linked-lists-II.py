"""
Problem 92 from Top 150 Interview: Reverse Linked List II

Given the head of a singly linked list and two integers left and right where left <= right, 
reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:

    The number of nodes in the list is n.
    1 <= n <= 500
    -500 <= Node.val <= 500
    1 <= left <= right <= n

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head) # create a dummy node, setting its next pointer to the head
        prev = dummy # set previous pointer to this dummy
        cur = head # set current pointer to the head of the list
        count = 1 # to keep track of where we are in the list
        while count < left: # while we haven't reached the left node yet
            prev = cur # move previous pointer
            cur = cur.next # move current pointer
            count += 1
        
        # we now reached the left node
        left_prev = prev # save its previous node. This node represents the end of the left side
        init_left_next = left_prev.next # save its next node. This node will represent the beginning of the right side
        prev = None # reset prev to None for the reversal
        while count < right + 1: # while we haven't reached beyond the right node yet
            next_node = cur.next # temporarily save the next node of current node
            cur.next = prev # set the next pointer of the current node to point to the previous node
            prev = cur # move previous pointer
            cur = next_node # move current pointer by setting it to the next node
            count += 1
        
        # at this point we reversed the part we need, but it is disconnected from its previous side and next side, so
        # we need to reconnect them

        left_prev.next = prev # connect the end of the left side to the beginning of the reversed list 
        init_left_next.next = cur # connect the end of the reversed list to the beginning of the right side we saved earlier

        # now that everything is connected together again, the head might have changed
        # we thus use the dummy variable next pointer to recover the true head of the list and return it
        return dummy.next
