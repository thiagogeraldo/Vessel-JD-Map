from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from collections import deque

def str_to_matrix(string):
    return [[int(char) for char in line] for line in string.strip().split('\n')]

with open('static/map/map_ascii.txt', 'r') as file:
    content = file.read()
    m = str_to_matrix(content)

matrix = str_to_matrix(content)
grid = Grid(matrix=matrix)

temp_grid = Grid(matrix=[[1] * len(matrix[0]) for _ in matrix])

def find_nearest_one(start):
    rows, cols = len(m), len(m[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([start])
    visited = set([start])
    while queue:
        x, y = queue.popleft()
        if m[x][y] == 1:
            return (x, y)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.add((nx, ny))
    return None

def add_route(l, d):
    print((46 - l[0], l[1]), (46 - d[0], d[1]))
    l = (46 - l[0], l[1])
    start = find_nearest_one(l)
    d = (46 - d[0], d[1])
    end = find_nearest_one(d)
    print(l, d)

    finder = AStarFinder()

    path, _ = finder.find_path(grid.node(start[1], start[0]), grid.node(end[1], end[0]), grid)
    prepath, _ = finder.find_path(temp_grid.node(l[1], l[0]), temp_grid.node(start[1], start[0]), temp_grid)
    postpath, _ = finder.find_path(temp_grid.node(end[1], end[0]), temp_grid.node(d[1], d[0]), temp_grid)
    print([(46 - node.y, node.x) for node in prepath + path[1:-1] + postpath])
    return [(46 - node.y, node.x) for node in prepath + path[1:-1] + postpath]