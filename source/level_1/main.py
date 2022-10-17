from bfs import *
from dfs import *
from A_star import *
from UCS import *
from GBF import *
import sys

if __name__ == '__main__':
    
    if len(sys.argv) != 4:
        sys.exit("Usage: python main.py dfs level_1 map1.txt")

    maze = None
    if sys.argv[2] == "dfs":
        print('Test Level 1: DFS - Search Algorithms...')
        maze = DFS_Maze(sys.argv[3])
        maze.dfs_Search()
        
    elif sys.argv[2] == "bfs":
        print('Test Level 1: BFS - Search Algorithms...')
        maze = BFS_Maze(sys.argv[3])
        maze.bfs_Search()
        
    elif sys.argv[2] == "ucs":
        print('Test Level 1: UCS - Search Algorithm...')
        maze = UCS_Maze(sys.argv[3])
        maze.ucs_Search()

    if sys.argv[2] == "gbf":
        print('Test Level 1: Greedy Best First - Search Algorithms...')
        maze = GBF_Maze(sys.argv[3])
        maze.gbf_Search()

    elif sys.argv[2] == "astar":
        print('Test Level 1: A* Search Algorithms...')
        maze = A_star_Maze(sys.argv[3])
        maze.A_star()
    
    maze.visualize_maze(True, sys.argv[3])