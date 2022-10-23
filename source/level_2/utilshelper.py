from matplotlib.pyplot import bone
from utils import *
from re import L

import pygame
import math
from queue import PriorityQueue
import os

pygame.display.set_caption("A* Path Finding Algorithm")


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

# > A `Point` object represents a point in 2-D space.
class Point:
	def __init__(self, row, col, width, height, total_rows, color):
		"""
		The function takes in the row, column, width, height, total_rows, and color of the cell and sets
		the row, column, x, y, color, and neighbors of the cell
		
		:param row: the row of the grid the cell is in
		:param col: the column of the grid
		:param width: width of each cell
		:param height: The height of each cell
		:param total_rows: The total number of rows in the grid
		:param color: the color of the pixel
		"""
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
		"""
		It draws a rectangle of this point on the screen
		
		:param win: The window to draw the rectangle on
		"""
		pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

	def update_neighbors(self, grid):
		"""
		Generate the children nodes of this point.

		:param grid: The grid that store the maze's node.
		"""
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
	"""
	It takes the maze, and creates a grid of points, where each point is a square, and the color of the
	square is determined by the value of the point in the maze
	
	:param rows: number of rows in the maze
	:param width: width of the maze
	:param height: height of the maze
	:param maze: the maze object
	:return: A list of lists of points.
	"""
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
	"""
	It draws a grid of lines on the window, with the number of rows and columns being equal to the
	number of rows and columns in the grid
	
	:param win: The window to draw the grid on
	:param rows: The number of rows in the grid
	:param width: The width of the grid
	:param height: The height of the window
	"""
	gap = width // rows
	for i in range(rows):
		pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
		for j in range(height):
			pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


def draw(win, grid, rows, width, height):
	"""
	It draws the grid
	
	:param win: The window that the grid is being drawn on
	:param grid: The grid of points
	:param rows: number of rows in the grid
	:param width: The width of the window
	:param height: The height of the window
	"""
	win.fill(WHITE)

	for row in grid:
		for Point in row:
			Point.draw(win)

	pygame.display.update()