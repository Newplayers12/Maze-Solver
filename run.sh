pip install pygame vidmaker matplotlib

cd source/level_1/

echo Doing the DFS algorithm
python main.py level_1 dfs ../../input/level_1/input1.txt
python main.py level_1 dfs ../../input/level_1/input2.txt
python main.py level_1 dfs ../../input/level_1/input3.txt
python main.py level_1 dfs ../../input/level_1/input4.txt
python main.py level_1 dfs ../../input/level_1/input5.txt
python main.py level_1 dfs ../../input/level_1/input6.txt
python main.py level_1 dfs ../../input/level_1/input7.txt


echo Doing the BFS algorithm
python main.py level_1 bfs ../../input/level_1/input1.txt
python main.py level_1 bfs ../../input/level_1/input2.txt
python main.py level_1 bfs ../../input/level_1/input3.txt
python main.py level_1 bfs ../../input/level_1/input4.txt
python main.py level_1 bfs ../../input/level_1/input5.txt
python main.py level_1 bfs ../../input/level_1/input6.txt
python main.py level_1 bfs ../../input/level_1/input7.txt


echo Doing the UCS algorithm
python main.py level_1 ucs ../../input/level_1/input1.txt
python main.py level_1 ucs ../../input/level_1/input2.txt
python main.py level_1 ucs ../../input/level_1/input3.txt
python main.py level_1 ucs ../../input/level_1/input4.txt
python main.py level_1 ucs ../../input/level_1/input5.txt
python main.py level_1 ucs ../../input/level_1/input6.txt
python main.py level_1 ucs ../../input/level_1/input7.txt


echo Doing the GBF Algorithm with Manhattan
python main.py level_1 gbfs ../../input/level_1/input1.txt 1
python main.py level_1 gbfs ../../input/level_1/input2.txt 1
python main.py level_1 gbfs ../../input/level_1/input3.txt 1
python main.py level_1 gbfs ../../input/level_1/input4.txt 1
python main.py level_1 gbfs ../../input/level_1/input5.txt 1
python main.py level_1 gbfs ../../input/level_1/input6.txt 1
python main.py level_1 gbfs ../../input/level_1/input7.txt 1


echo Doing the GBF Algorithm with Euclidean
python main.py level_1 gbfs ../../input/level_1/input1.txt 2
python main.py level_1 gbfs ../../input/level_1/input2.txt 2
python main.py level_1 gbfs ../../input/level_1/input3.txt 2
python main.py level_1 gbfs ../../input/level_1/input4.txt 2
python main.py level_1 gbfs ../../input/level_1/input5.txt 2
python main.py level_1 gbfs ../../input/level_1/input6.txt 2
python main.py level_1 gbfs ../../input/level_1/input7.txt 2


echo Doing the A\* algorithm with Manhattan
python main.py level_1 astar ../../input/level_1/input1.txt 1
python main.py level_1 astar ../../input/level_1/input2.txt 1
python main.py level_1 astar ../../input/level_1/input3.txt 1
python main.py level_1 astar ../../input/level_1/input4.txt 1
python main.py level_1 astar ../../input/level_1/input5.txt 1
python main.py level_1 astar ../../input/level_1/input6.txt 1
python main.py level_1 astar ../../input/level_1/input7.txt 1

echo Doing the A\* algorithm with Euclidean
python main.py level_1 astar ../../input/level_1/input1.txt 2
python main.py level_1 astar ../../input/level_1/input2.txt 2
python main.py level_1 astar ../../input/level_1/input3.txt 2
python main.py level_1 astar ../../input/level_1/input4.txt 2
python main.py level_1 astar ../../input/level_1/input5.txt 2
python main.py level_1 astar ../../input/level_1/input6.txt 2
python main.py level_1 astar ../../input/level_1/input7.txt 2


echo Doing Level 2 maps
cd ../level_2/
python main.py level_2 algo1 ../../input/level_2/input1.txt
python main.py level_2 algo1 ../../input/level_2/input2.txt
python main.py level_2 algo1 ../../input/level_2/input3.txt
python main.py level_2 algo1 ../../input/level_2/input4.txt


echo Doing Level 3 maps
cd ../level_3/
python main.py level_3 algo2 ../../input/level_3/input1.txt
python main.py level_3 algo2 ../../input/level_3/input2.txt
python main.py level_3 algo2 ../../input/level_3/input3.txt