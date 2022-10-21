cd source/level_1/

echo Doing the DFS algorithm
# python main.py level_1 dfs ../../input/level_1/map0.txt
# python main.py level_1 dfs ../../input/level_1/map1.txt
# python main.py level_1 dfs ../../input/level_1/map2.txt
# python main.py level_1 dfs ../../input/level_1/map3.txt
# python main.py level_1 dfs ../../input/level_1/map4.txt
# python main.py level_1 dfs ../../input/level_1/map5.txt

python main.py level_1 dfs ../../input/level_1/map8.txt


echo Doing the BFS algorithm
# python main.py level_1 bfs ../../input/level_1/map0.txt
# python main.py level_1 bfs ../../input/level_1/map1.txt
# python main.py level_1 bfs ../../input/level_1/map2.txt
# python main.py level_1 bfs ../../input/level_1/map3.txt
# python main.py level_1 bfs ../../input/level_1/map4.txt
# python main.py level_1 bfs ../../input/level_1/map5.txt

python main.py level_1 bfs ../../input/level_1/map8.txt


echo Doing the UCS algorithm
# python main.py level_1 ucs ../../input/level_1/map0.txt
# python main.py level_1 ucs ../../input/level_1/map1.txt
# python main.py level_1 ucs ../../input/level_1/map2.txt
# python main.py level_1 ucs ../../input/level_1/map3.txt
# python main.py level_1 ucs ../../input/level_1/map4.txt
# python main.py level_1 ucs ../../input/level_1/map5.txt

python main.py level_1 ucs ../../input/level_1/map8.txt


echo Doing the GBF Algorithm
# python main.py level_1 gbfs ../../input/level_1/map0.txt
# python main.py level_1 gbfs ../../input/level_1/map1.txt
# python main.py level_1 gbfs ../../input/level_1/map2.txt
# python main.py level_1 gbfs ../../input/level_1/map3.txt
# python main.py level_1 gbfs ../../input/level_1/map4.txt
# python main.py level_1 gbfs ../../input/level_1/map5.txt

python main.py level_1 gbfs ../../input/level_1/map8.txt


echo Doing the A\* algorithm
# python main.py level_1 astar ../../input/level_1/map0.txt

# python main.py level_1 astar ../../input/level_1/map1.txt
# python main.py level_1 astar ../../input/level_1/map2.txt
# python main.py level_1 astar ../../input/level_1/map3.txt
# python main.py level_1 astar ../../input/level_1/map4.txt
# python main.py level_1 astar ../../input/level_1/map5.txt

python main.py level_1 astar ../../input/level_1/map8.txt

## Pause for the statistic if needed...
read -p "Press enter to continue..."

# echo Doing Level 2 maps
# cd source/level_2/
# python main.py level_2 ucs ../../input/level_2/map1.txt
# python main.py level_2 ucs ../../input/level_2/map2.txt
## Map_3 still doesn't have a good path
# python main.py level_2 ucs ../../input/level_2/map0.txt
# python main.py level_2 ucs ../../input/level_2/map1.txt

# pause()