import random
from typing import List, Tuple
from constants import COLORS, GRID_WIDTH

class Tetromino:
    # Define shapes for all pieces
    SHAPES = {
        'I': [
            [[0, 0, 0, 0],
             [1, 1, 1, 1],
             [0, 0, 0, 0],
             [0, 0, 0, 0]],
        ],
        'O': [
            [[1, 1],
             [1, 1]],
        ],
        'T': [
            [[0, 1, 0],
             [1, 1, 1],
             [0, 0, 0]],
        ],
        'S': [
            [[0, 1, 1],
             [1, 1, 0],
             [0, 0, 0]],
        ],
        'Z': [
            [[1, 1, 0],
             [0, 1, 1],
             [0, 0, 0]],
        ],
        'J': [
            [[1, 0, 0],
             [1, 1, 1],
             [0, 0, 0]],
        ],
        'L': [
            [[0, 0, 1],
             [1, 1, 1],
             [0, 0, 0]],
        ],
    }

    def __init__(self):
        self.shape_name = random.choice(list(self.SHAPES.keys()))
        self.shape = self.SHAPES[self.shape_name][0]
        self.color = COLORS[self.shape_name]
        self.rotation = 0
        # Starting position (centered at top)
        self.x = GRID_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self, board: List[List[Tuple[int, int, int]]]) -> bool:
        # Save current position and rotation
        old_shape = self.shape
        old_x, old_y = self.x, self.y

        # Perform rotation
        N = len(self.shape)
        self.shape = [[self.shape[N-1-j][i] for j in range(N)] for i in range(N)]

        # Check if rotation is valid
        if not self._is_valid_position(board):
            # Restore old position and rotation if invalid
            self.shape = old_shape
            self.x, self.y = old_x, old_y
            return False
        return True

    def move(self, dx: int, dy: int, board: List[List[Tuple[int, int, int]]]) -> bool:
        self.x += dx
        self.y += dy
        if not self._is_valid_position(board):
            self.x -= dx
            self.y -= dy
            return False
        return True

    def _is_valid_position(self, board: List[List[Tuple[int, int, int]]]) -> bool:
        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell:
                    abs_x, abs_y = self.x + x, self.y + y
                    if (abs_x < 0 or abs_x >= GRID_WIDTH or
                        abs_y >= len(board) or
                        (abs_y >= 0 and board[abs_y][abs_x] != (0, 0, 0))):
                        return False
        return True

    def get_positions(self) -> List[Tuple[int, int]]:
        positions = []
        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell:
                    positions.append((self.x + x, self.y + y))
        return positions