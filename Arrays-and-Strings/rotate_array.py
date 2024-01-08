"""
Problem 189 from Top Interview 150: Rotate Array

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        last_k = nums[-k:]
        first_k = nums[:-k]
        nums[0:] = last_k + first_k