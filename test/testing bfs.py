from queue import Queue

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

def test_bfs():
    # Define a simple grid
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
