from queue import Queue
''' The bfs function implements the breadth-first search algorithm to find a path from the start node to the end node in a given grid. The pygame component has been removed and this focuses mainly on implementing the logic used for the visualization earlier. 
We use a queue to explore nodes in a breadth-first manner, and dictionaries came_from and visited to track the path and visited nodes.'''
def bfs(grid, start, end):
    q = Queue()
    q.put(start)
    came_from = {}
    visited = {start}

    while not q.empty():
        current = q.get()

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor in grid[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.put(neighbor)
                came_from[neighbor] = current

    return None

'''The test_bfs function defines a simple grid, calls the bfs function to find a path, and checks if the obtained path matches the expected path.'''
def test_bfs():
    grid = {
        (0, 0): [(0, 1), (1, 0)],
        (0, 1): [(0, 0), (1, 1)],
        (1, 0): [(0, 0), (1, 1)],
        (1, 1): [(0, 1), (1, 0)],
    }

    start = (0, 0)
    end = (1, 1)

    path = bfs(grid, start, end)

    expected_path = [(0, 0), (0, 1), (1, 1)]

    assert path == expected_path, f"Path does not match expected path. Found: {path}"

    print("Test passed: Path matches expected path.")

test_bfs()
