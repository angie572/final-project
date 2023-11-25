import pygame
from algorithms.a_star import a_star
from algorithms.dijkstra import dijkstra
from algorithms.bfs import bfs
pygame.init()

class Grid:
    """
    - Manages the entire grid where the pathfinding takes place.
    - Responsible for initializing the grid with spots (nodes), drawing it, and handling user interactions.

    Methods:
    - __init__: Initializes the grid with given dimensions.
    - make_grid: Fills the grid with spot objects.
    - draw: Renders the grid and its spots on the Pygame window.
    - get_clicked_pos: Translates pixel coordinates to grid coordinates.
    - reset: Resets the grid to its initial state, with an option to clear barriers.
    - clear_path: Clears the path after an algorithm has run.
    - update_neighbors: Updates the neighbors for each spot in the grid based on the current grid state.
    """
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

    def reset(self, clear_barriers=False):
        for row in self.grid:
            for spot in row:
                if clear_barriers or not spot.is_barrier():
                    spot.reset()

    def clear_path(self):
        for row in self.grid:
            for spot in row:
                if spot.is_closed() or spot.is_open() or spot.is_path():
                    spot.reset()

    def update_neighbors(self):
        for row in self.grid:
            for spot in row:
                spot.update_neighbors(self.grid)


import pygame

class Spot:
    """
    - Represents each cell/node in the grid.
    - Manages the properties of each spot like its position, color, and its neighbors.

    Methods:
    - __init__: Initializes a spot with its row, column, width, and total rows.
    - State Check Methods (is_closed, is_open, is_barrier, etc.): Check the current state of the spot.
    - State Update Methods (make_start, make_closed, make_open, etc.): Update the state of the spot.
    - draw: Draws the spot on the Pygame window.
    - update_neighbors: Determines and updates neighboring spots based on grid layout and current state.
    """
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = (255, 255, 255)  
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == (205, 92, 92)  # Indian Red

    def is_open(self):
        return self.color == (60, 179, 113)  # Medium Sea Green

    def is_barrier(self):
        return self.color == (47, 79, 79)  # Dark Slate Gray

    def is_start(self):
        return self.color == (255, 215, 0)  # Gold

    def is_end(self):
        return self.color == (100, 149, 237)  # Cornflower Blue

    def reset(self):
        self.color = (200, 200, 200)  # Light Grey

    def make_start(self): self.color = (255, 215, 0)  # Gold
    def make_closed(self): self.color = (205, 92, 92)  # Indian Red
    def make_open(self): self.color = (60, 179, 113)  # Medium Sea Green
    def make_barrier(self): self.color = (47, 79, 79)  # Dark Slate Gray
    def make_end(self): self.color = (100, 149, 237)  # Cornflower Blue
    def make_path(self): self.color = (218, 165, 32)  # Golden Rod

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # DOWN, UP, RIGHT, LEFT

        for dx, dy in directions:
            row, col = self.row + dx, self.col + dy
            if 0 <= row < self.total_rows and 0 <= col < self.total_rows:
                neighbor = grid[row][col]
                if not neighbor.is_barrier():
                    self.neighbors.append(neighbor)


def draw_text(win, text, position, font, color=(0, 0, 0)):
    """
    - Utility function for rendering text on the Pygame window.
    - Takes in the window object, text, position, font, and color for the text.
    """
    text_surface = font.render(text, True, color)
    win.blit(text_surface, position)

def main(win, width, rows):
    """
    - The central function of the application where the Pygame loop is managed.
    - Handles user interactions, algorithm selection, and execution of pathfinding algorithms.

    Process:
    - Initializes the grid and manages user inputs for setting start, end, and barriers.
    - Listens for key presses to select and execute the chosen algorithm.
    - Displays the results of the algorithm once executed.
    - Handles application events like quitting, resetting, and clearing the path.
    """
    grid = Grid(rows, width)
    start = None
    end = None
    run = True
    started = False
    algorithm = None
    algorithm_result = None

    while run:
        draw(win, grid)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if started:
                continue

            if pygame.mouse.get_pressed()[0]:  # Left mouse button
                pos = pygame.mouse.get_pos()
                row, col = grid.get_clicked_pos(pos)
                spot = grid.grid[row][col]
                if not start and spot != end:
                    start = spot
                    start.make_start()
                elif not end and spot != start:
                    end = spot
                    end.make_end()
                elif spot != end and spot != start:
                    spot.make_barrier()

            elif pygame.mouse.get_pressed()[2]:  # Right mouse button
                pos = pygame.mouse.get_pos()
                row, col = grid.get_clicked_pos(pos)
                spot = grid.grid[row][col]
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    algorithm = a_star
                    print("Selected algorithm: A*")
                elif event.key == pygame.K_d:
                    algorithm = dijkstra
                    print("Selected algorithm: Dijkstra's")
                elif event.key == pygame.K_b:
                    algorithm = bfs
                    print("Selected algorithm: Breadth First Search (BFS)")
                elif event.key == pygame.K_SPACE and start and end and not started and algorithm:
                    started = True
                    for row in grid.grid:
                        for spot in row:
                            spot.update_neighbors(grid.grid)

                    # Store the results from the algorithm
                    algorithm_result = algorithm(lambda: draw(win, grid), grid.grid, start, end)
                    started = False
                    # Display the results
                    draw_results(win, algorithm_result)
                elif event.key == pygame.K_c:
                    if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                        grid.reset(clear_barriers=True)
                    else:
                        grid.clear_path()
                    start = None
                    end = None
                    started = False
                    algorithm = None

    pygame.quit()

def draw_results(win, results):
    """
    - Displays the pathfinding results on the Pygame window.
    - Shows pathfinding statistic like time taken, nodes visited, and path length.
    """
    if results:
        time_taken, nodes_visited, path_length = results  
        if time_taken is not None and nodes_visited is not None and path_length is not None:
            font = pygame.font.SysFont(None, 24)
            draw_text(win, f"Time taken: {time_taken:.2f} seconds", (10, WIDTH + 10), font)
            draw_text(win, f"Nodes visited: {nodes_visited}", (10, WIDTH + 35), font)
            draw_text(win, f"Path length: {path_length}", (10, WIDTH + 60), font)  
        pygame.display.update()



def draw(win, grid):
    """
    - Responsible for updating the Pygame window with the current state of the grid.
    - Calls the draw method of the grid object to render its current state.
    """
    win.fill((255, 255, 255))
    grid.draw(win)
    pygame.display.update()

# Pygame window setup
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Pathfinding Visualizer")
main(WIN, WIDTH, 50)
