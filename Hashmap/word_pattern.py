"""
Problem 290 from Top Interview 150: Word Pattern

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection 
between a letter in pattern and a non-empty word in s.
"""

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        pattern_dict, s_dict = {}, {} # create pattern and s dictionaries
        count = 1 # used to associate each character or string with a tag
        for char in pattern: # for each character in pattern string
            if char not in pattern_dict: # if the character is not in the pattern dictionary
                pattern_dict[char] = count # record a tag for it in the dictionary
                count += 1 # increment the tag for the next character
        count = 1 # reset tag
        s_strings = s.split() # split s into individual strings
        for string in s_strings: # for each individual string in s
            if string not in s_dict: # if the string is not in s dictionary
                s_dict[string] = count # record a tag for it in the dictionary
                count += 1 # increment the tag for the next character

        transformed_str1, transformed_str2 = "", "" # we will create new strings based on these tags
        for char in pattern: # for each character in the pattern string
            transformed_str1 += str(pattern_dict[char]) # append the tag associated with this character to the new string
        for string in s_strings: # for each individual string in s
            transformed_str2 += str(s_dict[string]) # append the tag associated with this string to the new string
        
        # Since we used the same tag system for both pattern and s, then they should return the same tag string if s
        # follows the same pattern. Thus, return True. On the other hand, if they don't return the same tag string, 
        # then s does not follow the same pattern. Thus, return False
        return transformed_str1 == transformed_str2