"""
Problem 55 from Top Interview 150: Jump Game

You are given an integer array nums. You are initially positioned at the array's first index, and 
each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n == 1:
            return True
        cur_end = n - 1
        while (cur_end > 0):
            init_cur_end = cur_end
            for i in range(cur_end - 1, -1, -1):
                if (i + nums[i] >= cur_end):
                    cur_end = i
                    break
            final_cur_end = cur_end
            if (init_cur_end == final_cur_end):
                return False
        return True