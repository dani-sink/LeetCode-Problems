"""
Problem 82 from Top 150 Interview:  Remove Duplicates from Sorted List II

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:

Input: head = [1,1,1,2,3]
Output: [2,3]

Constraints:

    The number of nodes in the list is in the range [0, 300].
    -100 <= Node.val <= 100
    The list is guaranteed to be sorted in ascending order.

"""

# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        list_dict = {}
        new_list = ListNode('0', None) # new list we will create
        head_ptr = head
        cur_ptr = new_list
        while head_ptr is not None: # find all duplicates
            if head_ptr.val in list_dict:
                list_dict[head_ptr.val] += 1
            else:
                list_dict[head_ptr.val] = 1
            head_ptr = head_ptr.next
        head_ptr = head
        filtered_list = [item[0] for item in list_dict.items() if item[1] == 1] # filter duplicates
        filtered_list.sort() # sort again just in case
        if len(filtered_list) == 0: # if no element is left, return empty list
            return None
        else: # otherwise
            for count, item in enumerate(filtered_list): # iterate through the non-duplicates
                cur_ptr.val = item # add them to the new_list
                if count == len(filtered_list) - 1: # If we are at the tail
                    cur_ptr.next = None # set next to None to terminate new_list
                else: # otherwise
                    cur_ptr.next = ListNode() # keep adding elements
                    cur_ptr = cur_ptr.next
            return new_list # return the new_list