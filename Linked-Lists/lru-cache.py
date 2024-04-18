"""
Problem 146 from Top 150 Interview: LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

    . LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    
    . int get(int key) Return the value of the key if the key exists, otherwise return -1.
    
    . void put(int key, int value) Update the value of the key if the key exists. Otherwise, 
    add the key-value pair to the cache. If the number of keys exceeds the capacity from this 
    operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

 

Constraints:

    1 <= capacity <= 3000
    0 <= key <= 104
    0 <= value <= 105
    At most 2 * 105 calls will be made to get and put.
    
"""

class Node:

    """
    Node class for our LinkedList class.
    Contain a key, value pair along with previous pointer and next pointer
    """

    def __init__(self, key, value, prev=None, next=None):
        """
        :type key: int
        :type value: int
        :type prev: Node
        :type next: Node
        :rtype: None
        """
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LinkedList:

    """
    Our LinkedList class which represents the recency of use of each cache item
    """

    head = None
    tail = None

    def prepend(self, node):
        """
        Prepends this node to the head of the list. This is used when we want to set
        a node to be the most recently used one.

        :type node: Node
        :rtype: None
        """
        if self.head is not None:
            node.next = self.head
            self.head.prev = node

        if self.tail is None:
            self.tail = node

        self.head = node


    def remove(self, node):
        """
        Removes this node from the linked list by removing 
        all the links pointing to it. This is used when we
        want to evict the least recently used node from 
        the cache

        :type node: Node
        :rtype: None
        """
        if node is None:
            return

        prev_node = node.prev
        next_node = node.next

        if prev_node is not None:
            prev_node.next = next_node

        if next_node is not None:
            next_node.prev = prev_node

        if self.head == node:
            self.head = next_node

        if self.tail == node:
            self.tail = prev_node

        node.prev = None
        node.next = None

        

class LRUCache(object):

    """
    Our LRUCache class
    """

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity # we keep track of the capacity
        self.cache_dict = {} # dictionary used to keep track of the cache (key, value pairs) and to retrieve them in O(1) time
        self.cache_list = LinkedList() # Linked list to keep track of the history of use of each cache items


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache_dict: # if the key is not in the dictionary
            return -1 # return -1
        
        # Otherwise
        target_node = self.cache_dict[key] # Save the value associated with this key, which is a reference to a node in the linked list
        if self.cache_list.head != target_node: # if the head of our cache linked list is different than this value
            self.cache_list.remove(target_node) # Remove the value from its position in the linked list
            self.cache_list.prepend(target_node) # Re-insert the value at the head of the linked list. This is to place the  most recently used value at the head and update the history of the recently used cache items

        return target_node.value # return the value associated with this key.
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        new_node = Node(key, value) # create a new node to insert
        if key in self.cache_dict: # if the key is already in the cache dictionary
            self.remove_node(self.cache_dict[key]) # we remove the node associated with this key from the list

        if len(self.cache_dict) >= self.capacity: # if the size of our dictionary is greater than or equal to the max capacity
            self.evict_lru_node() # evict the least recently used node

        self.cache_list.prepend(new_node) # prepend the new node we created to the list
        self.cache_dict[key] = new_node # Update the key with the new node


    def evict_lru_node(self):
        """
        This function evicts the node at the tail of the list, 
        which is the Least Recently Used node.
        :rtype: None
        """
        lru_node = self.cache_list.tail # get the tail of the linked list

        if lru_node is None: # if there is no tail
            return # stop execution 

        # Otherwise
        self.remove_node(lru_node) # remove the node from the linked list



    def remove_node(self, node):
        """
        Removes this node from the cache linked list

        :type node: Node
        :rtype: None
        """
        self.cache_list.remove(node) # remove the node from the list
        del self.cache_dict[node.key] # delete the (key, value) in the dictionary  


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)