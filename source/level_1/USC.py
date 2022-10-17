from heapq import heappush, heappop
from utils import Maze, Node


class USC_Node(Node):
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = 0
        # Heuristic coi như luôn là 0 vì không có ảnh hưởng 
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
    
    def updateCost(self, cost):
        self.cost = self.parent.cost + cost

    def updateHeuristic(self, goal, Func):
        self.heuristic = F[Func](self.state, goal)

class USC_Maze(Maze):
    def __init__(self, file_name):
        f=open(file_name,'r')
        n_bonus_points = int(next(f)[:-1])
        self.bonus_points = []
        for i in range(n_bonus_points):
            x, y, reward = map(int, next(f)[:-1].split(' '))
            self.bonus_points.append((x, y, reward))

        text=f.read()
        self.matrix=[list(i) for i in text.splitlines()]
        f.close()
        self.shape = [len(self.matrix), len(self.matrix[0])]

        self.start = None
        self.goal = None
        self.walls = []

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j]=='S':
                    self.start=(i,j)

                elif self.matrix[i][j]==' ':
                    if (i==0) or (i==len(self.matrix)-1) or (j==0) or (j==len(self.matrix[0])-1):
                        self.goal=(i,j)
                
                elif self.matrix[i][j] == 'X':
                    self.walls.append((i, j))
                        
                else:
                    pass
    def uscMarkedNode(self):
        

        # keep track of number of states explored
        # self.num_explored = 0

        # initialize an empty explored set
        self.explored = set()

        # initialize start node
        start = USC_Node(self.start, parent=None, action=None)

        # check if start node is the goal node
        if start.state == self.goal:
            return start

        # contain the set of child node
        frontier = []
        ## using the Heap to contains the nodes, pushing the one with lowest cost upfront
        heappush(frontier, start)
        
        self.explored.add(start.state)

        # Loop untils the Heap is empty
        while frontier:
            # take a node from set
            tempNode = heappop(frontier)
            # self.solution.append(tempNode.action, tempNode.state)
            # self.num_explored += 1

            for action, state in self.generateSuccessors(tempNode.state):
                if state not in self.explored:
                    # initialzie a child node
                    child = USC_Node(state=state, parent=tempNode, action=action)
                    if child.state == self.goal:
                        return child
                    child.updateCost(1)

                    # add child node into frontier and mark it
                    heappush(frontier, child)
                    self.explored.add(child.state)
        
        
    def usc_Search(self):
        action = []
        cells = []
        tempNode = self.uscMarkedNode()

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