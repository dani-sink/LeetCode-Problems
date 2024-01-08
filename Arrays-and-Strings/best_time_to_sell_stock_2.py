"""
Problem 121 from Top Interview 150: Best Time to Buy and Sell Stock 2

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of 
the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        
        """
        We only want to take into account positve profit. 
        Thus, negative profit or zero profit should be ignored
        """
        n = len(prices)
        # Initial profit
        max_profit = 0
        for i in range(1,n):
            # Check profit between two adjacent elements
            current_profit = prices[i] - prices[i-1]
            # If profit is positve, add it to the max profit
            if (current_profit > 0):
                max_profit += current_profit
            # Otherwise, do nothing
            
        # Return the profit
        return max_profit
