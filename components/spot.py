import pygame

class Spot:
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
