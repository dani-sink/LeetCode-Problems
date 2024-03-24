"""
Problem 21: Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

Constraints:

    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None and list2 is None: 
            return None # return nothing if both list are empty
        
        # both list are not empty
        new_list = ListNode() # create a new list
        cur_pointer = new_list # keep a pointer to the head of this new list
        l1_pointer = list1 # keep a pointer to the head of list1
        l2_pointer = list2 # keep a pointer to the head of list2
        while l1_pointer is not None and l2_pointer is not None: # while there are still elements to see in both lists
            if l1_pointer.val < l2_pointer.val: # if the value at list1 current node is smaller
                cur_pointer.val = l1_pointer.val # update the current node of new_list with this value
                l1_pointer = l1_pointer.next # move the pointer of list1
            else: # otherwise
                cur_pointer.val = l2_pointer.val # update the current node of new_list with this value
                l2_pointer = l2_pointer.next # move the pointer of list2
            cur_pointer.next = ListNode() # create a next node for the current node in new_list
            cur_pointer = cur_pointer.next # go to that node
        
        if l1_pointer is None: # if there are no longer any element to see in list1
            if l2_pointer is not None: # if there are still elements to see in list2
                while l2_pointer.next is not None: # do the same process as before
                    cur_pointer.val = l2_pointer.val
                    cur_pointer.next = ListNode()
                    cur_pointer = cur_pointer.next # except we only move list2 pointer now
                    l2_pointer = l2_pointer.next

                # when we reach the tail of list2,
                cur_pointer.val = l2_pointer.val # set the current node value to the value of the tail in list2
                cur_pointer.next = None # set the next pointer to None to mark the end of the list.

        if l2_pointer is None: # if there are no longer any element to see in list2
            if l1_pointer is not None: # if there are still elements to see in list1
                while l1_pointer.next is not None: # do the same process except as before
                    cur_pointer.val = l1_pointer.val
                    cur_pointer.next = ListNode()
                    cur_pointer = cur_pointer.next 
                    l1_pointer = l1_pointer.next # except we only move list1 pointer now
                cur_pointer.val = l1_pointer.val # set the current node value to the value of the tail in list1
                cur_pointer.next = None # set the next pointer to None to mark the end of the list.
        
        return new_list