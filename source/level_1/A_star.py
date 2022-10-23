from queue import PriorityQueue
from utils import Node
from utils import Maze
from utils import F


# A_star_Node is a subclass of Node that adds a heuristic function to the Node class.
class A_star_Node(Node):
    def __init__(self, state, parent, action):
        """
        The function takes in a state, parent, and action and assigns them to the node
        
        :param state: the state in the state space to which the node corresponds
        :param parent: the node that generated this node
        :param action: the action that was taken to get to this node
        """
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = 0
        self.heuristic = 0
        
    def __eq__(self, other):
        """
        It compares two nodes and returns true if they are equal.
        
        :param other: The other node to compare to
        :return: The return value is a boolean value.
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
        It compares the sum of cost and heuristic value of two nodes.
        
        :param other: The other node to compare to
        :return: The return value is a boolean value.
        """
        return (self.heuristic + self.cost < other.heuristic + other.cost)

    def __gt__(self, other):
        """
        If the sum of the heuristic and cost of the current node is greater than the sum of the
        heuristic and cost of the other node, return true
        
        :param other: The other node to compare to
        :return: The return value is a boolean value.
        """
        return (self.heuristic + self.cost > other.heuristic + other.cost)

    def __le__(self, other):
        """
        If the value of the left operand is less than or equal to the value of the right operand, then
        condition becomes true
        
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
    
    def updateCost(self):
        """
        The function updateCost() updates the cost of the current node by adding 1 to the cost of the
        parent node
        """
        self.cost = self.parent.cost + 1

    def updateHeuristic(self, goal, Func):
        """
        The function takes in a goal state and a heuristic function and updates the heuristic value of
        the node
        
        :param goal: the goal state
        :param Func: The heuristic function to use
        """
        self.heuristic = F[Func](self.state, goal)


# The Frontier class is a data structure that stores a list of nodes that are waiting to be explored
class Frontier():
    def __init__(self):
        """
        The function __init__() is a constructor that initializes the frontier to a PriorityQueue
        """
        self.frontier = PriorityQueue()

    def add(self, node):
        """
        It adds a node to the frontier.
        
        :param node: the node to be added to the frontier
        """
        self.frontier.put((node.cost + node.heuristic, node.heuristic, node))

    def empty(self):
        """
        It checks if the frontier is empty.
        :return: The return statement is returning the size of the queue.
        """
        return self.frontier.qsize() == 0

    def remove(self):
        """
        It removes the first element in the frontier.
        :return: The third element of the tuple 
        (the first and the second are the priority factors of our priority queue).
        """
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier.get()
            return node[2]


# The A_star_Maze class is a subclass of the Maze class. It inherits all the methods and attributes of
# the Maze class, and adds a few more methods and attributes.
class A_star_Maze(Maze):
    def A_star(self, heuristic):
        """
        The above function is the A* search algorithm. It takes in a heuristic function and returns the
        path cost.
        
        :param heuristic: a function that takes in a state and returns a number that is the estimated
        cost from that state to the goal
        :return: The path cost of the solution.
        """

        # Initialize frontier to just the starting position
        start = A_star_Node(state=self.start, parent=None, action=None)
        frontier = Frontier()
        frontier.add(start)
        self.draw_explored.append((start.state, 0))

        # Initialize an empty explored set
        self.explored = set(start.state)
        
        # Keep looping until solution found
        while True:
            # If nothing left in frontier, then no path
            if frontier.empty():
                raise NameError("no solution")

            # Choose a node from the frontier
            node = frontier.remove()

            # If node is the goal, then we have a solution
            if node.state == self.goal:
                actions = []
                cells = []
                path_cost = node.cost
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                cells.append(start.state)
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return path_cost

            # Mark node as explored
            self.explored.add(node.state)
            self.draw_explored.append((node.state, 1))
            
            # Add neighbors to frontier
            for action, state in self.generateSuccessors(node.state):
                if state not in self.explored:
                    child = A_star_Node(state=state, parent=node, action=action)
                    child.updateCost()
                    child.updateHeuristic(self.goal, heuristic)
                    self.explored.add(child.state)
                    frontier.add(child)
                    self.draw_explored.append((child.state, 0))
