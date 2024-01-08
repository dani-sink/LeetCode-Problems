"""
Problem 205 from Top Interview 150: Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving 
the order of characters. No two characters may map to the same character, but a character 
may map to itself.
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        s_dict, t_dict = {}, {} # create s and t dictionaries
        count = 1 # used to associate each character with a tag
        for char in s: # for each character in s
            if char not in s_dict: # if the character is not in s dictionary
                s_dict[char] = count # record a tag for it in the dictionary
                count += 1 # increment the tag for the next character
        count = 1 # reset tag
        for char in t: # for each character in t
            if char not in t_dict: # if the character is not in t dictionary
                t_dict[char] = count # record a tag for it in the dictionary
                count += 1 # increment the tag for the next character
        
        transformed_str1, transformed_str2 = "", "" # we will create new strings based on these tags
        for char in s: # for each character in s
            transformed_str1 += str(s_dict[char]) # append the tag associated with this character to the new string
        for char in t: # for each character in s
            transformed_str2 += str(t_dict[char]) # append the tag associated with this character to the new string

        # Since we used the same tag system for both s and t, then they should return the same tag string if they
        # are isomorphic. Thus, return True. On the other hand, if they don't return the same tag string, 
        # then they are not isomorphic. Thus, return False
        return transformed_str1 == transformed_str2