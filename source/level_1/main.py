from tokenize import Name
from bfs import *
from dfs import *
from A_star import *
from ucs import *
from gbfs import *
import sys
import os


from utilshelper import illustration_video

def line_break():
    print("***"*20)

def write_output_file_txt(input_dir, algorithm, info, heuristic = None): # output/level_1/map1/algorithm/ ...*.txt *.mp4
    dir_info = input_dir.split('/')       # ../../input/level_1/map0.txt, astar, "..."

    map_name = dir_info[-1].split('.')[0]
    output_dir = os.path.join(os.path.pardir, os.path.pardir, 'output') #, map_name, algorithm)
    # output/level_1/map1/algorithm/

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
    if algorithm in ['astar', 'gbfs']:
        file_output = open(os.path.join(output_dir, algorithm + '_heuristic_' + heuristic + '.txt'), "w")
    else:
        file_output = open(os.path.join(output_dir, algorithm + '.txt'), "w")
    # file_output = open(os.path.join(output_dir, algorithm + '.txt'), "w")
    file_output.write(info)
    file_output.close()

if __name__ == '__main__':
    
    line_break()
    if len(sys.argv) != 4 and len(sys.argv) != 5:
        sys.exit("Usage: python main.py level_1 dfs ../../input/level_1/map0.txt")

    try:
        maze = None
        path_cost = 0
        if sys.argv[2] == "dfs":
            print('Test Level 1: DFS - Search Algorithms...')
            maze = DFS_Maze(sys.argv[3])
            path_cost = maze.dfs_Search()
            
        elif sys.argv[2] == "bfs":
            print('Test Level 1: BFS - Search Algorithms...')
            maze = BFS_Maze(sys.argv[3])
            path_cost = maze.bfs_Search()
            
        elif sys.argv[2] == "ucs":
            print('Test Level 1: UCS - Search Algorithm...')
            maze = UCS_Maze(sys.argv[3])
            path_cost = maze.ucs_Search()

        elif sys.argv[2] == "gbfs":
            print('Test Level 1: Greedy Best First - Search Algorithms...')
            maze = GBF_Maze(sys.argv[3])
            path_cost = maze.gbf_Search(sys.argv[4])

        elif sys.argv[2] == "astar":
            print('Test Level 1: A* Search Algorithms...')
            maze = A_star_Maze(sys.argv[3])
            path_cost = maze.A_star(sys.argv[4])
    
        # win = illustration_video(maze, True, sys.argv[3])
        if sys.argv[2] in ['astar', 'gbfs']:
            write_output_file_txt(sys.argv[3], sys.argv[2], f"{path_cost}", sys.argv[4])
            maze.save_video(sys.argv[3], sys.argv[2], sys.argv[4])
        else:
            write_output_file_txt(sys.argv[3], sys.argv[2], f"{path_cost}")
            maze.save_video(sys.argv[3], sys.argv[2])

        # maze.visualize_maze(False, sys.argv[3])
    except NameError as message:
        print("{}, outputed the result in output folder".format(message))
        write_output_file_txt(sys.argv[3], sys.argv[2], "NO")
        
    line_break()