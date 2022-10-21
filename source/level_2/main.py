from tokenize import Name
from bfs import *
from dfs import *
from A_star import *
from UCS import *
from GBF import *
import sys

from utilshelper import illustration_video

if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit("Usage: python main.py dfs level_1 map1.txt")

    try:
        maze = None
        if sys.argv[2] == "dfs":
            print('Test Level 2: DFS - Search Algorithms...')
            maze = DFS_Maze(sys.argv[3])
            maze.dfs_Search()
            
        elif sys.argv[2] == "bfs":
            print('Test Level 2: BFS - Search Algorithms...')
            maze = BFS_Maze(sys.argv[3])
            maze.bfs_Search()
            
        elif sys.argv[2] == "ucs":
            print('Test Level 2: UCS - Search Algorithm...')
            maze = UCS_Maze(sys.argv[3])
            print("Done Maze")
            maze.ucs_Search()
            
        elif sys.argv[2] == "gbf":
            print('Test Level 2: Greedy Best First - Search Algorithms...')
            maze = GBF_Maze(sys.argv[3])
            maze.gbf_Search()

        elif sys.argv[2] == "astar":
            print('Test Level 2: A* Search Algorithms...')
            maze = A_star_Maze(sys.argv[3])
            maze.A_star()
    
        # win = illustration_video(maze, True, sys.argv[3])

        maze.save_video(sys.argv[3], sys.argv[2])
        # maze.visualize_maze(False, sys.argv[3])
    except Exception as message:
        
        print("detect a fault: ", message)
        print("Sao may lai ngu vl ra the")
        input("Nhap gi do di")
    input()