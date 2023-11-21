import pygame
from algorithms.a_star import a_star
from algorithms.dijkstra import dijkstra

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

def main(win, width, rows):
    grid = Grid(rows, width)
    start = None
    end = None
    run = True
    started = False
    algorithm = None  # To store the chosen algorithm

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

                if event.key == pygame.K_d:
                    algorithm = dijkstra

                if event.key == pygame.K_SPACE and start and end and not started and algorithm:
                    started = True
                    for row in grid.grid:
                        for spot in row:
                            spot.update_neighbors(grid.grid)

                    algorithm(lambda: draw(win, grid), grid.grid, start, end)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    started = False
                    algorithm = None
                    grid.reset()

    pygame.quit()

def draw(win, grid):
    win.fill((255, 255, 255))
    grid.draw(win)
    pygame.display.update()

# Pygame window setup
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Pathfinding Visualizer")
main(WIN, WIDTH, 50)