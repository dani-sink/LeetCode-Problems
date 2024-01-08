"""
Problem 228 from Top Interview 150: Summary Ranges

You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the 
array exactly. That is, each element of nums is covered by exactly one of the 
ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

    . "a->b" if a != b
    
    . "a" if a == b
"""

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        n = len(nums)
        if n == 0:
            return []
        nums_dict = {} # hashmap to store the numbers
        start, end = nums[0], nums[0] # delimiters of the current range, initially placed at the first element
        output = [] # will store all our ranges
        for num in nums: # create the hashmap
            if num not in nums_dict:
                nums_dict[num] = 1
        for index, num in enumerate(nums): #iterate over the nums list
            if num + 1 not in nums_dict: # If the direct successor of the current number is not in the hashmap
                end = num # then, we arrived at the end of the current range, so place the end delimiter at this number
                if start == end: # if the start delimiter is the same as the end delimiter
                    output.append(str(start)) # it means the range is just one number, so add it to the output
                else: # if the start delimiter is not the same as the end delimiter
                    output.append(str(start) + "->" + str(end)) # create the range using start and end and add it to output
                if index < n - 1: # if the current element is not the last element of the list
                    start = nums[index + 1] # set the start to be the next element after the current element we are at

        return output # return the ouput