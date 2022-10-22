from heapq import heappush, heappop
from utils import Maze, Node, F, Heuristic_level_2
from copy import deepcopy
import os 

class ALGO_1_Node(Node):
    def __init__(self, state, parent, action, points):
        self.state = state
        self.parent = parent
        self.action = action

        self.list_points = -points # số lượng điểm thưởng đã qua
        self.cost = self.parent.cost if self.parent else 0
        
        self.heuristic = 0
        
    def __eq__(self, other):
        return self.list_points == other.list_points and self.cost == other.cost and self.state == other.state

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        if (self.list_points == other.list_points):
            return self.cost + self.heuristic < other.cost + other.heuristic
        else:
            return self.list_points < other.list_points
       

    def __gt__(self, other):
        return (not self < other) and (not self == other)

    def __le__(self, other):
        return (self < other) or (self == other)

    def __ge__(self, other):
        return (self > other) or (self == other)
    
    def updateCost(self, cost):
        self.cost += cost

    def updateHeuristic(self, goal, list_points):
        self.heuristic = Heuristic_level_2(self.state, goal, list_points)

class ALGO_1_Maze(Maze):
    # def __init__(self):
    #     self.row = len(self.matrix)
    #     self.col = len(self.matrix[0])
    #     self.dist_maze = [[10**10 for i in range(self.col)] for i in range(self.row)]
    
    # def getDist(self, u):
    #     return self.dist_maze[u[0]][u[1]]
    
    # def updateDist(self, u, value):
    #     self.dist_maze[u[0]][u[1]] = value
    
    def ALGO_1_MarkedNode(self): #, actions, path, u, list_points):
        #######################################################################TRASH
        self.explored = set()
        
        # initialize start node
        start = ALGO_1_Node(self.start, parent=None, action=None, points = 0)
        # start.updateHeuristic(self.goal, self.bonus_points)

        # contain the set of child node
        frontier = []
        ## using the Heap to contains the nodes, pushing the one with lowest cost upfront
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
        action = []
        cells = []
        ## Ý tưởng khác, chúng ta vẫn dùng BFS như thường, chỉ cần 
        ## Cần phải chỉnh lại thành một cái DFS đệ quy để có thể đi một ô nhiều lần -> đồng thời thì cũng không có lưu quá nhiều thứ
        # self.dist_maze[self.start[0]][self.start[1]] = 0
        # list_points = deepcopy(self.bonus_points)
        # AnsActions, AnsCells = self.ALGO_1_MarkedNode()
        
        
        # self.solution = (list(map(lambda x:x.action, ListAns)), list(map(lambda x:x.state, ListAns)))
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

        
            