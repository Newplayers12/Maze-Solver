from queue import Queue
from utils import Maze
from utils import Node


# The class BFS_Queue() is a class that implements a queue data structure using a list
class BFS_Queue():
    def __init__(self):
        """
        The function __init__() is a constructor that initializes the class variables List and Queue
        """
        self.List = []
        self.Queue = Queue()
        
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

    def checkExistState(self, state):
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

# > This class is a subclass of the Maze class, and it uses breadth-first search to find the shortest
# path from the start to the end of the maze
class BFS_Maze(Maze):
    def bfsMarkedNode(self):
        """
        A function that uses BFS to find the shortest path from the start node to the goal node.
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
        frontier = BFS_Queue()
        frontier.put((start, 0))
        self.draw_explored.append((start.state, 0))

        self.explored.add(start.state)

        # do loops until no child node to expand
        while True:
            if frontier.empty():
                raise NameError("no solution")
                
            # take a node from set
            tempNode, cur_cost = frontier.get()
            self.draw_explored.append((tempNode.state, 1))

            for action, state in self.generateSuccessors(tempNode.state):
                if state not in self.explored and not frontier.checkExistState(state):
                    # initialzie a child node
                    child = Node(state=state, parent=tempNode, action=action)
                    if child.state == self.goal:
                        return child, cur_cost + 1
                    # add child node into frontier and mark it
                    frontier.put((child, cur_cost + 1))
                    self.explored.add(child.state)
                    self.draw_explored.append((child.state, 0))

        
    def bfs_Search(self):
        """
        The function is responsible for finding the path from the goal node to the start node
        :return: The path cost is being returned.
        """
        action = []
        cells = []
        
        tempNode, path_cost = self.bfsMarkedNode()
        
        # This is responsible for finding the path from the goal node to
        # the start node.
        while True:
            action.append(tempNode.action)
            cells.append(tempNode.state)
            tempNode = tempNode.parent
            if tempNode.state == self.start:
                break
        
        # Reversing the list of actions and cells by tracking back to the parent node.
        cells.append(self.start)
        action.reverse()
        cells.reverse()
        
        self.solution = (action, cells)
        return path_cost
        