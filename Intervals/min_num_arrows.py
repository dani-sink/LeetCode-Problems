"""
Problem 452 from Top Interview 150: Minimum Number of Arrows to Burst Balloons


There are some spherical balloons taped onto a flat wall that represents the XY-plane. 

The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a 
balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact 
y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points 
along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. 
There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, 
bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.
"""

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key = lambda x: x[1])
        output = []
        cur_point = points[0]
        cur_edge = points[0][1]
        for point in points: 
            if point[0] <= cur_edge and point[1] >= cur_edge:
                cur_point = [min(cur_point[0], point[0]), max(point[1], cur_point[1])]
            else: 
                output.append(cur_point) 
                cur_point = point
                cur_edge = cur_point[1]
        output.append(cur_point)
        return len(output)