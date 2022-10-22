read -p "Press enter to start level 1"

cd source/level_1/

# echo Doing the DFS algorithm
# python main.py level_1 dfs ../../input/level_1/map0.txt
# python main.py level_1 dfs ../../input/level_1/map1.txt
# python main.py level_1 dfs ../../input/level_1/map2.txt
# python main.py level_1 dfs ../../input/level_1/map3.txt
# python main.py level_1 dfs ../../input/level_1/map4.txt
# python main.py level_1 dfs ../../input/level_1/map5.txt
# python main.py level_1 dfs ../../input/level_1/map6.txt


# echo Doing the BFS algorithm
# python main.py level_1 bfs ../../input/level_1/map0.txt
# python main.py level_1 bfs ../../input/level_1/map1.txt
# python main.py level_1 bfs ../../input/level_1/map2.txt
# python main.py level_1 bfs ../../input/level_1/map3.txt
# python main.py level_1 bfs ../../input/level_1/map4.txt
# python main.py level_1 bfs ../../input/level_1/map5.txt
# python main.py level_1 bfs ../../input/level_1/map6.txt


# echo Doing the UCS algorithm
# python main.py level_1 ucs ../../input/level_1/map0.txt
# python main.py level_1 ucs ../../input/level_1/map1.txt
# python main.py level_1 ucs ../../input/level_1/map2.txt
# python main.py level_1 ucs ../../input/level_1/map3.txt
# python main.py level_1 ucs ../../input/level_1/map4.txt
# python main.py level_1 ucs ../../input/level_1/map5.txt
# python main.py level_1 ucs ../../input/level_1/map6.txt


echo Doing the GBF Algorithm with Manhattan
# python main.py level_1 gbfs ../../input/level_1/map0.txt 1
# python main.py level_1 gbfs ../../input/level_1/map1.txt 1
# python main.py level_1 gbfs ../../input/level_1/map2.txt 1
python main.py level_1 gbfs ../../input/level_1/map3.txt 1
# python main.py level_1 gbfs ../../input/level_1/map4.txt 1
# python main.py level_1 gbfs ../../input/level_1/map5.txt 1
# python main.py level_1 gbfs ../../input/level_1/map6.txt 1


echo Doing the GBF Algorithm with Euclidean
# python main.py level_1 gbfs ../../input/level_1/map0.txt 2
# python main.py level_1 gbfs ../../input/level_1/map1.txt 2
# python main.py level_1 gbfs ../../input/level_1/map2.txt 2
python main.py level_1 gbfs ../../input/level_1/map3.txt 2
# python main.py level_1 gbfs ../../input/level_1/map4.txt 2
# python main.py level_1 gbfs ../../input/level_1/map5.txt 2
# python main.py level_1 gbfs ../../input/level_1/map6.txt 2


echo Doing the A\* algorithm with Manhattan
# python main.py level_1 astar ../../input/level_1/map0.txt 1
# python main.py level_1 astar ../../input/level_1/map1.txt 1
# python main.py level_1 astar ../../input/level_1/map2.txt 1
python main.py level_1 astar ../../input/level_1/map3.txt 1
# python main.py level_1 astar ../../input/level_1/map4.txt 1
# python main.py level_1 astar ../../input/level_1/map5.txt 1
# python main.py level_1 astar ../../input/level_1/map6.txt 1

echo Doing the A\* algorithm with Euclidean
# python main.py level_1 astar ../../input/level_1/map0.txt 2
# python main.py level_1 astar ../../input/level_1/map1.txt 2
# python main.py level_1 astar ../../input/level_1/map2.txt 2
python main.py level_1 astar ../../input/level_1/map3.txt 2
# python main.py level_1 astar ../../input/level_1/map4.txt 2
# python main.py level_1 astar ../../input/level_1/map5.txt 2
# python main.py level_1 astar ../../input/level_1/map6.txt 2

## Pause for the statistic if needed...
read -p "Press enter to continue level 2"

# echo Doing Level 2 maps
# cd ../level_2/
# python main.py level_2 algo1 ../../input/level_2/map0.txt
# python main.py level_2 algo1 ../../input/level_2/map1.txt
# python main.py level_2 algo1 ../../input/level_2/map2.txt


read -p "Press enter to close the prompt."
