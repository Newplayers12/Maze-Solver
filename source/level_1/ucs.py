from distutils.command import check
from heapq import heappush, heappop
from math import fabs
from utils import Maze, Node, F


class UCS_Node(Node):
    def __init__(self, state, parent, action):
        """
        The function takes in a state, a parent, and an action, and returns a node with the state,
        parent, action, and cost.
        
        :param state: the state in the state space to which the node corresponds
        :param parent: the node that generated this node
        :param action: The action that was taken to get to this state
        """
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = 0
        
    def __eq__(self, other):
        """
        The function compares the cost of the current node with the cost of the other node
        
        :param other: The other node to compare to
        :return: true if this cost and the other's cost are equal.
        """
        return (self.cost == other.cost)

    def __ne__(self, other):
        """
        If the two objects are not equal, then the function returns True
        
        :param other: The other object to compare to
        :return: The return value is a boolean value.
        """
        return not (self == other)

    def __lt__(self, other):
        """
        The function compares the cost of the current node with the cost of the node passed as an
        argument
        
        :param other: The other node to compare to
        :return: Boolean value
        """
        return (self.cost < other.cost) 

    def __gt__(self, other):
        """
        The function compares the cost of the current node to the cost of the other node
        
        :param other: The other node to compare to
        :return: Boolean value
        """
        return (self.cost > other.cost) 

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
        The function updateCost() takes in a cost and updates the cost of the current node to be the
        cost of the parent node plus the cost of the current node
        
        :param cost: the cost of the edge from the parent to this node
        """
        self.cost = self.parent.cost + cost

class UCS_Maze(Maze):
    def ucsMarkedNode(self):
        """
        It takes a node, checks if it's the goal, if not, it generates all the successors of that node,
        checks if they're in the frontier or explored set, if not, it adds them to the frontier and
        marks them as explored
        :return: The goal node
        """

        def checkExist(frontier, state):
            """
            It checks if the state is already in the frontier
            
            :param frontier: the list of nodes that are waiting to be expanded
            :param state: the current state of the board
            :return: a boolean value.
            """
            for x in frontier:
                if state == x.state:
                    return True
            return False
    
        # initialize an empty explored set
        self.explored = set()

        # initialize start node
        start = UCS_Node(self.start, parent=None, action=None)

        # check if start node is the goal node
        if start.state == self.goal:
            return start

        # contain the set of child node
        frontier = []
        
        # using the Heap to contains the nodes, pushing the one with lowest cost upfront
        heappush(frontier, start)
        self.draw_explored.append((start.state, 0))
        
        # Loop untils the Heap is empty
        while frontier:
            # take a node from set
            tempNode = heappop(frontier)
            self.explored.add(tempNode.state)
            self.draw_explored.append((tempNode.state, 1))

            for action, state in self.generateSuccessors(tempNode.state):
                if state not in self.explored and not checkExist(frontier, state):
                    for x in frontier:
                        if state == x.state:
                            return 
                    # initialzie a child node
                    child = UCS_Node(state=state, parent=tempNode, action=action)
                    if child.state == self.goal:
                        child.updateCost(1)
                        return child
                    child.updateCost(1)

                    # add child node into frontier and mark it
                    heappush(frontier, child)
                    self.explored.add(child.state)

                    self.draw_explored.append((child.state, 0))
        raise NameError("no solution")
        
        
    def ucs_Search(self):
        """
        The function takes the marked node and traces back to the start node, adding the actions and
        cells to the list
        :return: The path cost is being returned.
        """
        action = []
        cells = []

        tempNode = self.ucsMarkedNode()
        path_cost = tempNode.cost

        # Adding the actions and cells to the list.
        while True:
            action.append(tempNode.action)
            cells.append(tempNode.state)
            tempNode = tempNode.parent
            if tempNode.state == self.start:
                break
        
        # Reverse the tracking list to get the solution.
        cells.append(self.start)
        action.reverse()
        cells.reverse()
        
        self.solution = (action, cells)
        return path_cost