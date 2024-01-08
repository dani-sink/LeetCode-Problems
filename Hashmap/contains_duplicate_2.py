"""
Problem 219 from Top Interview 150: Contains Duplicate II

Given an integer array nums and an integer k, return true if there are 
two distinct indices i and j in the array such that nums[i] == nums[j] 
and abs(i - j) <= k.
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dup_dict = {} # create duplicate dictionary
        for index, value in enumerate(nums): # iterate while keeping track of both index and value
            if value in dup_dict: # if nums[i] == nums[j]
                if abs(dup_dict[value] - index) <= k: # if abs(i - j) <= k
                    return True # the conditions are satisfied, thus return True
                else: # if not
                    dup_dict[value] = index # update the index for this number
            else: # if nums[i] != nums[j]
                dup_dict[value] = index # create an entry for this number in the dicitonary for future use

        return False # if we reach this point, then we did not meet the conditions required, thus return false