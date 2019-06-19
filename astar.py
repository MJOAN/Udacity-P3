import heapq
from collections import defaultdict
import math

def shortest_path(M, start, goal):
    closedset= set()
    
    openset= list()
    heapq.heappush(openset, (0, start, 0))
    
    came_from = defaultdict()
    
    f = defaultdict()
    f[start] = calculate_distance(M, start, goal)
    
    while len(openset) > 0:
        (actual_cost, current_node, distance_cost) = heapq.heappop(openset)
        
        if current_node == goal:
            return a_star_search_path(came_from, current_node)
        
        closedset.add(current_node)
        
        for neighbor in M.roads[current_node]:
            if neighbor in closedset:
                continue
                
            distance_cost = actual_cost + calculate_distance(M, current_node, neighbor)
            heuristic = calculate_distance(M, neighbor, goal)

            f[neighbor] = actual_cost + heuristic
            came_from[neighbor] = current_node
            
    return "No path found."
    
def a_star_search_path(came_from, current_node):
    path = [current_node]
    while current_node in came_from.keys():
        current = came_from[current_node]
        path.append(current)
        print('path: ',path)
    return path[::-1]

def calculate_distance(M, coordinate_x_y_1, coordinate_x_y_2):
    current_x_y = M.intersections[coordinate_x_y_1]
    neighbor_x_y = M.intersections[coordinate_x_y_2]
    return math.sqrt(sum([(a - b) ** 2 for a, b in zip(current_x_y, neighbor_x_y)]))

# Citations: 
# 1: https://www.w3resource.com/python-exercises/python-basic-exercise-40.php
# 2: http://theory.stanford.edu/~amitp/GameProgramming/ImplementationNotes.html
# 3: https://en.wikipedia.org/wiki/A*_search_algorithm
