import pygame
from spot import Spot

class Grid:
    def __init__(self, rows, width):
        self.rows = rows
        self.width = width
        self.gap = width // rows
        self.grid = self._initialize_grid()

    def _initialize_grid(self):
        return [[Spot(i, j, self.gap, self.rows) for j in range(self.rows)] for i in range(self.rows)]

    def draw_grid(self, window):
        window.fill((255, 255, 255))  # White background
        self._draw_all_spots(window)
        self._draw_grid_lines(window)

    def _draw_all_spots(self, window):
        for row in self.grid:
            for spot in row:
                spot.draw(window)

    def _draw_grid_lines(self, window):
        for i in range(self.rows):
            pygame.draw.line(window, (128, 128, 128), (0, i * self.gap), (self.width, i * self.gap))
            pygame.draw.line(window, (128, 128, 128), (i * self.gap, 0), (i * self.gap, self.width))

    def handle_click(self, position):
        row, col = position[1] // self.gap, position[0] // self.gap
        return self.grid[row][col]

    def reset_grid(self):
        for row in self.grid:
            for spot in row:
                spot.reset()

    def update_grid_neighbors(self):
        for row in self.grid:
            for spot in row:
                spot.update_neighbors(self.grid)
