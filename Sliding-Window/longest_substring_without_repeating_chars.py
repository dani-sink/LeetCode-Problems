"""
Problem 3 from Top Interview 150: Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        max_length = 0 # current max length
        window = "" # current window size
        for i in range(0,n):
            if s[i] in window: # if current character is in the window
                if len(window) > max_length: # if the length of the window is greater than the current max length
                    max_length = len(window) # update the length

            # before advancing the window, we must remove any duplicate of the current character so that
            # each character in the window is unique
                while s[i] in window: 
                    window = window[1:] # we do so by advancing the left side of the window by 1
                window += s[i] # Once there is no duplicates anymore, add the current character and continue
            else:   # if current character is not in the window
                window += s[i] # add it
                if len(window) > max_length: # if the length of the window is greater than the current max length
                    max_length = len(window) # update the length
    
        return max_length