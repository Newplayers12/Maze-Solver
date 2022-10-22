import sys
import math
from queue import PriorityQueue
from queue import LifoQueue
from queue import Queue
import matplotlib.pyplot as plt
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import vidmaker
from utilshelper import *
import time

VIDEO_INDEX = 0




def manhattan(Start, Goal):
    return abs(Start[0] - Goal[0]) + abs(Start[1] - Goal[1])

def euclidean(Start, Goal):
    dx = Goal[0] - Start[0]
    dy = Goal[1] - Start[1]
    return math.sqrt(dx*dx + dy * dy)

def diagonal(Start, Goal):
    cost_n = 1 # cost of non-diagonal movement
    cost_d = cost_n * math.sqrt(2) # cost of diagonal movement
    d_max = max(abs(Goal[0] - Start[0]), abs(Goal[1] - Start[1]))
    d_min = min(abs(Goal[0] - Start[0]), abs(Goal[1] - Start[1]))
    return  cost_n * (d_max - d_min) + cost_d * d_min

F = {
    '1': manhattan,
    '2': euclidean,
}


class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action
    


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
        self.draw_explored = []
        self.draw_frontier = []
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
        f.close()
    
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
            
            output_dir = os.path.join(output_dir, 'level_1')
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

    def save_video(self, input_dir, algorithm, heuristic = None):
        dir_info = input_dir.split('/')       # ../../input/level_1/map0.txt, astar, "..."

        map_name = dir_info[-1].split('.')[0]
        output_dir = os.path.join(os.path.pardir, os.path.pardir, 'output') #, map_name, algorithm)
        # output/level_1/map1/algorithm/

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
        # if not os.path.exists(output_dir):
        #     os.mkdir(output_dir)
        # file_output = open(os.path.join(output_dir, algorithm + '.txt'), "w")
        # plt.savefig(os.path.join(output_dir, dir_info[-1].split('.')[-2] + '.png'))

        if algorithm in ['astar', 'gbfs']:
            video = vidmaker.Video(os.path.join(output_dir, algorithm + '_heuristic_' + heuristic + '.mp4'), late_export=True)
        else:
            video = vidmaker.Video(os.path.join(output_dir, algorithm + '.mp4'), late_export=True)

        clock = pygame.time.Clock()
        FPS = 60

        HEIGHT = self.shape[0] * 15
        WIDTH = self.shape[1] * 15
        ROWS = 15
        WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Path Finding Algorithm")
        clock.tick(FPS)
        grid = make_grid(ROWS, WIDTH, HEIGHT, self)
        
        run = True
        while run:           
            draw(WIN, grid, ROWS, WIDTH, HEIGHT)
            
            for i in range(1, len(self.solution[1]) - 1):
                point = Point(self.solution[1][i][0], self.solution[1][i][1], 15, 15, ROWS, WHITE)
                point.draw(WIN)

            video.update(pygame.surfarray.pixels3d(WIN).swapaxes(0, 1), inverted=False)
            
            for node, cnt in self.draw_explored[2:]:
                # delta = len(self.draw_frontier) - len(self.draw_explored)
                # if i > delta:
                #     point = Point(self.draw_explored[i - delta][0], self.draw_explored[i - delta][1], 15, 15, ROWS, GREY)
                #     point.draw(WIN)
                point = Point(node[0], node[1], 15, 15, ROWS, PURPLE if cnt == 1 else TURQUOISE)
                point.draw(WIN)
                # time.sleep(1e-4)
                video.update(pygame.surfarray.pixels3d(WIN).swapaxes(0, 1), inverted=False)

            for i in range(len(self.solution[1])):
                point = Point(self.solution[1][i][0], self.solution[1][i][1], 15, 15, ROWS, YELLOW)
                point.draw(WIN)
                time.sleep(1e-2)
                video.update(pygame.surfarray.pixels3d(WIN).swapaxes(0, 1), inverted=False)
            
            Point(self.start[0], self.start[1], 15, 15, ROWS, RED).draw(WIN)
            Point(self.goal[0], self.goal[1], 15, 15, ROWS, GREEN).draw(WIN)

            if algorithm in ['astar', 'gbfs']:
                pygame.image.save(WIN, os.path.join(output_dir, algorithm + '_heuristic_' + heuristic + '.jpg'))
            else:
                pygame.image.save(WIN, os.path.join(output_dir, algorithm + '.jpg'))
            run = False



        # video.update(pygame.surfarray.pixels3d(WIN).swapaxes(0, 1), inverted=False)
        
        video.export(True)
        pygame.quit()
    
