"""
Problem 1 from Top Interview 150: Two Sum

Given an array of integers nums and an integer target, return indices 
of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        n = len(nums) # length of nums list
        seen = {} # stores the elements we've seen so far and their index
        for i in range(n): # iterate over nums
            
        # since the solution is unique, if we store each element in the hashmap, then doing target - nums[i]
        # where nums[i] is the current element, will always give us at least one element which is already in the hashmap
            y = target - nums[i]
            if y in seen: # if y is already in seen, 
            # then, we found our other element, thus return the index of the other element and the current element
                return [seen[y], i]  
            else: # otherwise
            # create a entry in the hashmap with key the value of the element and with value the index of that element
                seen[nums[i]] = i 