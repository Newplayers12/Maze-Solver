from utils import Node
from utils import Maze
from queue import LifoQueue

class DFS_Maze(Maze):
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
        while True:
            if frontier.empty():
                raise NameError("no solution")
            
            # take a node from set
            tempNode = frontier.get()
            # self.solution.append(tempNode.action, tempNode.state)
            # self.num_explored += 1
            self.explored.add(tempNode.state)
            self.draw_explored.append((tempNode.state, 1))

            for action, state in self.generateSuccessors(tempNode.state):
                if state not in self.explored:
                    # initialzie a child node
                    child = Node(state=state, parent=tempNode, action=action)
                    if child.state == self.goal:
                        return child
                    # child.updateCost()

                    # add child node into frontier and mark it
                    frontier.put(child)
                    # self.explored.add(child.state)
                    self.draw_explored.append((child.state, 0))

        
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
        
        cells.append(self.start)
        action.reverse()
        cells.reverse()
        
        self.solution = (action, cells)