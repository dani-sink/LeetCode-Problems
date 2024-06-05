""" 
Problem 133 from Top 150 Interview: Clone Graph

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, 
the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors 
of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.


Example 1:

Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:

Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.

 

Constraints:

    The number of nodes in the graph is in the range [0, 100].
    1 <= Node.val <= 100
    Node.val is unique for each node.
    There are no repeated edges and no self-loops in the graph.
    The Graph is connected and all nodes can be visited starting from the given node.

"""

from collections import deque

# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):

    # Helper method to deep copy the given graph in a breadth-first search manner
    def bfs(self, start, visited):
        q, q2 = deque(), deque() # create two queues for the original graph and the new graph
        new_visited = set() # create a new visited set for the new graph
        visited.add(start) # add the start node to the queue of the original graph
        q.append(start) # add the start node to the queue
        new_start = Node(start.val) # create a deep copy of the start node
        new_visited.add((new_start, start.val)) # add the new start node to the new visited set associated with the new graph
        q2.append(new_start) # append the new start node to the second queue
        cur_pointer = None # this pointer will point to the current node in the new graph

        while q: # while the first queue is not empty
            cur_node = q.popleft() # get the current node in the original graph by popping from the first queue
            cur_pointer = q2.popleft() # get the current node in the new graph by popping from the second queue
            for neighbor in cur_node.neighbors: # go through each neighbor of the current node
                if neighbor not in visited: # if the neighbor has not yet been visited
                    q.append(neighbor) # add the neighbor to the queue
                    visited.add(neighbor) # add the neighbor to the visited set
                    new_node = Node(neighbor.val) # create a deep copy of the neighbor
                    q2.append(new_node) # append the deep copy to the second queue
                    cur_pointer.neighbors.append(new_node) # add the deep copy to the adjacency list of the current node in the new graph we are building
                    new_visited.add((new_node, neighbor.val)) # add the deep copy to the new visited set for the new graph
                else: # if the neighbor has already been visited
                    value = [tup for tup in new_visited if tup[1] == neighbor.val][0][0] # find the neighbor in the new visited set since it must have been added before
                    cur_pointer.neighbors.append(value) # add the neighbor to the adjacency list of the current node in the new graph

        return new_start # once done with the bfs, we return the new graph


    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        
        visited = set()

        # we perform a bfs of the original graph, deep copying each node and their neighbors during the search, and then we return
        # the new graph
        return self.bfs(node, visited) 