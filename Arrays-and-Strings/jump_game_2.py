"""
Problem 45 from Top Interview 150: Jump Game 2

You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, 
if you are at nums[i], you can jump to any nums[i + j] where:

   . 0 <= j <= nums[i] and
   . i + j < n

Return the minimum number of jumps to reach nums[n - 1].
"""
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        cur_end = n - 1
        all_jumps = []
        num_jumps = 0
        while (cur_end > 0):
            for i in range(cur_end - 1, -1, -1):
                if (i + nums[i] >= cur_end):
                    all_jumps.append((i, nums[i]))
            if (len(all_jumps) > 0):
                cur_end = min(all_jumps, key=lambda x:x[0])[0]
            all_jumps = []
            num_jumps += 1
        return num_jumps
        