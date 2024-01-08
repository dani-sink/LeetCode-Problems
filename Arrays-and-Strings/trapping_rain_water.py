"""
Problem 42 from Top Interview 150: Trapping Rain Water

Given n non-negative integers representing an elevation map where the 
width of each bar is 1, compute how much water it can trap after raining.
"""

"""
The idea behind the solution is the following: Instead of thinking about how much rainwater 
the elevation map can trap, we could think about how many blocks we should add before the 
elevation map can no longer trap water. Using that reasoning, we create a new elevation map
from the original one, in which water can no longer be trapped and we compare the two maps.
The difference in the bar blocks between both elevation maps will be our answer.
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        height_copy = list(height) # Make a copy of the list
        max_val = max(height) # Get the max value of the list
        max_indexes =  [i for i, val in enumerate(height) if val == max_val] # Search if there are multiples max values
        if len(max_indexes) > 1: # If there are multiple max values
            first_max = max_indexes[0] # Get the first max index
            last_max = max_indexes[-1] # Get the last max index
            for i in range(1, first_max): # Iterate until first max
                if height_copy[i] < height_copy[i-1]: # If current bar height is less than previous one
                    height_copy[i] = height_copy[i-1] # Make it the same height
            for i in range(first_max, last_max): # Iterate between first and last max index
                height_copy[i] = max_val # Set the height to the max height
            for i in range(n-2 , last_max-1, -1): #  Iterate from the end until last max
                if height_copy[i] < height_copy[i+1]: # If current bar height is less than next one
                    height_copy[i] = height_copy[i+1] # Make it the same height

            # Get the total rainwater by getting absolute difference between the heights of both maps
            total_rain_water = [abs(height_copy[i] - height[i]) for i in range(n)] 
            return sum(total_rain_water) # Return the sum of this new list
        else: # If there is only one max value
            index_max = height.index(max_val) # Get its index
            for i in range(1, index_max): # Iterate until we reach the max index
                if height_copy[i] < height_copy[i-1]: # If current bar height is less than previous one
                    height_copy[i] = height_copy[i-1] # Make it the same height
            for i in range(n-2 , index_max-1, -1): #  Iterate from the end until the max
                if height_copy[i] < height_copy[i+1]:  # If current bar height is less than next one
                    height_copy[i] = height_copy[i+1] # Make it the same height

            # Get the total rainwater by getting absolute difference between the heights of both maps
            total_rain_water = [abs(height_copy[i] - height[i]) for i in range(n)] 
            return sum(total_rain_water) # Return the sum of this new list