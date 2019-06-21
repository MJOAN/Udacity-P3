import heapq
from collections import defaultdict
import math 

def shortest_path(M, start, goal):
    closedset = set()
    
    openset = list()  
    heapq.heappush(openset, (0, start)) 
    
    g = [math.inf] * (len(M.intersections) + 1)
    g[start] = 0
        
    came_from = defaultdict()
    
    f = defaultdict()
    f[start] = calculate_distance(M, start, goal)
     
    while len(openset) > 0:
        (g_cost, current) = heapq.heappop(openset) 
                
        if current == goal:
            return a_star_search_path(came_from, goal)

        closedset.add(current)
        
        for neighbor in M.roads[current]:  
            
            if neighbor in closedset:
                continue
        
            distance_cost = g_cost + calculate_distance(M, current, neighbor)
            
            if neighbor in openset and distance_cost < g[neighbor]: 
                openset.remove(neighbor)
                
            if neighbor not in openset and g[neighbor] > distance_cost:                
                g[neighbor] = distance_cost
                came_from[neighbor] = current 
                
                f[neighbor] = g[neighbor] + calculate_distance(M, neighbor, goal)
                heapq.heappush(openset, (f[neighbor], neighbor))
           
    return "No path found"
         
def a_star_search_path(came_from, current):
    path = [current]
    while current in came_from.keys():
        current = came_from[current]
        path.append(current)
    return path[::-1]

def calculate_distance(M, intersection1, intersection2):
    current_x_y = M.intersections[intersection1]
    neighbor_x_y = M.intersections[intersection2]
    return math.sqrt(sum( [ (a - b) ** 2 for a, b in zip(current_x_y, neighbor_x_y) ] ))

# Citations: 
# 1: https://www.w3resource.com/python-exercises/python-basic-exercise-40.php
# 2: http://theory.stanford.edu/~amitp/GameProgramming/ImplementationNotes.html
# 3: https://en.wikipedia.org/wiki/A*_search_algorithm
