"""
Problem 25 from Top 150 Interview: Reverse Nodes in k-Group

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes 
is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Constraints:

    The number of nodes in the list is n.
    1 <= k <= n <= 5000
    0 <= Node.val <= 1000

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    
    # helper function
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

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        count = 1 
        cur = head
        # step done to count the number of elements in the list
        while cur.next is not None: 
            cur = cur.next
            count += 1
        
        count = count - count % k # we determine how many left-out elements there are
        k_groups = [] # we store the index of the k-groups here
        for i in range(1, count, k): 
            k_groups.append([i, i + k - 1]) # we create the k-groups

        for group in  k_groups: # for each group
            head = self.reverseBetween(head, group[0], group[1]) # call reverseBetween using the indexes stored in the group
        return head # return the list
        