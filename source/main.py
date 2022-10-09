from A_star import Maze
import sys

if __name__ == '__main__':
    
    if len(sys.argv) != 3:
        sys.exit("Usage: python main.py level_1 map1.txt")

    print('Test A-star Algorithm...')
    maze = Maze(sys.argv[2])
    maze.A_star()
    maze.visualize_maze(True, sys.argv[2])