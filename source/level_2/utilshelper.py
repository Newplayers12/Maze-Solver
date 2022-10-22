from matplotlib.pyplot import bone
from utils import *
from re import L
from tkinter import Widget
import pygame
import math
from queue import PriorityQueue
import os

pygame.display.set_caption("A* Path Finding Algorithm")

## TO DO: Cần thêm một danh sách các màu đậm dần (biểu hiện cho việc là đã đi qua càng nhiều điểm)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)
LIGHT_PINK = (245, 54, 181)

# start point; end point
class Point:
	def __init__(self, row, col, width, height, total_rows, color):
		self.row = row
		self.col = col
		self.y = row * width
		self.x = col * height

		self.color = color
		self.neighbors = []

		self.width = width
		self.height = height
		self.total_rows = total_rows

	def get_pos(self):
		return self.row, self.col

	def is_closed(self):
		return self.color == RED

	def is_open(self):
		return self.color == GREEN

	def is_barrier(self):
		return self.color == BLACK

	def is_start(self):
		return self.color == ORANGE

	def is_end(self):
		return self.color == TURQUOISE

	def reset(self):
		self.color = WHITE

	def make_start(self):
		self.color = ORANGE

	def make_closed(self):
		self.color = RED

	def make_open(self):
		self.color = GREEN

	def make_barrier(self):
		self.color = BLACK

	def make_end(self):
		self.color = TURQUOISE

	def make_path(self):
		self.color = PURPLE

	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

	def update_neighbors(self, grid):
		self.neighbors = []
		if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # DOWN
			self.neighbors.append(grid[self.row + 1][self.col])

		if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # UP
			self.neighbors.append(grid[self.row - 1][self.col])

		if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): # RIGHT
			self.neighbors.append(grid[self.row][self.col + 1])

		if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # LEFT
			self.neighbors.append(grid[self.row][self.col - 1])

	def __lt__(self, other):
		return False

def make_grid(rows, width, height, maze):
	grid = []
	print("size: ", width, height)
	gap1 = 15
	gap2 = 15

	bonus_points = []
	for i in range(len(maze.bonus_points)):
		bonus_points.append([])
		for j in range(len(maze.bonus_points[0]) - 1):
			bonus_points[i].append(maze.bonus_points[i][j])

	for i in range(int(height / gap1)):
		grid.append([])
		for j in range(int( width/ gap2)):
			if maze.start==(i,j):
				point = Point(i, j, gap1, gap2, rows, RED)
			elif maze.goal==(i,j):
				point = Point(i, j, gap1, gap2, rows, GREEN)
			elif (i, j) in maze.solution[1] and [i, j] not in bonus_points:
				point = Point(i, j, gap1, gap2, rows, YELLOW)
			elif [i, j] in bonus_points:
				point = Point(i, j, gap1, gap2, rows, LIGHT_PINK)
			elif maze.matrix[i][j]=='X':
				point = Point(i, j, gap1, gap2, rows, BLACK)
			elif maze.matrix[i][j]==' ':
				point = Point(i, j, gap1, gap2, rows, WHITE)

			grid[i].append(point)

	return grid


def draw_grid(win, rows, width, height):
	gap = width // rows
	for i in range(rows):
		pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
		for j in range(height):
			pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


def draw(win, grid, rows, width, height):
	win.fill(WHITE)

	for row in grid:
		for Point in row:
			Point.draw(win)

	# draw_grid(win, rows, width, height)
	pygame.display.update()


def illustration_video(maze, save_img = False, input_dir = None):
	def uscln(a, b):
		temp1 = a
		temp2 = b
		while (temp1 != temp2):
			if (temp1 > temp2):
				temp1 -= temp2
			else:
				temp2 -= temp1
		uscln = temp1
		return uscln
	# ROWS specify the length of mini square
	HEIGHT = len(maze.matrix) * 15
	WIDTH = len(maze.matrix[0]) * 15
	ROWS = 15
	WIN = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Path Finding Algorithm")

	# make a grid by many mini squares
	grid = make_grid(ROWS, WIDTH, HEIGHT, maze)

	# use loops to increase and update map
	run = True
	while run:
		draw(WIN, grid, ROWS, WIDTH, HEIGHT)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			else:
				pass
	# Save the screenshot of pygame
	if save_img:
		dir_info = input_dir.split('/')       
		output_dir = os.path.join(os.path.pardir, os.path.pardir, 'output')

		if not os.path.exists(output_dir):
			os.mkdir(output_dir)

		output_dir = os.path.join(output_dir, dir_info[-2])
		if not os.path.exists(output_dir):
			os.mkdir(output_dir)
		pygame.image.save(WIN, os.path.join(output_dir, dir_info[-1].split('.')[-2] + '.png'))
	# quit the windown
	pygame.quit()
	return WIN


# function to draw illustration video
# draw a maze
# if __name__ == '__main__':
# 	maze = Maze("input/level_1/map5.txt")
# 	illustration_video(maze)