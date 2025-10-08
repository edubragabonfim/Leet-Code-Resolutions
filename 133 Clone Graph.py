from collections import deque

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node: return node

        q = deque([node])

        clones = {}
        clones[node.val] = Node(node.val, [])

        while q:
            curr = q.popleft()  # removeu o 1
            curr_clone = clones[curr.val]

            for n in curr.neighbors:
                if n.val not in clones:  # O(1)
                    clones[n.val] = Node(n.val, [])  # Criou clone do 2 e do 3
                    q.append(n)  # Adicionou na lista
                curr_clone.neighbors.append(clones[n.val])

        return clones[node.val]