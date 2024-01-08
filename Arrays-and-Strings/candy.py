"""
Problem 135 from Top Interview 150: Candy

There are n children standing in a line. Each child is assigned a rating value given in 
the integer array ratings.

You are giving candies to these children subjected to the following requirements:

    . Each child must have at least one candy.
    
    . Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the candies to the children.
"""

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        candies = n * [1] # Give every child 1 candy initially
        for i in range(1, n): # Traverse ratings from left to right
            if ratings[i] > ratings[i-1]: #  If current child has a higher rating than the previous child
                candies[i] = candies[i-1] + 1 # Current child gets one more candy to maintain Rule #2
        for i in range(n-2,-1, -1): # Traverse ratings from left to right
            if ratings[i] > ratings[i+1]: # If current child has a higher rating than the next child
                if candies[i] <= candies[i+1]: # If its number of candies is less than the next child's
                    candies[i] = candies[i+1] + 1 # Current child gets one more candy to maintain Rule #2
        return sum(candies)
    
"""
Time Complexity Analysis:

    1. Initialization: 
    
        The line n = len(ratings) takes O(1) time.
        
    2. First Loop: 
    
        The first loop for i in range(1, n) iterates 'n' times. Each iteration involves 
        a constant time comparison ratings[i] > ratings[i-1] and an assignment 
        candies[i] = candies[i-1] + 1. Therefore, this loop has a time complexity of O(n).
        
    3. Second Loop: 
        The second loop for i in range(n-2,-1, -1) also iterates 'n' times. Each iteration 
        involves a constant time comparison ratings[i] > ratings[i+1] and a conditional assignment 
        candies[i] = candies[i+1] + 1. Therefore, this loop also has a time complexity of O(n).
    
Overall, the time complexity of the code is O(n).
"""