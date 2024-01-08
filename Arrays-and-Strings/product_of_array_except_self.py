"""
Problem 238 from Top Interview 150: Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal
to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        # Initialize prefix and suffix product arrays to store products
        prefix_sub_array = [1] * n
        suffix_sub_array = [1] * n
        prefix_sub_array[0] = 1
        suffix_sub_array[-1] = 1
        # Compute prefix product array
        for i in range(1, n):
            prefix_sub_array[i] = nums[i-1] * prefix_sub_array[i-1]
        # Compute suffix product array
        for i in range(n - 2, -1, -1):
            suffix_sub_array[i] = nums[i+1] * suffix_sub_array[i+1]
        # Multiply corresponding prefix and suffix products based on index
        answer = [prefix_sub_array[i] * suffix_sub_array[i] for i in range(n)]
        return answer
    
"""
Time Complexity Analysis:

    1. Initialization: 
        The initialization of prefix_sub_array and suffix_sub_array takes O(n) time, as it 
        involves creating lists of length 'n' and assigning initial values to each element.
        
    2. Prefix Subarray Calculation: The first loop iterates 'n' times, and each iteration 
       involves a constant time operation. Therefore, the time complexity of this loop is O(n).
    
    3. Suffix Subarray Calculation: The second loop also iterates 'n' times, and each iteration 
       involves a constant time operation. Therefore, the time complexity of this loop is also O(n).
    
    4. Answer Calculation: The list comprehension at the end iterates 'n' times and performs a 
       constant time operation for each iteration. Therefore, the time complexity of this operation 
       is O(n).
       
Worst-case vs. Best-case of Time Analysis:

    . The worst-case and best-case time complexities are the same for all operations 
      in the code. They all have a time complexity of O(n).

Time Average-case Analysis:

    . The average-case time complexity is the same as the worst-case and best-case 
      time complexities, which is O(n).

Overall, the time complexity of the code is O(n).
"""
