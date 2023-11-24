'''This code implements and tests a simple version of Dijkstra's pathfinding algorithm. The Pygame component has been removed to focus solely on the logic of the algorithm.
'''
from queue import PriorityQueue

'''This function creates a grid represented as a dictionary. Each key is a tuple (row, col) representing a cell in the grid, and the value is a list of neighboring cells that can be reached from that cell. Cells that are not barriers have their neighbors calculated and stored.
The neighbors are determined based on the cardinal directions (up, down, left, right) and are only added if they are within the grid boundaries and not in the list of barriers.'''
def create_simple_grid(grid_size, barriers):
    grid = {}
    for row in range(grid_size):
        for col in range(grid_size):
            grid[(row, col)] = []  # Initialize each cell with an empty list

    for row in range(grid_size):
        for col in range(grid_size):
            if (row, col) not in barriers:
                neighbors = []
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    neighbor = (row + dx, col + dy)
                    if 0 <= neighbor[0] < grid_size and 0 <= neighbor[1] < grid_size:
                        neighbors.append(neighbor)
                grid[(row, col)] = neighbors
    return grid

'''This is the core function implementing Dijkstra's algorithm. It takes the grid, a start node, and an end node as arguments.
The algorithm uses a priority queue (open_set) to efficiently find the next node to process. It keeps track of the shortest distance to each node (g_score) and how each node was reached (came_from).
As the algorithm runs, it updates these data structures. When the end node is reached, the function reconstructs and returns the path from the start node to the end node by backtracking through the came_from dictionary.'''
def dijkstra(grid, start, end):
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {node: float('inf') for node in grid}
    g_score[start] = 0

    while not open_set.empty():
        current = open_set.get()[1]

        if current == end:
            path = []
            while current != start:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor in grid[current]:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                open_set.put((g_score[neighbor], neighbor))

    return None
'''This function tests the Dijkstra's algorithm.
A 5x5 grid is created with specified barrier locations. The start and end points are set at opposite corners of the grid.
The algorithm is then run on this grid, and the path it finds is compared to an expected_path.'''
def test_dijkstra():
    grid_size = 5
    barriers = [(1, 1), (1, 2), (1, 3), (3, 1), (3, 2), (3, 3)]
    grid = create_simple_grid(grid_size, barriers)

    start = (0, 0)
    end = (4, 4)
    path = dijkstra(grid, start, end)

    expected_path = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]
    assert path == expected_path, f"Path does not match expected path. Found: {path}"

    print("Test passed: Path matches expected path.")

test_dijkstra()




