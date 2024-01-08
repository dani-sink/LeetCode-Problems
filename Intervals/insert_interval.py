"""
Problem 57 from Top 150 Interview: Insert Intervals

You are given an array of non-overlapping intervals intervals where intervals[i] = [start_i, end_i] 
represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. 
You are also given an interval newInterval = [start, end] that represents the start and end of another 
interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order 
by start_i and intervals still does not have any overlapping intervals 
(merge overlapping intervals if necessary).

Return intervals after the insertion.
"""

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort() # sort the list
        output = [] # our output
        cur_interval = intervals[0] # current interval we are at
        for interval in intervals: # for each interval
            if interval[0] <= cur_interval[1]: # if the current interval is less than or equal to the current interval
                # take the mininum of both intervals first value and the maximum of both intervals second value
                cur_interval = [min(cur_interval[0], interval[0]), max(interval[1], cur_interval[1])]
            else: # if the interval is greater than the current interval
                output.append(cur_interval) # add the current interval to the output
                cur_interval = interval # the current interval is now the interval we are at in the loop

        output.append(cur_interval) # append the last interval to the output
        return output # return the output