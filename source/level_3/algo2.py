from heapq import heappush, heappop
from utils import Maze, Node, F, euclidean
from copy import deepcopy
import os 

class ALGO_2_Node(Node):
    def __init__(self, state, parent, action):
        """
        The function takes in a state, a parent, and an action, and returns a node with the state,
        parent, and action as attributes, and a cost and heuristic attribute that are set to 0
        
        :param state: The state in the state space to which the node corresponds
        :param parent: the node that generated this node
        :param action: The action that was taken to get to this state
        """
        self.state = state
        self.parent = parent
        self.action = action

        self.cost = self.parent.cost if self.parent else 0
        
        self.heuristic = 0
        
    def __eq__(self, other):
        """
        It compares the cost and heuristic of two nodes.
        
        :param other: The other node to compare to
        :return: Boolean value.
        """
        return self.cost + self.heuristic == other.cost + self.heuristic and self.state == other.state

    def __ne__(self, other):
        """
        If the two objects are not equal, then the function returns True
        
        :param other: The other object to compare to
        :return: The return value is a boolean value.
        """
        return not (self == other)

    def __lt__(self, other):
        """
        It compares the cost of the current node with the cost of the other node.
        
        :param other: The other node to compare to
        :return: Boolean value.
        """
        return self.cost + self.heuristic < other.cost + other.heuristic
        
    def __gt__(self, other):
        """
        If the current object is not less than the other object, and the current object is not equal to
        the other object, then the current object is greater than the other object
        
        :param other: Boolean value
        """
        return (not self < other) and (not self == other)

    def __le__(self, other):
        """
        It compares two objects and returns True if the first object is less than or equal to the second
        object.
        
        :param other: The other object to compare to
        :return: The return value is a boolean value.
        """
        return (self < other) or (self == other)

    def __ge__(self, other):
        """
        If the value of the left operand is greater than or equal to the value of the right operand,
        then condition becomes true
        
        :param other: The other object to compare to
        :return: The result of the comparison: boolean value
        """
        return (self > other) or (self == other)
    
    def updateCost(self, cost):
        """
        This function updates the cost of the item by adding the cost of the item to the current cost of
        the item
        
        :param cost: the cost of the current node
        """
        self.cost += cost

    def updateHeuristic(self, goal):
        """
        The function takes in a goal state and updates the heuristic value of the node to the euclidean
        distance between the node's state and the goal state
        
        :param goal: the goal state
        """
        self.heuristic = euclidean(self.state, goal)

class ALGO_2_Maze(Maze):    
    def ALGO_2_MarkedNode(self, S, E):
        """
        > The function takes in the start and goal state, and returns the path from the start to the
        goal state
        
        :param S: the start state
        :param E: the end state
        :return: The goal node
        """
        # initialize the explored
        self.explored = set()
        
        # initialize start node
        start = ALGO_2_Node(S, parent=None, action=None)

        frontier = []
        
        # using the Heap to contain the nodes
        heappush(frontier, start)
        self.draw_explored.append([])
        self.draw_explored[-1].append((start.state, 0))
        self.explored.add(start.state)

        
        while frontier:
            tempNode = heappop(frontier)
            
            self.explored.add(tempNode.state)

            self.draw_explored[-1].append((tempNode.state, 1))
            
            for action, state in self.generateSuccessors(tempNode.state):
                if state not in self.explored:
                    # initialzie a child node
                    child = ALGO_2_Node(state=state, parent=tempNode, action=action)
                    
                    if child.state == E:
                        child.updateCost(1)
                        return child

                    child.updateCost(1)
                    child.updateHeuristic(E)
                    # add child node into frontier and mark it
                    if child not in frontier:
                        heappush(frontier, child)
                    self.draw_explored[-1].append((child.state, 0))
        raise NameError("No solution")
        
        
    def ALGO_2_Search(self, S, E):
        """
        It takes the start and end nodes, finds the path from the end node to the start node, and then
        reverses the path to get the path from the start node to the end node
        
        :param S: Start state
        :param E: The goal state
        :return: The path cost is being returned.
        """
        action = []
        cells = []

        tempNode = self.ALGO_2_MarkedNode(S, E)
        path_cost = tempNode.cost
        while True:
            action.append(tempNode.action)
            cells.append(tempNode.state)
            tempNode = tempNode.parent
            if tempNode.state == S:
                break
        
        cells.append(S)
        action.reverse()
        cells.reverse()
        
        self.solution.append((action, cells))
        
        return path_cost