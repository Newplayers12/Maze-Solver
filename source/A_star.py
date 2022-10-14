import sys
import math
from queue import PriorityQueue
from queue import LifoQueue
from queue import Queue
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import os
from functions import *


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




class Node():
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
        



class Maze():
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


    def generateSuccessors(self, state):
        row, col = state
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]

        result = []
        for action, (r, c) in candidates:
            if 0 <= r < self.shape[0] and 0 <= c < self.shape[1] and (r, c) not in self.walls:
                result.append((action, (r, c)))
        return result


    def A_star(self):
        """Finds a solution to maze, if one exists."""

        # Keep track of number of states explored
        self.num_explored = 0

        # Initialize frontier to just the starting position
        start = Node(state=self.start, parent=None, action=None)
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
                    child = Node(state=state, parent=node, action=action)
                    child.updateCost()
                    child.updateHeuristic(self.goal, "manhattan")
                    frontier.add(child)

    def bfsMarkedNode(self):
        """Find a solution to maze, if one exists"""

        # keep track of number of states explored
        # self.num_explored = 0

        # initialize an empty explored set
        self.explored = set()

        # initialize start node
        start = Node(self.start, parent=None, action=None)

        # check if start node is the goal node
        if start.state == self.goal:
            return start

        # contain the set of child node
        frontier = Queue()
        frontier.put(start)
        self.explored.add(start.state)

        # do loops until no child node to expand
        while frontier.empty() == False:
            # take a node from set
            tempNode = frontier.get()
            # self.solution.append(tempNode.action, tempNode.state)
            # self.num_explored += 1

            for action, state in self.generateSuccessors(tempNode.state):
                if state not in self.explored:
                    # initialzie a child node
                    child = Node(state=state, parent=tempNode, action=action)
                    if child.state == self.goal:
                        return child
                    # child.updateCost()

                    # add child node into frontier and mark it
                    frontier.put(child)
                    self.explored.add(child.state)
        
    def bfs_Search(self):
        action = []
        cells = []
        tempNode = self.bfsMarkedNode()

        while True:
            action.append(tempNode.action)
            cells.append(tempNode.state)
            tempNode = tempNode.parent
            if tempNode.state == self.start:
                break
        
        action.reverse()
        cells.reverse()
        
        self.solution = (action, cells)


    def dfsMarkedNode(self):
        """Find a solution to maze, if one exists"""

        # keep track of number of states explored
        # self.num_explored = 0

        # initialize an empty explored set
        self.explored = set()

        # initialize start node
        start = Node(self.start, parent=None, action=None)

        # check if start node is the goal node
        if start.state == self.goal:
            return start

        # contain the set of child node
        frontier = LifoQueue()
        frontier.put(start)
        self.explored.add(start.state)

        # do loops until no child node to expand
        while frontier.empty() == False:
            # take a node from set
            tempNode = frontier.get()
            # self.solution.append(tempNode.action, tempNode.state)
            # self.num_explored += 1

            for action, state in self.generateSuccessors(tempNode.state):
                if state not in self.explored:
                    # initialzie a child node
                    child = Node(state=state, parent=tempNode, action=action)
                    if child.state == self.goal:
                        return child
                    # child.updateCost()

                    # add child node into frontier and mark it
                    frontier.put(child)
                    self.explored.add(child.state)
        
    def dfs_Search(self):
        action = []
        cells = []
        tempNode = self.dfsMarkedNode()

        while True:
            action.append(tempNode.action)
            cells.append(tempNode.state)
            tempNode = tempNode.parent
            if tempNode.state == self.start:
                break
        
        action.reverse()
        cells.reverse()
        
        self.solution = (action, cells)

    def visualize_maze(self, save_img = False, input_dir = None):
        """
        Args:
        1. matrix: The matrix read from the input file,
        2. bonus: The array of bonus points,
        3. start, end: The starting and ending points,
        4. route: The route from the starting point to the ending one, defined by an array of (x, y), e.g. route = [(1, 2), (1, 3), (1, 4)]
        """
        #1. Define walls and array of direction based on the route
        walls = self.walls
        route = self.solution[1]

        if route:
            direction=[]
            for i in range(1,len(route)):
                if route[i][0]-route[i-1][0]>0:
                    direction.append('v') #^
                elif route[i][0]-route[i-1][0]<0:
                    direction.append('^') #v        
                elif route[i][1]-route[i-1][1]>0:
                    direction.append('>')
                else:
                    direction.append('<')

            direction.pop(0)

        #2. Drawing the map
        ax=plt.figure(dpi=100).add_subplot(111)

        for i in ['top','bottom','right','left']:
            ax.spines[i].set_visible(False)

        plt.scatter([i[1] for i in walls],[-i[0] for i in walls],
                    marker='X',s=100,color='black')
        
        plt.scatter([i[1] for i in self.bonus_points],[-i[0] for i in self.bonus_points],
                    marker='P',s=100,color='green')

        plt.scatter(self.start[1],-self.start[0],marker='*',
                    s=100,color='gold')

        if route:
            for i in range(len(route)-2):
                plt.scatter(route[i+1][1],-route[i+1][0],
                            marker=direction[i],color='silver')

        plt.text(self.goal[1],-self.goal[0],'EXIT',color='red',
            horizontalalignment='center',
            verticalalignment='center')
        plt.xticks([])
        plt.yticks([])
        
        # Save Plotting Image
        if save_img:
            dir_info = input_dir.split('/')       
            output_dir = os.path.join(os.path.pardir, 'output')

            if not os.path.exists(output_dir):
                os.mkdir(output_dir)
            
            output_dir = os.path.join(output_dir, dir_info[-2])
            if not os.path.exists(output_dir):
                os.mkdir(output_dir)
            plt.savefig(os.path.join(output_dir, dir_info[-1].split('.')[-2] + '.png'))
        
        plt.show()

        print(f'Starting point (x, y) = {self.start[0], self.start[1]}')
        print(f'Ending point (x, y) = {self.goal[0], self.goal[1]}')
        
        for _, point in enumerate(self.bonus_points):
            print(f'Bonus point at position (x, y) = {point[0], point[1]} with point {point[2]}')



if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit("Usage: python A_star.py level_x map.txt")

    maze = Maze(sys.argv[2])

    maze.A_star()
    maze.visualize_maze(True, sys.argv[2])