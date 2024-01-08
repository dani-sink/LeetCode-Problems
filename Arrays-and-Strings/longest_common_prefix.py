"""
Problem 14 from Top Interview 150: Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        first_str = strs[0]
        str_to_build = ""
        for i in range(len(first_str)):
            all_same = True
            for s in strs:
                if i >= len(s):
                    all_same = False
                    break
                elif s[i] != first_str[i]:
                    all_same = False
                    break
            if all_same is True:
                str_to_build += first_str[i]
            else:
                return str_to_build
        return str_to_build