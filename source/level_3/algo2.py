from heapq import heappush, heappop
from utils import Maze, Node, F, euclidean
from copy import deepcopy
import os 

class ALGO_2_Node(Node):
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

        self.cost = self.parent.cost if self.parent else 0
        
        self.heuristic = 0
        
    def __eq__(self, other):
        return self.cost + self.heuristic == other.cost + self.heuristic and self.state == other.state

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self.cost + self.heuristic < other.cost + other.heuristic
        
    def __gt__(self, other):
        return (not self < other) and (not self == other)

    def __le__(self, other):
        return (self < other) or (self == other)

    def __ge__(self, other):
        return (self > other) or (self == other)
    
    def updateCost(self, cost):
        self.cost += cost

    def updateHeuristic(self, goal):
        self.heuristic = euclidean(self.state, goal)

class ALGO_2_Maze(Maze):
    # def __init__(self):
    #     self.row = len(self.matrix)
    #     self.col = len(self.matrix[0])
    #     self.dist_maze = [[10**10 for i in range(self.col)] for i in range(self.row)]
    
    # def getDist(self, u):
    #     return self.dist_maze[u[0]][u[1]]
    
    # def updateDist(self, u, value):
    #     self.dist_maze[u[0]][u[1]] = value
    
    def ALGO_2_MarkedNode(self, S, E): #, actions, path, u, list_points):
        #######################################################################TRASH        
        self.explored = set()
        
        # initialize start node
        start = ALGO_2_Node(S, parent=None, action=None)
        

        
        frontier = []
        
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
        action = []
        cells = []
        ## Ý tưởng khác, chúng ta vẫn dùng BFS như thường, chỉ cần 
        ## Cần phải chỉnh lại thành một cái DFS đệ quy để có thể đi một ô nhiều lần -> đồng thời thì cũng không có lưu quá nhiều thứ
        # self.dist_maze[self.start[0]][self.start[1]] = 0
        # list_points = deepcopy(self.bonus_points)
        # AnsActions, AnsCells = self.ALGO_2_MarkedNode()
        
        
        # self.solution = (list(map(lambda x:x.action, ListAns)), list(map(lambda x:x.state, ListAns)))
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

        
            