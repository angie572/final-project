from heapq import heappush, heappop
'''This is a simple implementation of the astar algorithm from which the pycharm component has been removed while the logic of the code has still been maintaned.'''
def manhattan_distance(point1, point2):
    """Calculate Manhattan distance."""
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)

def a_star(grid, start, end):
    count = 0
    open_set = []
    heappush(open_set, (0, count, start))
    came_from = {}
    g_score = {spot: float("inf") for spot in grid}
    g_score[start] = 0
    f_score = {spot: float("inf") for spot in grid}
    f_score[start] = manhattan_distance(start, end)

    while open_set:
        current = heappop(open_set)[2]

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor in grid[current]:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + manhattan_distance(neighbor, end)
                if neighbor not in open_set:
                    count += 1
                    heappush(open_set, (f_score[neighbor], count, neighbor))

    return None

''' The test_a_star function defines a simple 2D grid of tuples, calls the a_star function to find a path, checks if the obtained path matches the expected path, and prints a message accordingly'''
def test_a_star():
    grid = {
        (0, 0): [(0, 1), (1, 0)],
        (0, 1): [(0, 0), (1, 1)],
        (1, 0): [(0, 0), (1, 1)],
        (1, 1): [(0, 1), (1, 0)],
    }

    start = (0, 0)
    end = (1, 1)

    path = a_star(grid, start, end)

    expected_path = [(0, 0), (0, 1), (1, 1)]

    assert path == expected_path, f"Path does not match expected path. Found: {path}"

    print("Test passed: Path matches expected path.")

test_a_star()

