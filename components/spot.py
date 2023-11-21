import pygame

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
