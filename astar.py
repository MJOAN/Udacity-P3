import heapq
import math 

import heapq
from collections import defaultdict
import math 

import heapq
from collections import defaultdict
import math 

def shortest_path(edges, nodes, start, goal):
    closedset = set()
    
    openset = list()  
    
    # heapq will store in tuple(heuristic_estimated_cost, current_node, distance_cost)
    heapq.heappush(openset, (0, start, 0)) 
        
    came_from = defaultdict()
    
    g = [math.inf] * (len(M.intersections) + 1)  
    g[start] = 0
    
    f = defaultdict()
    f[start] = calculate_distance(M, start, goal)
     
    while len(openset) > 0:
        (g_cost, current, distance_cost) = heapq.heappop(openset) 
        
        if current == goal:
            return a_star_search_path(came_from, current)
        
        closedset.add(current)

        for neighbor in M.roads[current]:  
        
            if neighbor in closedset:
                continue

            distance_cost = g_cost + calculate_distance(M, current, neighbor)
            
            heuristic = calculate_distance(M, neighbor, goal)
            f[neighbor] = g[neighbor] + heuristic
            
            heapq.heappush(openset, (f[neighbor], neighbor, distance_cost))
            
            g[neighbor] = distance_cost
            came_from[neighbor] = current   
                  
    return "No path found"

def a_star_search_path(came_from, current):
    path = []
    keys = [key for key in came_from.keys()]
    while current in keys:
        current = came_from[current]
        path.append(current)
    return path

def calculate_distance(M, intersection1, intersection2):
    current_x_y = M.intersections[intersection1]
    neighbor_x_y = M.intersections[intersection2]
    return math.sqrt(sum( [ (a - b) ** 2 for a, b in zip(current_x_y, neighbor_x_y) ] ))


# Citations: 
# 1: https://www.w3resource.com/python-exercises/python-basic-exercise-40.php
# 2: http://theory.stanford.edu/~amitp/GameProgramming/ImplementationNotes.html
# 3: https://en.wikipedia.org/wiki/A*_search_algorithm
