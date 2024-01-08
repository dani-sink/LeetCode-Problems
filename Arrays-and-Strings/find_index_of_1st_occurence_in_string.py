"""
Problem 28 from Top Interview 150: Zigzag Conversion

Given two strings needle and haystack, return the index of the 
first occurrence of needle in haystack, or -1 if needle is not 
part of haystack.
"""

"""
The idea behind the solution is the following:
  . Create a window of size the length of the needle while keeping 
    a pointer to the start of the window which represents the index
  . Iterate this window over the haystack
  . If the window matches entirely with the needle, return the start pointer.
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        len_needle = len(needle)
        pointer1 = 0
        all_same = True
        found_index = -1
        while pointer1 < n:
            if pointer1 < n and haystack[pointer1] == needle[0]:
                for j in range(pointer1, pointer1 + len_needle):
                    if j < n:
                        if haystack[j] != needle[j - pointer1]:
                            all_same = False
                            break
                    else:
                        all_same = False
                        break
                if all_same is True:
                    found_index = pointer1
                    break
                else:
                    pointer1 += 1
                    all_same = True
            else:
                pointer1 += 1
        return found_index