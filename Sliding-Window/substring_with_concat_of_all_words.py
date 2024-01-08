"""
Problem 30 from Top Interview 150: Substring with Concatenation of All Words

You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated substring in s is a substring that contains all the strings of any permutation of 
words concatenated.

    . For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", 
    and "efcdab" are all concatenated strings. "acdbef" is not a concatenated substring because it is 
    not the concatenation of any permutation of words.

Return the starting indices of all the concatenated substrings in s. 
You can return the answer in any order.
"""

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        n = len(s) # length of entire string
        m = len(words) # length of words array
        word_len = len(words[0]) # lenght of each word in words
        concat_str_len = m * word_len # length of the concatenation of all words in array
        window = ""   # window, initially empty
        indices = []  # where we store the indices
        main_dict = {} # dictionary of the words in words array for reference
        for string in words:
            if string in main_dict:
                main_dict[string] += 1
            else:
                main_dict[string] = 1

        for i in range(0, n): # Iterate over the entire string
            window = s[i:i+concat_str_len] # current window
            if len(window) == concat_str_len: # check if the current window is of size concat_str_len
                # separate window into substrings of size word_len
                substrings = [window[j:j+word_len] for j in range(0, len(window), word_len)]
                curr_dict = {} # Make a dictionary of these substrings
                for string in substrings:
                    if string in curr_dict:
                        curr_dict[string] += 1
                    else:
                        curr_dict[string] = 1
                condition = True
                if main_dict != curr_dict: # If the main dictionary and the current dictionary are different
                    condition = False # Then, the current window is not a concatenated substring of s
                if condition is True: # Otherwise, it is a concatenated substring of s
                    indices.append(i) # Save the index in the indices array
        return indices