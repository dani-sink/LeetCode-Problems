"""
Problem 138 from Top 150 Interview: Copy List with Random Pointer

A linked list of length n is given such that each node contains an additional random pointer, 
which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new 
nodes, where each new node has its value set to the value of its corresponding original node. 
Both the next and random pointer of the new nodes should point to new nodes in the copied list 
such that the pointers in the original list and copied list represent the same list state. 
None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, 
then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. 
Each node is represented as a pair of [val, random_index] where:
    . val: an integer representing Node.val
    . random_index: the index of the node (range from 0 to n-1) that the 
    random pointer points to, or null if it does not point to any node.

Your code will only be given the head of the original linked list.


Example 1:

Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:

Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:

Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]


Constraints:

    0 <= n <= 1000
    -104 <= Node.val <= 104
    Node.random is null or is pointing to some node in the linked list.

"""





# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None # check for empty list

        # for non-empty list
        new_list = Node(head.val) # create a new_list
        cur_pointer = new_list # keep track of the head of that list
        head_ptr = head # keep track of the head of original list
        dict_mapping = {} # mapping between nodes of original list and new_list

        while head_ptr.next is not None: # while we are not at the tail yet
            cur_pointer.val = head_ptr.val # copy the value of the current node to the value of the original list
            cur_pointer.random = head_ptr.random # point both random pointers of both list to the same node initially
            if not (head_ptr in dict_mapping): # create the mapping
                dict_mapping[head_ptr] = cur_pointer # current node of original list maps to current node of new_list
            head_ptr = head_ptr.next # move the pointer of the original list
            cur_pointer.next = Node(head.val) # create the next node of the current node in the new_list
            cur_pointer = cur_pointer.next # set the next pointer to this node

        # we are at the tail
        cur_pointer.val = head_ptr.val # set the current node value to the original value
        if not (head_ptr in dict_mapping): # create mapping also for the tail
                dict_mapping[head_ptr] = cur_pointer

        cur_pointer.random = head_ptr.random # set the current node random pointer to the original random pointer
        cur_pointer.next = None # set the current node next to None
        cur_pointer = new_list # reset the current node pointer 
        head_ptr = head # reset the original pointer

        while head_ptr is not None: # iterate over the original list
            if cur_pointer.random is not None: # if the random pointer of the current node of new_list is not None
                cur_pointer.random = dict_mapping[head_ptr.random] # use mapping to set it to the appropriate node in the new list
            else: # if the random pointer is None
                cur_pointer.random = None # set the random pointer of the current node to None 
            head_ptr = head_ptr.next # move original pointer
            cur_pointer = cur_pointer.next # move current pointer
        
        return new_list