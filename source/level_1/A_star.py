from queue import PriorityQueue
from utils import Node
from utils import Maze
from utils import F

class A_star_Node(Node):
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = 0
        self.heuristic = 0
        
    def __eq__(self, other):
        return (self.cost == other.cost) and (self.heuristic == other.heuristic)

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return (self.heuristic + self.cost < other.heuristic + other.cost) and (self.heuristic < other.heuristic)

    def __gt__(self, other):
        return (self.heuristic + self.cost > other.heuristic + other.cost) and (self.heuristic > other.heuristic)

    def __le__(self, other):
        return (self < other) or (self == other)

    def __ge__(self, other):
        return (self > other) or (self == other)
    
    def updateCost(self):
        self.cost = self.parent.cost + 1

    def updateHeuristic(self, goal, Func):
        self.heuristic = F[Func](self.state, goal)


class Frontier():
    def __init__(self):
        self.frontier = PriorityQueue()

    def add(self, node):
        self.frontier.put((node.cost + node.heuristic, node.heuristic, node))

    # Can be used for another algorithm but seems not useful here...
    # def contains_state(self, state):
        # return any(node.state == state for node in self.frontier)

    def empty(self):
        return self.frontier.qsize() == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier.get()
            return node[2]


class A_star_Maze(Maze):
    def A_star(self):
        """Finds a solution to maze, if one exists."""

        # Keep track of number of states explored
        self.num_explored = 0

        # Initialize frontier to just the starting position
        start = A_star_Node(state=self.start, parent=None, action=None)
        frontier = Frontier()
        frontier.add(start)

        # Initialize an empty explored set
        self.explored = set()

        # Keep looping until solution found
        while True:

            # If nothing left in frontier, then no path
            if frontier.empty():
                raise Exception("no solution")

            # Choose a node from the frontier
            node = frontier.remove()
            self.num_explored += 1

            # If node is the goal, then we have a solution
            if node.state == self.goal:
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                cells.append(start.state)
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return

            # Mark node as explored
            self.explored.add(node.state)

            # Add neighbors to frontier
            for action, state in self.generateSuccessors(node.state):
                # if not frontier.contains_state(state) and state not in self.explored:
                if state not in self.explored:
                    child = A_star_Node(state=state, parent=node, action=action)
                    child.updateCost()
                    child.updateHeuristic(self.goal, "manhattan")
                    frontier.add(child)
