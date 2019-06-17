import heapq
import math 

def shortest_path(M, start, goal):
    
    closedset = set()
    
    openset = list()  
    # heapq maintains invariant = min cost from start/ tuple = (intersection, cost)
    heapq.heappush(openset, (start, 0))  
    print('openset: ', openset)
    
    came_from = dict()
    
    g = [math.inf] * (len(M.intersections) + 1) 
    g[start] = 0
     
    # f references "value" of g(intersection) + calculate_distance(intersection, goal) 
    f = dict()  
    f[start] = calculate_distance(M, start, goal)
    
    while len(openset) > 0:
        (current, g_cost) = heapq.heappop(openset)
       
        if current == goal:
            return a_star_search_path(came_from, current)
        
        closedset.add(current)  # cite 2
        
        for neighbor in M.roads[current]:   
            
            distance_cost = g_cost + calculate_distance(M, current, neighbor)
            heuristic = calculate_distance(M, neighbor, goal)
            f[neighbor] = g[neighbor] + heuristic
            
            print('distance_cost', distance_cost)
            print('f[neighbor] =: ', g[neighbor], heuristic)
            print('openset: ', openset)
            print('g: ', g)
            print('f: ', f)
            print('came_from: ', came_from)
            print('closedset: ', closedset)
            
            if neighbor in openset and distance_cost < g[neighbor]: 
                openset.remove(neighbor)
                g[neighbor] = distance_cost
            elif neighbor in closedset and distance_cost < g[neighbor]:
                closedset.remove(neighbor)
                g[neighbor] = distance_cost
            elif neighbor not in openset and neighbor not in closedset:
                g[neighbor] = distance_cost
                heapq.heappush(openset, (neighbor, f[neighbor]))
                came_from[neighbor] = current
                
    return False

def a_star_search_path(came_from, current): # cite 3
    path = []
    while current in came_from.keys():
        current = came_from[current]
        path.append(current)
    return path

def calculate_distance(M, intersection1, intersection2):
    current_x_y = M.intersections[intersection1]
    neighbor_x_y = M.intersections[intersection2]
    
    return math.sqrt(sum( [ (a - b) ** 2 for a, b in zip(current_x_y, neighbor_x_y) ] )) # cite 1
    

# Citations: 
# 1: https://www.w3resource.com/python-exercises/python-basic-exercise-40.php
# 2: http://theory.stanford.edu/~amitp/GameProgramming/ImplementationNotes.html
# 3: https://en.wikipedia.org/wiki/A*_search_algorithm
