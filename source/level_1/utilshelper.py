import pygame
import math
from queue import PriorityQueue

# WIDTH = 800
# HEIGHT = 400
# WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("A* Path Finding Algorithm")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class Point():
	def __init__(self, x, y):
		pass


def make_grid(rows, width):
	grid = []
	gap = width // rows

	return grid


def draw_grid(win, rows, width):
	gap = width // rows

def draw(win, grid, rows, width):
	win.fill(WHITE)

	for row in grid:
		for spot in row:
			spot.draw(win)

	draw_grid(win, rows, width)
	pygame.display.update()


def main(win, width):
	ROWS = 50
	grid = make_grid(ROWS, width)

	start = None
	end = None

	run = True
	while run:
		draw(win, grid, ROWS, width)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		# 	if pygame.mouse.get_pressed()[0]: # LEFT
		# 		pos = pygame.mouse.get_pos()
		# 		row, col = get_clicked_pos(pos, ROWS, width)
		# 		spot = grid[row][col]
		# 		if not start and spot != end:
		# 			start = spot
		# 			start.make_start()

		# 		elif not end and spot != start:
		# 			end = spot
		# 			end.make_end()

		# 		elif spot != end and spot != start:
		# 			spot.make_barrier()

		# 	elif pygame.mouse.get_pressed()[2]: # RIGHT
		# 		pos = pygame.mouse.get_pos()
		# 		row, col = get_clicked_pos(pos, ROWS, width)
		# 		spot = grid[row][col]
		# 		spot.reset()
		# 		if spot == start:
		# 			start = None
		# 		elif spot == end:
		# 			end = None

		# 	if event.type == pygame.KEYDOWN:
		# 		if event.key == pygame.K_SPACE and start and end:
		# 			for row in grid:
		# 				for spot in row:
		# 					spot.update_neighbors(grid)

		# 			algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)

		# 		if event.key == pygame.K_c:
		# 			start = None
		# 			end = None
		# 			grid = make_grid(ROWS, width)

	pygame.quit()

# main(WIN, WIDTH)