"""
Problem 26 from Top Interview 150: Remove Duplicates From Sorted Array 1

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that 
each unique element appears only once. The relative order of the elements should be kept the same. Then 
return the number of unique elements in nums.
Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
     - Change the array nums such that the first k elements of nums contain the unique elements in 
       the order they were present in nums initially. The remaining elements of nums are not important 
       as well as the size of nums.
     - Return k.
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        filtered_list = list(set(nums))
        filtered_list.sort()
        m = len(filtered_list)
        n = len(nums)
        num_dups = n - m
        for i in range(m):
            nums[i] = filtered_list[i]
        for i in range(num_dups):
            nums.pop(m)
        
"""
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be accepted.
"""