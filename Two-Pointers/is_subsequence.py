"""
Problem 392 from Top Interview 150: Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting 
some (can be none) of the characters without disturbing the relative positions of the remaining 
characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(t)
        m = len(s)
        pointer1 = 0
        pointer2 = 0
        while pointer2 < n:
            if pointer1 >= m:
                return True
            if s[pointer1] == t[pointer2]:
                pointer1 += 1
            pointer2 += 1
        
        if pointer1 < m:
            return False
        else:
            return True
        