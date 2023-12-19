from heapq import heappop, heappush
from string import ascii_lowercase
import numpy as np


def get_height(c):
    if c in ascii_lowercase:
        return ascii_lowercase.index(c)
    if c == "S":
        return 0
    if c == "E":
        return 25

def get_neighbors(x,y):
    for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
        tmp_x, tmp_y = x+dx,y+dy
        
        if not (0 <= tmp_x < map_height and 0 <= tmp_y < map_length):
            continue
        if get_height(height_map[tmp_x][tmp_y]) <= get_height(height_map[x][y]) + 1:
            yield tmp_x, tmp_y

def dijkstra(start, end):
    visited = [[False] * map_length for _ in range(map_height)]
    heap = [(0, start[0], start[1])]

    while True:
        steps, x, y = heappop(heap)
        if visited[x][y]:
            continue
        visited[x][y] = True
        
        if (x,y) == end:
            return steps
        
        for tmp_x, tmp_y in get_neighbors(x,y):
            heappush(heap, (steps+1, tmp_x, tmp_y))

def get_neighbors2(x,y):
    for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
        tmp_x, tmp_y = x+dx,y+dy
        
        if not (0 <= tmp_x < map_height and 0 <= tmp_y < map_length):
            continue
        if get_height(height_map[tmp_x][tmp_y]) >= get_height(height_map[x][y]) - 1:
            yield tmp_x, tmp_y

def dijkstra2(start):
    visited = [[False] * map_length for _ in range(map_height)]
    heap = [(0, start[0], start[1])]

    while True:
        steps, x, y = heappop(heap)
        if visited[x][y]:
            continue
        visited[x][y] = True
        
        if get_height(height_map[x][y]) == 0:
            return steps
        
        for tmp_x, tmp_y in get_neighbors2(x,y):
            heappush(heap, (steps+1, tmp_x, tmp_y))


with open("input/day12.txt") as f:
    lines = f.read().strip().split("\n")
height_map = []
for line in lines:
    line_arr = []
    for c in line:
        line_arr.append(c)
    height_map.append(line_arr)
map_height = len(height_map)
map_length = len(height_map[0])
np_map = np.array(height_map)
start = np.where(np_map == "S")
end = np.where(np_map == "E")
start = (start[0][0], start[1][0])
end = (end[0][0], end[1][0])

# Part 1
# Dijkstra's algorithm
print(dijkstra(start, end))

# Part 2
print(dijkstra2(end))