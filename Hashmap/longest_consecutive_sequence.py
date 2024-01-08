"""
Problem 128 from Top Interview 150: Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the 
longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        if n == 0: # for a list of length 0, the length of the sequence is 0
            return 0
        nums_dict = {} 
        for num in nums: # turn the list into a set
            if num not in nums_dict:
                nums_dict[num] = 1

        nums_set = nums_dict.keys() # get the keys
        maxLen = 1 # max sequence length, initialy 1
        for num in nums_set: # iterate over the set
            if num - 1 not in nums_dict: # if the predecessor of the current number is not in the hashmap
                curNum = num # then, the current sequence starts at this current number
                cur_streak = 1 # represents the number of consecutive numbers we encoutered for this current number
                while curNum + 1 in nums_dict: # while there is a consecutive number
                    curNum += 1 # increment the current number by 1
                    cur_streak += 1 # increase the streak by 1

                # At termination of this loop, we reach this point
                if cur_streak > maxLen: # if the current streak that we found is higher than the max sequence length
                    maxLen = cur_streak # then we found a higher sequence length, so record it
        return maxLen # return the max sequence length