import sys
import math
from queue import PriorityQueue
from queue import LifoQueue
from queue import Queue
import matplotlib.pyplot as plt
import os
import pygame
import vidmaker
from utilshelper import *
import time

VIDEO_INDEX = 0


def manhattan(Start, Goal):
    """
    > The heuristic function takes two tuples as input, and returns the sum of the absolute value of the
    difference between the first elements of the tuples and the second elements of the tuples
    
    :param Start: The starting point of the path
    :param Goal: The goal state
    :return: The distance between the start and goal points.
    """
    return abs(Start[0] - Goal[0]) + abs(Start[1] - Goal[1])

def euclidean(Start, Goal):
    """
    > The heuristic function takes two points as input and returns the Euclidean distance between them
    
    :param Start: The starting point of the path
    :param Goal: The goal position
    :return: The distance between the start and goal points.
    """
    dx = Goal[0] - Start[0]
    dy = Goal[1] - Start[1]
    return math.sqrt(dx*dx + dy * dy)

def diagonal(Start, Goal):
    """
    The diagonal heuristic function.
    The cost of diagonal movement is the cost of non-diagonal movement times the square root of 2. The
    cost of non-diagonal movement is the cost of diagonal movement divided by the square root of 2
    
    :param Start: The starting point of the path
    :param Goal: The goal node
    :return: The cost of moving from Start to Goal.
    """
    # cost of non-diagonal movement
    cost_n = 1
    # cost of diagonal movement
    cost_d = cost_n * math.sqrt(2) 
    d_max = max(abs(Goal[0] - Start[0]), abs(Goal[1] - Start[1]))
    d_min = min(abs(Goal[0] - Start[0]), abs(Goal[1] - Start[1]))
    return  cost_n * (d_max - d_min) + cost_d * d_min

F = {
    'manhattan': manhattan,
    'euclidean': euclidean,
    'diagonal': diagonal,
}


class Node():
    def __init__(self, state, parent, action):
        """
        The function takes in a state, a parent, and an action, and returns a node with the state,
        parent, and action.
        
        :param state: the state in the state space to which the node corresponds
        :param parent: the node that generated this node
        :param action: The action that was taken to get to this state
        """
        self.state = state
        self.parent = parent
        self.action = action
    


class Maze():
    def __init__(self, file_name):
        f=open(file_name,'r')
        # Reading the number of bonus points from the file and then reading the bonus points from the
        # file.
        n_bonus_points = int(next(f)[:-1])
        self.bonus_points = []
        for i in range(n_bonus_points):
            x, y, reward = map(int, next(f).split())
            self.bonus_points.append((x, y, reward))

        # Reading the file and storing it in a matrix.
        text=f.read()
        self.matrix=[list(i) for i in text.splitlines()]
        f.close()
        
        # Getting the shape of the matrix.
        self.shape = [len(self.matrix), len(self.matrix[0])]
        # A list of explored nodes, served for drawing the map.
        self.draw_explored = []
        # start node of the map (maze)
        self.start = None 
        # escape node of the map (maze)
        self.goal = None 
        # walls of the map (notate: "X" in the input files)
        self.walls = [] 
        # solution list: store every single path from 
        # the pick-up point number i to i + 1
        self.solution = []

        # Read the start and goal positions and the walls -> store in the object.
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j]=='S':
                    self.start=(i,j)

                elif self.matrix[i][j]==' ':
                    if (i==0) or (i==len(self.matrix)-1) or (j==0) or (j==len(self.matrix[0])-1):
                        self.goal=(i,j)
                
                elif self.matrix[i][j] == 'X':
                    self.walls.append((i, j))
                        
                elif self.matrix[i][j] == '+':
                    pass
                else:
                    pass
        f.close()
    
    def generateSuccessors(self, state):
        """
        It takes a state (a tuple of (row, col) coordinates) and returns a list of (action, state)
        pairs. 
        
        The action is one of "up", "down", "left", or "right". 
        
        The state is a new (row, col) tuple that is the result of moving in the specified direction. 
        
        The list of (action, state) pairs is empty if the state is a wall or if the state is outside the
        grid
        
        :param state: The current state of the agent
        :return: a list of tuples. Each tuple contains an action and a state.
        """
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
    
    def visualize_maze(self, save_img = False, input_dir = None):
        """
        It's a function that draws the map and the route on a graph
        (Source from TA... It seems useless because we've already
         used the pygame library to draw the map in a more colorful way ¯\_( ͡° ͜ʖ ͡°)_/¯.)
        
        :param save_img: whether to save the image or not, defaults to False (optional)
        :param input_dir: the directory of the input file
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
                    marker='s',s=100,color='black')
        
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
            output_dir = os.path.join(os.path.pardir, os.path.pardir, 'output')

            if not os.path.exists(output_dir):
                os.mkdir(output_dir)

            output_dir = os.path.join(output_dir, 'level_2')

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

    def save_video(self, input_dir, algorithm):

        # Example input: ../../input/level_2/map0.txt, astar
        dir_info = input_dir.split('/')

        map_name = dir_info[-1].split('.')[0]
        output_dir = os.path.join(os.path.pardir, os.path.pardir, 'output')

        if not os.path.exists(output_dir):
            os.mkdir(output_dir)

        output_dir = os.path.join(output_dir, dir_info[-2])

        if not os.path.exists(output_dir):
            os.mkdir(output_dir)

        output_dir = os.path.join(output_dir, map_name)
        
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        
        output_dir = os.path.join(output_dir, algorithm)
        
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)

        video = vidmaker.Video(os.path.join(output_dir, algorithm + '.mp4'), late_export=True)
        clock = pygame.time.Clock()
        FPS = 60
        
        HEIGHT = self.shape[0] * 15
        WIDTH = self.shape[1] * 15
        ROWS = 15
        WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Path Finding Algorithm")
        clock.tick(FPS)
        # get the matrix information and store it in grid.
        grid = make_grid(ROWS, WIDTH, HEIGHT, self)


        # draw the pygame console window
        draw(WIN, grid, ROWS, WIDTH, HEIGHT)

        
        # Change the color of the solution path from YELLOW to WHITE
        # refresh the solution to WHITE color, prepare to record the video.
        for sol in self.solution:
            for i in range(len(sol[1])):
                flag = False # check if node in solution is a bonus_point
                for j in range(len(self.bonus_points)):
                    if sol[1][i][0] == self.bonus_points[j][0] and sol[1][i][1] == self.bonus_points[j][1]:
                        flag = True
                        break
                if (flag):
                    Point(sol[1][i][0], sol[1][i][1], 15, 15, ROWS, LIGHT_PINK).draw(WIN)
                else:
                    Point(sol[1][i][0], sol[1][i][1], 15, 15, ROWS, WHITE).draw(WIN)
        
        Point(self.start[0], self.start[1], 15, 15, ROWS, RED).draw(WIN)
        Point(self.goal[0], self.goal[1], 15, 15, ROWS, GREEN).draw(WIN)

        # Start recording the video right here!!
        video.update(pygame.surfarray.pixels3d(WIN).swapaxes(0, 1), inverted=False)
        
        for k in range(len(self.solution)):
            """
            Loop through the solution. Each solution stands for a single stage that the algorithm
            trying to find the path from START_POINTS to the END_POINTS.
            """
            if (0 < k < len(self.bonus_points)):
                START_POINTS = (self.bonus_points[k - 1][:2])
                END_POINTS = (self.bonus_points[k][:2])
            elif k == 0:
                START_POINTS = self.start
                END_POINTS = (self.bonus_points[k][:2])
            else:
                END_POINTS = self.goal
                START_POINTS = (self.bonus_points[k - 1][:2])
            
            Point(START_POINTS[0], START_POINTS[1], 15, 15, ROWS, BLUE).draw(WIN)
            Point(END_POINTS[0], END_POINTS[1], 15, 15, ROWS, BLUE).draw(WIN)
        
            # draw explored nodes in stage k
            for node, cnt in self.draw_explored[k][2:]:
                flag = True # check if node in draw_explored is a bonus_point
                
                for j in range(len(self.bonus_points)):
                    if node[0] == self.bonus_points[j][0] and node[1] == self.bonus_points[j][1]:
                        point = Point(node[0], node[1], 15, 15, ROWS, ORANGE)
                        point.draw(WIN)
                        video.update(pygame.surfarray.pixels3d(WIN).swapaxes(0, 1), inverted=False)
                        flag = False
                        break
                if flag:
                    point = Point(node[0], node[1], 15, 15, ROWS, PURPLE if cnt == 1 else TURQUOISE)
                    point.draw(WIN)
                    video.update(pygame.surfarray.pixels3d(WIN).swapaxes(0, 1), inverted=False)
            
            # draw solution path from START_POINTS to the END_POINTS 
            for i in range(1, len(self.solution[k][1]) - 1):
                flag = True # check if node in solution is a bonus_point
                for j in range(len(self.bonus_points)):
                    if self.solution[k][1][i][0] == self.bonus_points[j][0] and self.solution[k][1][i][1] == self.bonus_points[j][1]:
                        point = Point(self.solution[k][1][i][0], self.solution[k][1][i][1], 15, 15, ROWS, ORANGE)
                        point.draw(WIN)
                        time.sleep(1e-2)
                        video.update(pygame.surfarray.pixels3d(WIN).swapaxes(0, 1), inverted=False)
                        flag = False
                        break
                if flag:
                    point = Point(self.solution[k][1][i][0], self.solution[k][1][i][1], 15, 15, ROWS, YELLOW)
                    point.draw(WIN)
                    time.sleep(1e-2)
                    video.update(pygame.surfarray.pixels3d(WIN).swapaxes(0, 1), inverted=False)
            
            # make the cell white again for the next solution to appear
            for node, cnt in self.draw_explored[k][:]:
                Point(node[0], node[1], 15, 15, ROWS, WHITE).draw(WIN)
                    
            for i in range(len(self.solution[k][1])):
                Point(self.solution[k][1][i][0], self.solution[k][1][i][1], 15, 15, ROWS, WHITE).draw(WIN)
                    
            for x, y, cost in self.bonus_points:
                Point(x, y, 15, 15, ROWS, LIGHT_PINK).draw(WIN)

            Point(self.start[0], self.start[1], 15, 15, ROWS, RED).draw(WIN)
            Point(self.goal[0], self.goal[1], 15, 15, ROWS, GREEN).draw(WIN)

            video.update(pygame.surfarray.pixels3d(WIN).swapaxes(0, 1), inverted=False)

        # Draw the final solution 
        for k in range(len(self.solution)):                    
            for i in range(len(self.solution[k][1])):
                flag = True # check if node in solution is a bonus_point
                if (self.solution[k][1][i] == self.start):
                    Point(self.start[0], self.start[1], 15, 15, ROWS, RED).draw(WIN)
                    continue
                if (self.solution[k][1][i] == self.goal):
                    Point(self.goal[0], self.goal[1], 15, 15, ROWS, GREEN).draw(WIN)
                for j in range(len(self.bonus_points)):
                    if self.solution[k][1][i][0] == self.bonus_points[j][0] and self.solution[k][1][i][1] == self.bonus_points[j][1]:
                        point = Point(self.solution[k][1][i][0], self.solution[k][1][i][1], 15, 15, ROWS, ORANGE)
                        point.draw(WIN)
                        time.sleep(1e-2)
                        video.update(pygame.surfarray.pixels3d(WIN).swapaxes(0, 1), inverted=False)
                        flag = False
                        break
                if flag:
                    point = Point(self.solution[k][1][i][0], self.solution[k][1][i][1], 15, 15, ROWS, YELLOW)
                    point.draw(WIN)
                    time.sleep(1e-2)
                    video.update(pygame.surfarray.pixels3d(WIN).swapaxes(0, 1), inverted=False)

        pygame.image.save(WIN, os.path.join(output_dir, algorithm + '.jpg'))        
        video.export(True)
        pygame.quit()