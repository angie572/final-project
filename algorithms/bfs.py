import pygame
from queue import Queue
import time

def bfs(draw, grid, start, end):
    start_time = time.time()  # Start timer
    q = Queue()
    q.put(start)
    came_from = {}
    visited = {start}

    nodes_traversed = 0

    while not q.empty():
        nodes_traversed += 1  # Increment nodes traversed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = q.get()

        if current == end:
            path_length = reconstruct_path(came_from, end, draw)
            end.make_end()
            end_time = time.time()
            print(f"Time taken: {end_time - start_time:.2f} seconds")
            print(f"Nodes traversed: {nodes_traversed}")
            print(f"Path length: {path_length}")
            return (end_time - start_time, nodes_traversed, path_length)


        for neighbor in current.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                q.put(neighbor)
                came_from[neighbor] = current
                neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    end_time = time.time()  # End timer
    #When there's no path
    print(f"Time taken: {end_time - start_time:.2f} seconds")
    print(f"Nodes traversed: {nodes_traversed}")
    print("There's no path :(")
    return (None, None, None)


def reconstruct_path(came_from, current, draw):
    """Reconstructs the path and returns its length."""
    path_length = 0
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()
        path_length += 1
    return path_length
