import heapq
from collections import defaultdict
import math 
    
def shortest_path(M, start, goal):
    openset = set()
    openset.add(start)
    
    closedset = set()
    
    priority_queue = list()
    estimated_cost, distance_cost = 0, 0
    heapq.heappush(priority_queue, (estimated_cost, start, distance_cost))
    
    came_from = defaultdict()
    
    f = defaultdict()
    f[start] = calculate_distance(M, start, goal)
    
    while len(openset) > 0:
        (estimated_cost, current, distance_cost) = heapq.heappop(priority_queue)
        openset.remove(current)
        
        closedset.add(current)
        
        if current == goal:
            return a_star_search_path(came_from, current)
        
        for neighbor in M.roads[current]:  
            
            if neighbor in closedset: 
                continue  
            
            new_cost = distance_cost + calculate_distance(M, current, neighbor)         
            lowest_cost_so_far = get_neighbor_cost(priority_queue, neighbor)
            
            if neighbor not in openset or lowest_cost_so_far < distance_cost:                
                lowest_cost_so_far = distance_cost
                came_from[neighbor] = current 
                
                f[neighbor] = new_cost + calculate_distance(M, neighbor, goal)
                heapq.heappush(priority_queue, (f[neighbor], neighbor, new_cost))
                openset.add(neighbor)

    return False

def get_neighbor_cost(heap, neighbor):
    for i in heap:
        if i[1] == neighbor:  
            item = heap[0][2]
            return item
        
def a_star_search_path(came_from, current):
    path = [current]
    while current in came_from.keys():
        current = came_from[current]
        path.append(current)
    return path[::-1]

def calculate_distance(M, intersection1, intersection2): # cite: 1
    current_x_y = M.intersections[intersection1]
    neighbor_x_y = M.intersections[intersection2]
    return math.sqrt(sum( [ (a - b) ** 2 for a, b in zip(current_x_y, neighbor_x_y) ] ))

# Citations: 
# 1: https://www.w3resource.com/python-exercises/python-basic-exercise-40.php
# 2: http://theory.stanford.edu/~amitp/GameProgramming/ImplementationNotes.html
# 3: https://en.wikipedia.org/wiki/A*_search_algorithm
