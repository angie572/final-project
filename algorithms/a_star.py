import pygame
import time
from heapq import heappush, heappop

def manhattan_distance(point1, point2):
    """Calculate Manhattan distance."""
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)

def reconstruct_path(came_from, current, draw):
    """Reconstructs the path."""
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()

def a_star(draw, grid, start, end):
    start_time = time.time()
    nodes_traversed = 0

    count = 0
    open_set = []
    heappush(open_set, (0, count, start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = manhattan_distance(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while open_set:
        current = heappop(open_set)[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            end_time = time.time()
            print(f"Time taken: {end_time - start_time:.2f} seconds")
            print(f"Nodes traversed: {nodes_traversed}")
            return (end_time - start_time, nodes_traversed)

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + manhattan_distance(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    heappush(open_set, (f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()
        nodes_traversed += 1

    print("There's no path :(")
    return (None, None)
