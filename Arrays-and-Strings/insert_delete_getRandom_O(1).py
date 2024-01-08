"""
Problem 380 from Top Interview 150: Insert Delete GetRandom O(1)

Implement the RandomizedSet class:

    . RandomizedSet() Initializes the RandomizedSet object.

    . bool insert(int val) Inserts an item val into the set if not present. Returns 
      true if the item was not present, false otherwise.
      
    . bool remove(int val) Removes an item val from the set if present. Returns true 
      if the item was present, false otherwise.
      
    . int getRandom() Returns a random element from the current set of elements 
      (it's guaranteed that at least one element exists when this method is called). 
      Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in average 
O(1) time complexity.
"""
import random
class RandomizedSet(object):

    def __init__(self):
        self.__random_set = {}
        self.__random_list = []
    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.__random_set:
            return False
        else:
            self.__random_set[val] = 1
            self.__random_list.append(val)
            return True

        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.__random_set:
            del self.__random_set[val]
            self.__random_list.remove(val)
            return True
        else:
            return False

    def getRandom(self):
        """
        :rtype: int
        """
        length = len(self.__random_set)
        random_num = random.randint(0,length-1)
        return self.__random_list[random_num]

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()