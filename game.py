import pygame
import random

# Initialize Pygame
pygame.font.init()

# Global Constants
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
GRID_WIDTH = SCREEN_WIDTH // BLOCK_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // BLOCK_SIZE

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# Shapes format
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
]

SHAPES_COLORS = [CYAN, YELLOW, BLUE, GREEN, RED, ORANGE, MAGENTA]

class Tetris:
    def __init__(self):
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece = self.new_piece()
        self.next_piece = self.new_piece()
        self.current_position = [0, GRID_WIDTH // 2 - 1]
        self.score = 0

    def new_piece(self):
        index = random.randint(0, len(SHAPES) - 1)
        return SHAPES[index], SHAPES_COLORS[index]

    def rotate(self):
        self.current_piece[0] = [list(row) for row in zip(*self.current_piece[0][::-1])]

    def valid_move(self, offset):
        for i, row in enumerate(self.current_piece[0]):
            for j, value in enumerate(row):
                if value:
                    x = self.current_position[0] + i + offset[0]
                    y = self.current_position[1] + j + offset[1]
                    if x < 0 or x >= GRID_HEIGHT or y < 0 or y >= GRID_WIDTH or (x >= 0 and self.grid[x][y]):
                        return False
        return True

    def merge_piece(self):
        for i, row in enumerate(self.current_piece[0]):
            for j, value in enumerate(row):
                if value:
                    self.grid[self.current_position[0] + i][self.current_position[1] + j] = self.current_piece[1]

    def clear_lines(self):
        lines_cleared = 0
        for i in range(GRID_HEIGHT - 1, -1, -1):
            if all(self.grid[i]):
                del self.grid[i]
                self.grid.insert(0, [0 for _ in range(GRID_WIDTH)])
                lines_cleared += 1
        self.score += lines_cleared

    def drop(self):
        if self.valid_move((1, 0)):
            self.current_position[0] += 1
        else:
            self.merge_piece()
            self.clear_lines()
            self.current_piece = self.next_piece
            self.next_piece = self.new_piece()
            self.current_position = [0, GRID_WIDTH // 2 - 1]
            if not self.valid_move((0, 0)):
                return False
        return True


def draw_grid(surface, grid):
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value:
                pygame.draw.rect(surface, value, (j * BLOCK_SIZE, i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame