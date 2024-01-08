"""
Problem 242 from Top Interview 150: Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word 
or phrase, typically using all the original letters exactly once.
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict, t_dict = {}, {} # create s and t dictionaries
        
        # create s dictionary
        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1
        
        # create t dictionary
        for char in t:
            if char in t_dict:
                t_dict[char] += 1
            else:
                t_dict[char] = 1
        
        # If both dictionaries are equal, then s and t are anagrams. Otherwise, they are not.
        return s_dict == t_dict