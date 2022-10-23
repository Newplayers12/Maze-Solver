from tokenize import Name
from algo2 import *
from bfs import *
from utils import euclidean
import sys

# decorate the terminal when execute the program
def line_break():
    print("***"*20)

def write_output_file_txt(input_dir, algorithm, info):
    """
    It creates a directory structure for the output file, and then writes the output file
    
    :param input_dir: The directory of the input file
    :param algorithm: the name of the algorithm
    :param info: the string that you want to write to the file
    """
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

    file_output = open(os.path.join(output_dir, algorithm + '.txt'), "w")
    file_output.write(info)
    file_output.close()



if __name__ == '__main__':
    line_break()
    # check if the command is legal.
    if len(sys.argv) != 4:
        sys.exit("Usage: python main.py level_3 algo2 ../../input/level_3/map1.txt")
    
    # try to do the algo2.
    try:
        maze = None
        print('Test Level 3: Algorithm - 2 - Search Algorithm...')
        
        # Read in the maze - turn into the BFS maze
        maze_bfs = BFS_Maze(sys.argv[3])
        dp = dict()
        for x, y, cost in maze_bfs.bonus_points:
            dp[(x, y)] = maze_bfs.bfs_Search(maze_bfs.start, (x, y))
        
        # After calculate all the distance from the start to the 
        maze = ALGO_2_Maze(sys.argv[3])
        maze.bonus_points.sort(key = lambda x: dp[(x[:2])])
        sum_path_cost = 0
        sum_path_cost += maze.ALGO_2_Search(maze.start, (maze.bonus_points[0][:2]))
        for i in range(1, len(maze.bonus_points)):
            sum_path_cost += maze.ALGO_2_Search((maze.bonus_points[i - 1][:2]), (maze.bonus_points[i][:2]))

        sum_path_cost += maze.ALGO_2_Search((maze.bonus_points[-1][:2]), maze.goal)

        maze.save_video(sys.argv[3], sys.argv[2])
        write_output_file_txt(sys.argv[3], sys.argv[2], f"{sum_path_cost}")
        
    except NameError as message:
        print("{}, outputed the result in output folder".format(message))
        write_output_file_txt(sys.argv[3], sys.argv[2], "NO")
    line_break()