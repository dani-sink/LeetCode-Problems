"""
Problem 86 from Top 150 Interview: Partition List

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:

Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:

Input: head = [2,1], x = 2
Output: [1,2]

Constraints:

    The number of nodes in the list is in the range [0, 200].
    -100 <= Node.val <= 100
    -200 <= x <= 200

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        
        if head is None or head.next is None: # Edge case where list is empty or of length 1
            return head

        cur = head
        left_list, right_list = ListNode('blank', None), ListNode('blank', None) # partition list into left and right
        prev_left, prev_right = None, None # pointers keep track of the previous node for each partition
        tail_left = None # pointer to keep track of the tail node of left partition
        cur_left, cur_right = left_list, right_list # current pointers of left and right partitions

        while cur is not None: # iterate over the original list
            if cur.val < x: # if we are in this case, we deal with the left partition
                cur_left.val = cur.val # update the value of the current node
                if cur.next is None: # if we are the end of the original list
                    cur_left.next = None # set the next pointer of the current node of the left partition to None
                    if prev_right is not None: # if the previous node of the right partition points to something
                        prev_right.next = None # set its next pointer to point to None
                    tail_left = cur_left # set the tail pointer of the left partition to the current node
                else: # if we are not at the end yet
                    cur_left.next = ListNode() # make the next pointer of the current node of left partition to point to a new Node
                prev_left = cur_left # move previous pointer of left partition
                cur_left = cur_left.next # move current pointer of left partition
                cur = cur.next # move current pointer of original list

            else: # if we are in this case, we deal with the right partition
                cur_right.val = cur.val # update the value of the current node
                if cur.next is None: # if we are the end of the original list
                    cur_right.next = None # set the next pointer of the current node of the right partition to None
                    if prev_left is not None: # if the previous node of the left partition points to something
                        prev_left.next = None # set its next pointer to point to None
                    tail_left = prev_left # set the tail pointer of the left partition to the previous node of the left partition
                else: # if we are not at the end yet
                    cur_right.next = ListNode() # make the next pointer of the current node of right partition to point to a new Node
                prev_right = cur_right # move previous pointer of right partition
                cur_right = cur_right.next # move current pointer of right partition
                cur = cur.next # move current pointer of original list
        
        # Now we check in which case we are
        if left_list.val == 'blank': # if the left partition is empty
            return right_list # then return the right partition
        elif right_list.val == 'blank': # else if the right partition is empty
            return left_list  # then return the left partition
        else: # otherwise, both partitions are non-empty
            tail_left.next = right_list # reconnect them using the tail pointer of the left partition
        return left_list # return the updated left_list