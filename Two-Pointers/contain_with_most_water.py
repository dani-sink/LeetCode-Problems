"""
Problem 11 from Top Interview 150: Container With Most Water

You are given an integer array height of length n. There are n vertical 
lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the 
container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        pointer1 = 0
        pointer2 = n - 1
        max_area = 0
        length = 0
        width = 0
        while pointer1 <= pointer2:
            length = pointer2 - pointer1
            if height[pointer1] <= height[pointer2]:
                width = height[pointer1]
                pointer1 += 1
            else:
                width = height[pointer2]
                pointer2 -= 1
            if (length * width) > max_area:
                max_area = length * width
        return max_area