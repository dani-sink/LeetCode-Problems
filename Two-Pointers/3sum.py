"""
Problem 15 from Top Interview 150: 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], 
nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        triplets = []
        for i in range(n):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            cur_element = nums[i]
            cur_nums = nums[:i] + nums[i+1:]
            m = len(cur_nums)
            pointer1 = i
            pointer2 = m - 1
            while pointer1 < pointer2:
                cur_sum = cur_nums[pointer1] + cur_nums[pointer2]
                if cur_sum == -cur_element:
                    new_array = [cur_element, cur_nums[pointer1], cur_nums[pointer2]]
                    if not (sorted(new_array) in triplets):
                        triplets.append(sorted(new_array))
                    pointer1 += 1
                    pointer2 -= 1
                elif cur_sum < -cur_element:
                    pointer1 += 1
                else:
                    pointer2 -= 1
        return triplets