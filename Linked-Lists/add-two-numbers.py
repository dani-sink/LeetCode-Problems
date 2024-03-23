"""
Problem 2 of Top 150 Interview: Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, 
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.

"""



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1, stack2 = [], [] # initialize 2 stacks to store the two list elements
        l1_pointer, l2_pointer = l1, l2
        while l1_pointer is not None: # push all elements of l1 into stack1
            stack1.append(l1_pointer.val)
            l1_pointer = l1_pointer.next
        while l2_pointer is not None: # push all elements of l2 into stack2
            stack2.append(l2_pointer.val)
            l2_pointer = l2_pointer.next

        stack1.reverse() # reverse the order
        stack2.reverse() # reverse the order
        cur1, cur2 = 0, 0
        for digit in stack1: # get the integer represented by stack1
            cur1 = cur1 * 10 + digit
        for digit in stack2: # get the integer represented by stack2
            cur2 = cur2 * 10 + digit
        result = str(cur1 + cur2) # add them 
        final_arr = [int(e) for e in result] # separate each digit into array
        final_arr.reverse() # reverse the array again

        new_list = ListNode() # create a new linked list
        cur_pointer = new_list # another pointer to add elements to the new list
        for count, element in enumerate(final_arr): # for each element of the array
            cur_pointer.val = element # set the value of the current element 
                                      #  in linked list to be the value of the current element in the array
            if count != len(final_arr) - 1: # if we are not at the end of the array yet
                cur_pointer.next = ListNode() # create new node
                cur_pointer = cur_pointer.next # set the current list element to point to this new node 
            else: # otherwise, we are at the end of the list
                cur_pointer.next = None # set the current list element to point to None to end the linked list.

        return new_list # return the new linked list