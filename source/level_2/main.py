from tokenize import Name
from algo1 import *
import sys

from utilshelper import illustration_video

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
        sys.exit("Usage: python main.py level_2 algo1 ../../input/level_2/map1.txt")
    
    # try to do the algo1.
    try:
        maze = None
        print('Test Level 2: Algorithm - 1 - Search Algorithm...')
        # Read in the maze
        maze = ALGO_1_Maze(sys.argv[3])

        path_cost = maze.ALGO_1_Search()
            
        maze.save_video(sys.argv[3], sys.argv[2])
        write_output_file_txt(sys.argv[3], sys.argv[2], f"{path_cost}")

    except NameError as message:
        print("{}, outputed the result in output folder".format(message))
        write_output_file_txt(sys.argv[3], sys.argv[2], "NO")
    line_break()