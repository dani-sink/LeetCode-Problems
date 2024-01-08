"""
Problem 49 from Top Interview 150: Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        strs_dict = {} # create a dictionary of the strings
        for string in strs: # for each string in strs list
            sorted_str = ''.join(sorted(string)) # sort the string
            if sorted_str in strs_dict: # if the sorted string is already a key of the dictionary
                strs_dict[sorted_str].append(string) # append the current string to the list associated with this key
            else: # otherwise
                strs_dict[sorted_str] = [string] # create an list for this key and add the current string as an element
        return strs_dict.values() # return the values of this dictionary