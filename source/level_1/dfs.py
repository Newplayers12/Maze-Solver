from utils import Node
from utils import Maze
from queue import LifoQueue

# > This class is a subclass of the `Queue` class that implements a stack
class DFS_LifoQueue():
    def __init__(self):
        self.List=[]
        self.Queue = LifoQueue()

    def put(self, pair):
        """
        It adds a pair to the list and queue.
        
        :param pair: a tuple of (key, value)
        """
        self.List.append(pair)
        self.Queue.put(pair)
    
    def get(self):
        """
        It removes the first element from the queue and returns it.
        :return: A pair of values.
        """
        pair = self.Queue.get()
        self.List.remove(pair)
        return pair

    def checkExist(self, state):
        """
        It checks if the state is already in the list
        
        :param state: the current state of the game
        :return: a boolean value.
        """
        for x in self.List:
            if state == x[0]:
                return True
        return False

    def empty(self):
        """
        This function returns True if the queue is empty, and False otherwise
        :return: the boolean value of the Queue.empty() function.
        """
        return self.Queue.empty()
    
# > This class inherits from the Maze class and implements the depth-first search algorithm to solve
# the maze.
class DFS_Maze(Maze):
    def dfsMarkedNode(self):
        """
        A depth-first search algorithm. It will search the tree from the root node to the leaf node.
        :return: The goal node and the cost of the path to the goal node.
        """
        # initialize an empty explored set
        self.explored = set()

        # initialize start node
        start = Node(self.start, parent=None, action=None)

        # check if start node is the goal node
        if start.state == self.goal:
            return start

        # contain the set of child node
        frontier = DFS_LifoQueue()
        frontier.put((start, 0))
        self.explored.add(start.state)
        

        # do loops until no child node to expand
        while True:
            if frontier.empty():
                raise NameError("no solution")
            
            # take a node from set
            tempNode, cur_cost = frontier.get()
            self.explored.add(tempNode.state)
            self.draw_explored.append((tempNode.state, 1))

            for action, state in self.generateSuccessors(tempNode.state):
                if state not in self.explored and not frontier.checkExist(state):
                    # initialzie a child node
                    child = Node(state=state, parent=tempNode, action=action)
                    if child.state == self.goal:
                        return child, cur_cost + 1
                    
                    # add child node into frontier and mark it
                    frontier.put((child, cur_cost + 1))
                    
                    # self.explored.add(child.state)
                    self.draw_explored.append((child.state, 0))

        
    def dfs_Search(self):
        """
        The function dfs_Search() is used to find the solution to the problem using the Depth First
        Search algorithm.
        :return: The path cost is being returned.
        """
        action = []
        cells = []
        tempNode, path_cost = self.dfsMarkedNode()
        
        # Adding the actions and cells to the list.
        while True:
            action.append(tempNode.action)
            cells.append(tempNode.state)
            tempNode = tempNode.parent
            if tempNode.state == self.start:
                break
        
        # Adding the start node to the list of cells and reversing the list of actions and cells
        # to get the solution.
        cells.append(self.start)
        action.reverse()
        cells.reverse()
        
        self.solution = (action, cells)
        return path_cost