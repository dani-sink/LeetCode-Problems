"""
Problem 27 from Top Interview 150: Remove Element

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are 
not equal to val.
Consider the number of elements in nums which are not equal to val be k, to get accepted, you need 
to do the following things:
    - Change the array nums such that the first k elements of nums contain the elements 
      which are not equal to val. The remaining elements of nums are not important as well 
      as the size of nums.
    - Return k.
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        n = len(nums)
        last_index = -1
        for i in range(n):
            if nums[i] == val:
                count += 1
        filtered_nums = [num for num in nums if num != val]
        m = len(filtered_nums)
        for i in range(m):
            nums[i] = filtered_nums[i]
        for i in range(count):
            nums.pop(m)
            
"""
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be accepted.
"""