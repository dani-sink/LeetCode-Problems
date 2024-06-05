"""
Problem 399 from Top 150 Interview: Evaluate Division

You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] 
and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there 
is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

 

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0

Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]

 

Constraints:

    1 <= equations.length <= 20
    equations[i].length == 2
    1 <= Ai.length, Bi.length <= 5
    values.length == equations.length
    0.0 < values[i] <= 20.0
    1 <= queries.length <= 20
    queries[i].length == 2
    1 <= Cj.length, Dj.length <= 5
    Ai, Bi, Cj, Dj consist of lower case English letters and digits.

"""

class Node(object):
    def __init__(self, val = "", neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):

    # Helper method to create the directed graph 
    def createGraph(self, equations, values):
        node_list, graph_node_list = [], []
        for eq in equations: # create each node from the equations
            if eq[0] not in node_list:
                node_list.append(eq[0])
                graph_node_list.append(Node(eq[0]))
            if eq[1] not in node_list:
                node_list.append(eq[1])
                graph_node_list.append(Node(eq[1]))

        ind_val = 0
        for eq in equations: # add the edges in both direction for each node
            index1 = node_list.index(eq[0])
            index2 = node_list.index(eq[1])
            graph_node_list[index1].neighbors.append((graph_node_list[index2], values[ind_val])) 
            graph_node_list[index2].neighbors.append((graph_node_list[index1], 1 / values[ind_val])) # if there is an edge from x1 to x2, then the edge going from x_2 to x_1 should have as value the inverse of the value of the equation x_1 / x_2
            ind_val += 1

        return node_list, graph_node_list, graph_node_list[0]

    
    # Helper method to perform a dfs while computing the result of going through a particular computation path.
    def dfs(self, v, visited, acc, target):
        if v.val == target:
            return acc
        if v not in visited:
            visited.add(v)
            for neighbor in v.neighbors:
                if neighbor[0] not in visited:
                    val = self.dfs(neighbor[0], visited, acc * neighbor[1], target)
                    if val != None:
                        return val
            
        


    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # We reduce the problem to that of finding a valid path in a graph
        node_list, graph_node_list, start = self.createGraph(equations, values) # we create the graph
        output = [] # we store the output here
        for query in queries: # for each query
            if query[0] in node_list and query[1] in node_list: # if both variable are valid, then both will be in the graph
                visited = set() # create a visited set for the dfs
                index = node_list.index(query[0]) # get the index of the first variable in the node list
                start = graph_node_list[index] # get the node in the graph node list
                val = self.dfs(start, visited, 1, query[1]) # perform a dfs starting on this node to the target node
                if val is not None: # If the dfs returned an actual value
                    output.append(val) # add the value to the output
                else: # otherwise, the value returned by dfs was None, meaning there is no path from the first variable to the second variable in the graph, which means that the query is actually invalid
                    output.append(float(-1)) # add -1 to the output to represent that
            else: # if we are in this case, then at least one of the variables is invalid 
                output.append(float(-1)) # add -1 to the output to represent that
        return output # finally, we return the output