from distutils.command import check
from heapq import heappush, heappop
from utils import Maze, Node, F


class GBF_Node(Node):
    def __init__(self, state, parent, action):
        """
        The function takes in a state, a parent node, and an action, and returns a node object
        
        :param state: the state in the state space to which the node corresponds
        :param parent: The parent node of the current node
        :param action: the action that was taken to get to this node
        """
        self.state = state
        self.parent = parent
        self.action = action
        
        # Assume that the cost is always being 0 if the node does not be reached.
        # Only use to track the path cost in gbf_Search() method.
        self.cost = 0
        self.heuristic = 0
        
    def __eq__(self, other):
        """
        It compares two nodes and returns true if they are equal.
        
        :param other: The other node to compare to
        :return: Boolean value.
        """
        return (self.cost == other.cost) and (self.heuristic == other.heuristic)

    def __ne__(self, other):
        """
        If the two objects are not equal, then the function returns True
        
        :param other: The other object to compare to
        :return: The return value is a boolean value.
        """
        return not (self == other)

    def __lt__(self, other):
        """
        The function returns true if the heuristic value of the current node is less than the heuristic
        value of the other node
        
        :param other: the other node to compare to
        :return: Boolean value.
        """
        return  (self.heuristic < other.heuristic)

    def __gt__(self, other):
        """
        The function returns true if the heuristic value of the current node is greater than the
        heuristic value of the other node
        
        :param other: The other node to compare to
        :return: Boolean value.
        """
        return (self.heuristic > other.heuristic)

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

    def updateHeuristic(self, goal, Func):
        """
        The function takes in a goal state and a heuristic function and updates the heuristic value of
        the node
        
        :param goal: the goal state
        :param Func: The heuristic function to use
        """
        self.heuristic = F[Func](self.state, goal)

class GBF_Maze(Maze):
    def gbfMarkedNode(self, heuristic):
        """
        We use a heap to contain the nodes, and we push the one with lowest cost upfront
        
        :param heuristic: the heuristic function to use
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
        start = GBF_Node(self.start, parent=None, action=None)

        # check if start node is the goal node
        if start.state == self.goal:
            return start

        # contain the set of child node
        frontier = []
        
        # using the Heap to contains the nodes, pushing the one with lowest cost upfront
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
                if state not in self.explored and not checkExist(frontier, state):
                    # initialzie a child node
                    child = GBF_Node(state=state, parent=tempNode, action=action)
                    if child.state == self.goal:
                        child.updateCost(1)
                        return child
                    
                    # we don't use cost to measure for the Greedy Best First Search
                    # we only use this to track the path cost of the solution.
                    child.updateCost(1)
                    child.updateHeuristic(self.goal, heuristic)

                    # add child node into frontier and mark it
                    heappush(frontier, child)
                    
                    self.draw_explored.append((child.state, 0))
        
        # Used to raise an error if there is no solution.
        raise NameError("no solution")

        
        
    def gbf_Search(self, heuristic):
        """
        The function takes in a heuristic and returns the path cost of the solution
        
        :param heuristic: The heuristic function to be used
        :return: The path cost is being returned.
        """
        action = []
        cells = []
    
        tempNode = self.gbfMarkedNode(heuristic)
        path_cost = tempNode.cost

        # Track the path from the goal node to the start node.
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