"""
Problem 202 from Top Interview 150: Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

    . Starting with any positive integer, replace the number by the sum of the squares of its digits.
    
    . Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a 
      cycle which does not include 1.
      
    . Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        happy_dict = {} # hashmap to store the count of each digit in n
        val_dict = {} # hashmap that stores the values we found as a result of our happy number serch
        val = n # current value, initially n
        max_iters = 10000 # keep the number of iterations under 10000
        i = 0
        while i < max_iters: # iterate at most 10000 times
            str_int = str(val) # convert the current value to a string
            val = 0 # set it equal to 0
            for s in str_int: # for each digit in the current value
                if s in happy_dict: # if it is already in the hashmap
                    val += int(s)**2 # add its square the the current value
                else: # otherwise 
                    happy_dict[s] = 1 # record it in the dictionary
                    val += int(s)**2 # add its square the the current value

            # after completing the loop, we'll a have a new current value                    
            if val == 1: # if this value is equal to 1
                return True # we are done, so return True
            elif val in val_dict: # else if we already encountered this new value in the hashmap that stores values
                break # then, there is a cycle which does not include 1, so return False
            else: # otherwise
                val_dict[val] = 1 # this is the first time we see this new value so record it
            i += 1 # increment the number of iterations

        return False # if we reach this point, then return False