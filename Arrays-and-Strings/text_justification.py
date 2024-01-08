"""
Problem 68 from Top Interview 150: Text Justification

Given an array of strings words and a width maxWidth, format the text such that each 
line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in 
each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces 
on a line does not divide evenly between words, the empty slots on the left will be assigned more 
spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

    A word is defined as a character sequence consisting of non-space characters only.
    Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    The input array words contains at least one word.
"""

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        characters_so_far = 0
        curr_line = []
        min_white_spaces_needed = 0
        output = []
        while len(words) > 0:
            if characters_so_far + len(words[0]) + min_white_spaces_needed <= maxWidth:
                characters_so_far += len(words[0])
                curr_line.append(words.pop(0))
                if len(curr_line) > 1:
                    min_white_spaces_needed += 1
            if len(words) == 0 or characters_so_far + len(words[0]) + min_white_spaces_needed >= maxWidth:
                dictionary = {}
                for i in range(0, len(curr_line)):
                    dictionary[i] = curr_line[i]
                space_number = 0
                num_to_assign = min_white_spaces_needed
                while min_white_spaces_needed > 0:
                    dictionary[space_number % num_to_assign] += " "
                    space_number += 1
                    min_white_spaces_needed -= 1
                whitespaces_left = maxWidth - (characters_so_far + num_to_assign)
                space_number = 0
                num_to_assign = len(dictionary) - 1
                if len(words) == 0:
                    dictionary[len(curr_line) - 1] += " " * whitespaces_left
                    whitespaces_left = 0
                while whitespaces_left > 0:
                    if num_to_assign <= 0:
                        dictionary[0] += " "
                        whitespaces_left -= 1
                    else:
                        dictionary[space_number % num_to_assign] += " "
                        space_number += 1
                        whitespaces_left -= 1
                str_to_build = ''.join(dictionary.values())
                output.append(str_to_build)
                curr_line = []
                min_white_spaces_needed = 0
                characters_so_far = 0
        return output
        