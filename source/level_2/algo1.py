from heapq import heappush, heappop
from utils import Maze, Node, F, Heuristic_level_2
from copy import deepcopy
import sys
sys.setrecursionlimit(10000)


class UCS_Node(Node):
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = self.parent.cost if self.parent else 0
        
        self.heuristic = (0, 0, 0)
        
    def __eq__(self, other):
        return (self.heuristic == other.heuristic) and (self.cost == other.cost)

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self.cost + max(self.heuristic) < other.cost + max(other.heuristic)

    def __gt__(self, other):
        return (not self < other) and (not self == other)

    def __le__(self, other):
        return (self < other) or (self == other)

    def __ge__(self, other):
        return (self > other) or (self == other)
    
    def updateCost(self, cost):
        self.cost += cost

    def updateHeuristic(self, goal, bonus_points):
        self.heuristic = Heuristic_level_2(self.state, goal, bonus_points)

class UCS_Maze(Maze):
    def __init__(self):
        self.row = len(self.matrix)
        self.col = len(self.matrix[0])
        self.dist_maze = [[10**10 for i in range(self.col)] for i in range(self.row)]
        input("Lam xong roi ne")
        

    def ucsMarkedNode(self):
        
        # initialize an empty explored set
        """
        def foo(Head):
            flag[head] = True
            for v in adj[head]:
                
                Reached, costPath = foo(v)
                if (Reached == True):
                    break

            flag[head] = false
            return Reached, costPath
        """
        self.explored = set()
        # Create List points copy
        list_points = deepcopy(self.bonus_points)

        # initialize start node
        start = UCS_Node(self.start, parent=None, action=None)
        # start.updateHeuristic(self.goal, self.bonus_points)
        # check if start node is the goal node
        if start.state == self.goal:
            return start

        # contain the set of child node
        frontier = []
        ## using the Heap to contains the nodes, pushing the one with lowest cost upfront
        heappush(frontier, (start, [start], set()))

        self.draw_explored.append((start.state, 0))
        
        self.explored.add(start.state)

        # Loop untils the Heap is empty
        while frontier:
            # take a node from set
            tempNode, path_Ans, flag = heappop(frontier)
            # print(tempNode.heuristic, tempNode.cost)
            # input()
            self.explored.add(tempNode.state)
            self.draw_explored.append((tempNode.state, 1))
            # self.solution.append(tempNode.action, tempNode.state)
            # self.num_explored += 1

            for action, state in self.generateSuccessors(tempNode.state):
                if state not in flag:
                    # initialzie a child node
                    child = UCS_Node(state=state, parent=tempNode, action=action)
                    if child.state == self.goal:
                        return path_Ans + [child]

                    
                    id = 0
                    if (list_points):
                        for x, y, cost in list_points:
                            if ((x, y) == child.state):
                                child.updateCost(cost)
                                list_points.pop(id)
                                flag.clear()
                                break
                            id += 1

                    child.updateCost(1)
                    child.updateHeuristic(self.goal, list_points)
                    # add child node into frontier and mark it
                    flag.add(child.state)
                    heappush(frontier, (child, path_Ans + [child], deepcopy(flag)))
                    # self.draw_explored.append((child.state, GREY, số điểm đã qua))
        
        
    def ucs_Search(self):
        action = []
        cells = []
        
        try:
            ## Cần phải chỉnh lại thành một cái DFS đệ quy để có thể đi một ô nhiều lần -> đồng thời thì cũng không có lưu quá nhiều thứ

            ListAns = self.ucsMarkedNode()        
           
            self.solution = (list(map(lambda x:x.action, ListAns)), list(map(lambda x:x.state, ListAns)))
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            input()