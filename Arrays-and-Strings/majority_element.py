"""
Problem 169 from Top Interview 150: Majority Element

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume 
that the majority element always exists in the array.
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return nums[0]
        dictionary = {}
        pointer1 = 0
        pointer2 = n-1
        max_occurences = -1
        max_num = None
        while pointer1 <= pointer2:
            if nums[pointer1] in dictionary:
                dictionary[nums[pointer1]] += 1
            else:
                dictionary[nums[pointer1]] = 1
            if dictionary[nums[pointer1]] > max_occurences:
                max_occurences = dictionary[nums[pointer1]]
                max_num = nums[pointer1]
            if nums[pointer2] in dictionary:
                dictionary[nums[pointer2]] += 1
            else:
                dictionary[nums[pointer2]] = 1
            if dictionary[nums[pointer2]] > max_occurences:
                max_occurences = dictionary[nums[pointer2]]
                max_num = nums[pointer2]
            pointer1 += 1
            pointer2 -= 1
        return max_num
