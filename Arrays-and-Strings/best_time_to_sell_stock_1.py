"""
Problem 121 from Top Interview 150: Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different 
day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        # Get the current cheapest price, start with the first value
        cheapest_price = prices[0]
        # Current max profit is 0
        max_profit = 0
        #Iterate through the array
        for i in range(n):
            # If substracting the current cheapest_price from the current price
            # gives us more profit, update max_profit
            if prices[i] - cheapest_price > max_profit:
                max_profit = prices[i] - cheapest_price
            # If the current price is lower than the cheapest price, we update
            elif prices[i] < cheapest_price:
                cheapest_price = prices[i]
        
        return max_profit