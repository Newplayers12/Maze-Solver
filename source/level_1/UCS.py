from distutils.command import check
from heapq import heappush, heappop
from math import fabs
from utils import Maze, Node, F


class UCS_Node(Node):
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = 0
        self.heuristic = 0
        
    def __eq__(self, other):
        return (self.cost == other.cost)

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return (self.cost < other.cost) 

    def __gt__(self, other):
        return (self.cost > other.cost) 

    def __le__(self, other):
        return (self < other) or (self == other)

    def __ge__(self, other):
        return (self > other) or (self == other)
    
    def updateCost(self, cost):
        self.cost = self.parent.cost + cost

    def updateHeuristic(self, goal, Func):
        self.heuristic = F[Func](self.state, goal)

class UCS_Maze(Maze):
    def ucsMarkedNode(self):

        def checkExist(frontier, state):
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
        ## using the Heap to contains the nodes, pushing the one with lowest cost upfront
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
        action = []
        cells = []
        tempNode = self.ucsMarkedNode()
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