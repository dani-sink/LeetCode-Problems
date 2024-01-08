"""
Problem 134 from Top Interview 150: Gas Station

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station 
to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel 
around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, 
it is guaranteed to be unique
"""

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)

        # If the overall sum of the amount of gas is less than the
        # cost of the gas, then we can't make travel around the 
        # circuit once no matter where we start
        if sum(gas) < sum(cost):
            return -1
        
        starting_index = 0   # We record the starting index
        gas_tank = 0      # We keep track of the unit of gas put in the gas tank

        for i in range(n):
            gas_tank += -cost[i] + gas[i]   # Update gas_tank
            if gas_tank < 0:  # If the gas_tank value falls below 0
                starting_index = i+1  # Update starting position to the next one
                gas_tank = 0  # Reset the gas tank to 0

            # We do this because any station between 0 and the cuurent index
            # would not allow for circular movement in the clockwise direction
            # if they were chosen as the starting position because the tank
            # value would fall below zero.

        return starting_index  # Finally, return the starting index


"""
Time Complexity Analysis:

    1. Summing the Lists:
        The operation sum(gas) and sum(cost) both have a time complexity of O(n),
        where 'n' is the length of the lists.

    2. Loop Iteration: 
        The loop for i in range(n) runs 'n' times, so it has a 
        time complexity of O(n).
    
    3. Gas Tank Update: 
        The operation gas_tank += -cost[i] + gas[i] is a constant time operation, so
        it has a time complexity of O(1).

    4. Updating Starting Index: 
        The operation starting_index = i+1 is a constant time operation, so 
        it has a time complexity of O(1).

Overall, the time complexity of the code is O(n), where 'n' is the length of the cost list.
"""