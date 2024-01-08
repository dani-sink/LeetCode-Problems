"""
Problem 167 from Top Interview 150: Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. Let these two numbers 
be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array 
[index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same 
element twice.

Your solution must use only constant extra space.
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        pointer1 = 0
        pointer2 = n - 1
        cur_sum = 0
        while (pointer1 <= pointer2):
            cur_sum = numbers[pointer1] + numbers[pointer2]
            if cur_sum > target:
                pointer2 -= 1
            elif cur_sum < target:
                pointer1 += 1
            else:
                return [pointer1+1, pointer2+1]