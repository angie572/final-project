import pygame
import time
from queue import PriorityQueue

def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()

def dijkstra(draw, grid, start, end):
    start_time = time.time()  # Start the timer
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0

    open_set_hash = {start}

    nodes_traversed = 0  # Initialize node counter

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)
        nodes_traversed += 1

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            end_time = time.time()  # Stop the timer
            print(f"Time taken: {end_time - start_time:.2f} seconds")
            print(f"Nodes traversed: {nodes_traversed}")
            return (end_time - start_time, nodes_traversed)

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((g_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    #When there's no path
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.2f} seconds")
    print(f"Nodes traversed: {nodes_traversed}")
    print("There's no path :()")
    return (None, None)

class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = (255, 255, 255)  # White for empty spot
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == (255, 0, 0)  # Red for closed spot

    def is_open(self):
        return self.color == (0, 255, 0)  # Green for open spot

    def is_barrier(self):
        return self.color == (0, 0, 0)  # Black for barrier

    def is_start(self):
        return self.color == (255, 165, 0)  # Orange for start spot

    def is_end(self):
        return self.color == (128, 0, 128)  # Purple for end spot

    def reset(self):
        self.color = (255, 255, 255)  # Reset to white

    def make_start(self):
        self.color = (255, 165, 0)

    def make_closed(self):
        self.color = (255, 0, 0)

    def make_open(self):
        self.color = (0, 255, 0)

    def make_barrier(self):
        self.color = (0, 0, 0)

    def make_end(self):
        self.color = (128, 0, 128)

    def make_path(self):
        self.color = (64, 224, 208)  # Turquoise for path

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():  # DOWN
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():  # UP
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():  # RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():  # LEFT
            self.neighbors.append(grid[self.row][self.col - 1])

class Grid:
    def __init__(self, rows, width):
        self.rows = rows
        self.width = width
        self.grid = []
        self.gap = width // rows
        self.make_grid()

    def make_grid(self):
        self.grid = []
        for i in range(self.rows):
            self.grid.append([])
            for j in range(self.rows):
                spot = Spot(i, j, self.gap, self.rows)
                self.grid[i].append(spot)

    def draw(self, win):
        win.fill((255, 255, 255))  # Fill window with white
        for row in self.grid:
            for spot in row:
                spot.draw(win)

        for i in range(self.rows):
            pygame.draw.line(win, (128, 128, 128), (0, i * self.gap), (self.width, i * self.gap))
            for j in range(self.rows):
                pygame.draw.line(win, (128, 128, 128), (j * self.gap, 0), (j * self.gap, self.width))

    def get_clicked_pos(self, pos):
        y, x = pos
        row = y // self.gap
        col = x // self.gap
        return row, col

    def reset(self):
        for row in self.grid:
            for spot in row:
                spot.reset()

    def update_neighbors(self):
        for row in self.grid:
            for spot in row:
                spot.update_neighbors(self.grid)

