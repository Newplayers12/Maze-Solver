from heapq import heappush, heappop
from utils import Maze, Node, F

### The GBF Heuristic functions
HeuristicFunction = 'euclidean'

class GBF_Node(Node):
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action
        # Cost coi như luôn là 0 vì không có ảnh hưởng 
        self.cost = 0
        self.heuristic = 0
        
    def __eq__(self, other):
        return (self.cost == other.cost) and (self.heuristic == other.heuristic)

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return  (self.heuristic < other.heuristic)

    def __gt__(self, other):
        return (self.heuristic > other.heuristic)

    def __le__(self, other):
        return (self < other) or (self == other)

    def __ge__(self, other):
        return (self > other) or (self == other)
    
    def updateCost(self, cost):
        self.cost = self.parent.cost + cost

    def updateHeuristic(self, goal, Func):
        self.heuristic = F[Func](self.state, goal)

class GBF_Maze(Maze):
    def gbfMarkedNode(self):
        

        # keep track of number of states explored
        # self.num_explored = 0

        # initialize an empty explored set
        self.explored = set()

        # initialize start node
        start = GBF_Node(self.start, parent=None, action=None)
        # start.updateHeuristic(self.goal, HeuristicFunction)
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
        while len(frontier) > 0:
            
            # take a node from set
            tempNode = heappop(frontier)
            self.explored.add(tempNode.state)
            self.draw_explored.append((tempNode.state, 1))
            # self.solution.append(tempNode.action, tempNode.state)
            # self.num_explored += 1

            for action, state in self.generateSuccessors(tempNode.state):
                if state not in self.explored:
                    # initialzie a child node
                    child = GBF_Node(state=state, parent=tempNode, action=action)
                    if child.state == self.goal:
                        child.updateCost(1)

                        return child
                    # we don't use cost to measure for the Greedy Best First Search
                    child.updateCost(1)
                    child.updateHeuristic(self.goal, HeuristicFunction)
                    # add child node into frontier and mark it
                    heappush(frontier, child)
                    
                    self.draw_explored.append((child.state, 0))
        
        raise NameError("no solution")

        
        
    def gbf_Search(self):
        action = []
        cells = []
    
        tempNode = self.gbfMarkedNode()
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