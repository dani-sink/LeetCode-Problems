"""
Problem 209 from Top Interview 150: Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray
whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
"""

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        start_pointer = 0 
        cur_sum = 0
        min_window_so_far = 10**6
        for i in range(n):
            cur_sum += nums[i] # Accumulate sum until it is higher than the target
            while(cur_sum >= target): # while it is still higher than the target
                cur_sum -= nums[start_pointer] # Remove the element at the start pointer from the sum
            # compare the distance between the current position and new start pointer 
            # with the current minimum window
                min_window_so_far = min(min_window_so_far, i - start_pointer+1) 
                start_pointer += 1 # Advance the start pointer

        if min_window_so_far == 10**6: # If the minimum window is the same as its initial value
            return 0 # Then, the sum of the entire array is less than the target value, so return 0
        else: # Otherwise,
            return min_window_so_far # Return the minimum window