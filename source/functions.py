

"""
    This file contains all the functions - heuristic and non-heuristic
    How to add more functions?
    - Step 1: Define a functions with your choice of arguements like 3 samples from belows. Remember to return the value of heuristic or some tuple of value if you want
    - Step 2: add the functions name to the F Dictionary (look at the samples below)
    - Step 3: Test

"""
def manhattan(Start, Goal):
    # this function calculate the manhattan distance between two points on the plane
    return abs(Start[0] - Goal[0]) + abs(Start[1] - Goal[1])

def euclidean(Start, Goal):
    # this function calculate the Euclidean distance between two points 
    # using the formula sqrt((x1 - x2)** 2 + (y1 - y2)**2)

    dx = Goal[0] - Start[0]
    dy = Goal[1] - Start[1]
    return math.sqrt(dx*dx + dy * dy)

def diagonal(Start, Goal):
    cost_n = 1 # cost of non-diagonal movement
    cost_d = cost_n * math.sqrt(2) # cost of diagonal movement
    d_max = max(abs(Goal[0] - Start[0]), abs(Goal[1] - Start[1]))
    d_min = min(abs(Goal[0] - Start[0]), abs(Goal[1] - Start[1]))
    return  cost_n * (d_max - d_min) + cost_d * d_min




F = {
    'manhattan': manhattan,
    'euclidean': euclidean,
    'diagonal': diagonal,
}
