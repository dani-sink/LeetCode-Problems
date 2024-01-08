"""
Problem 274 from Top Interview 150: H-Index

Given an array of integers citations where citations[i] is the number of citations 
a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: 
    - The h-index is defined as the maximum value of h such that the given 
      researcher has published at least h papers that 
      have each been cited at least h times.
"""
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        # Sort the list in reverse order
        citations.sort(reverse=True)
        last_index = 0
        for i in range(n):
            # If the number of citations is than the current index,
            if citations[i] >= i+1:
                # Save it to last_index
                last_index = i+1
            """
            last_index will contain the index of the last value for
            which citations[i] >= i, which is the h-index.
            """
        return last_index
   