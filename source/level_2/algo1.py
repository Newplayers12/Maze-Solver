from heapq import heappush, heappop
from utils import Maze, Node, F, Heuristic_level_2
from copy import deepcopy
import os 

# > This class is a subclass of the Node class, and it has a method called `get_next_node` that
# returns the next node in the linked list
class ALGO_1_Node(Node):
    def __init__(self, state, parent, action, points):
        """
        This function is used to create a node object that will be used in the A* search algorithm.
        
        :param state: the current state of the game
        :param parent: the node that this is a successor of
        :param action: the action that was taken to get to this node
        :param points: the number of points that this node has passed through
        """
        self.state = state
        self.parent = parent
        self.action = action

        # number of points that this node has passed through
        self.list_points = -points 
        self.cost = self.parent.cost if self.parent else 0
        
        self.heuristic = 0
        
    def __eq__(self, other):
        """
        It compares two objects of the class "Node" and returns true if they are equal.
        
        :param other: The other node to compare to
        :return: The return value is a boolean value.
        """
        return self.list_points == other.list_points and self.cost == other.cost and self.state == other.state

    def __ne__(self, other):
        """
        If the two objects are not equal, then the function returns True
        
        :param other: The other object to compare to
        :return: The return value is a boolean value.
        """
        return not (self == other)

    def __lt__(self, other):
        """
        If the two states have the same list of points, then the state with the lower cost + heuristic
        is less than the other state. Otherwise, the state with the lower list of points is less than
        the other state
        
        :param other: The other node to compare to
        :return: Boolean value
        """
        if (self.list_points == other.list_points):
            return self.cost + self.heuristic < other.cost + other.heuristic
        else:
            return self.list_points < other.list_points
       

    def __gt__(self, other):
        """
        If the current object is not less than the other object, and the current object is not equal to
        the other object, then the current object is greater than the other object
        
        :param other: The other object to compare to
        :return: The return value is a boolean value.
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
        It compares two objects and returns True if the first object is greater than or equal to the
        second object
        
        :param other: The other object to compare to
        :return: The return value is a boolean value.
        """
        return (self > other) or (self == other)
    
    def updateCost(self, cost):
        """
        This function updates the cost of the item by adding the cost of the item to the current cost of
        the item
        
        :param cost: the cost of the current node
        """
        self.cost += cost

    def updateHeuristic(self, goal, list_points):   
        """
        The function takes in a goal state and a list of points and updates the heuristic of the current
        state to be the heuristic of the current state to the goal state plus the heuristic of the
        current state to the closest point in the list of points
        
        :param goal: the goal state
        :param list_points: a list of points that are obstacles
        """
        self.heuristic = Heuristic_level_2(self.state, goal, list_points)

class ALGO_1_Maze(Maze):    
    def ALGO_1_MarkedNode(self):
        """
        > The function takes in the start and goal state, and returns the path from the start to the
        goal state
        :return: The goal node.
        """
        self.explored = set()
        
        # initialize start node
        start = ALGO_1_Node(self.start, parent=None, action=None, points = 0)

        # contain the set of child node
        frontier = []

        # using the Heap to contains the nodes, pushing the one with lowest cost upfront
        list_points = deepcopy(self.bonus_points)
        heappush(frontier, start)
        self.draw_explored.append((start.state, 0))
        self.explored.add(start.state)

        # Loop untils the Heap is empty
        while frontier:
            # take a node from set
            tempNode = heappop(frontier)
            self.explored.add(tempNode.state)
            self.draw_explored.append((tempNode.state, 1))
            
            for action, state in self.generateSuccessors(tempNode.state):
                if state not in self.explored:
                    # initialzie a child node
                    child = ALGO_1_Node(state=state, parent=tempNode, action=action, points=-tempNode.list_points)
                    
                    if child.state == self.goal:
                        child.updateCost(1)
                        return child

                    # Checking if the current state is a bonus point. If it is, then it updates the
                    # cost of the node and the list of points. If it is not, then it updates the cost
                    # of the node.
                    id = 0  
                    for x, y, cost in list_points:
                        if ((x, y) == child.state):
                            child.updateCost(cost)
                            child.list_points += -1
                            list_points.pop(id)
                            break
                        id += 1
                    else:
                        child.updateCost(1)

                    child.updateHeuristic(self.goal, list_points)
                    # add child node into frontier and mark it
                    if child not in frontier:
                        heappush(frontier, child)
                    self.draw_explored.append((child.state, 0))
        raise NameError("No solution")
        
        
    def ALGO_1_Search(self):
        """
        It takes the marked node and traces back to the start node, appending the actions and cells to a
        list. Then, reverse the action and cells to get the solution.
        :return: The path cost is being returned.
        """
        action = []
        cells = []

        tempNode = self.ALGO_1_MarkedNode()
        path_cost = tempNode.cost
        while True:
            action.append(tempNode.action)
            cells.append(tempNode.state)
            tempNode = tempNode.parent
            if tempNode.state == self.start:
                break
        
        cells.append(self.start)
        action.reverse()
        cells.reverse()
        
        self.solution = (action, cells)
        return path_cost