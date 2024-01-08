"""
Problem 151 from Top Interview 150: Reverse Words in a String

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s 
will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. Do not include 
any extra spaces.
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        str_to_build = ""
        n = len(words)
        for i in range(n-1, -1, -1):
            if i == 0:
                str_to_build += words[i]
            else:    
                str_to_build += words[i] + " "
        return str_to_build