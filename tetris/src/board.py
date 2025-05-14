from typing import List, Tuple
from constants import GRID_WIDTH, GRID_HEIGHT, BLACK

class Board:
    def __init__(self):
        self.grid = [[BLACK for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.score = 0
        self.level = 1
        self.lines_cleared = 0

    def add_piece(self, piece) -> None:
        """Add a piece to the board permanently."""
        for x, y in piece.get_positions():
            if y >= 0:  # Only add if piece is visible on board
                self.grid[y][x] = piece.color

    def is_line_full(self, y: int) -> bool:
        """Check if a line is completely filled."""
        return all(color != BLACK for color in self.grid[y])

    def clear_lines(self) -> int:
        """Clear all full lines and return the number of lines cleared."""
        lines_cleared = 0
        y = GRID_HEIGHT - 1
        while y >= 0:
            if self.is_line_full(y):
                # Move all lines above down
                for move_y in range(y, 0, -1):
                    self.grid[move_y] = self.grid[move_y - 1][:]
                # Clear top line
                self.grid[0] = [BLACK for _ in range(GRID_WIDTH)]
                lines_cleared += 1
            else:
                y -= 1
        return lines_cleared

    def update_score(self, lines_cleared: int) -> None:
        """Update score based on lines cleared."""
        if lines_cleared > 0:
            self.lines_cleared += lines_cleared
            self.level = (self.lines_cleared // 10) + 1
            # Score calculation based on number of lines cleared
            points = {1: 100, 2: 300, 3: 500, 4: 800}
            self.score += points.get(lines_cleared, 0) * self.level

    def is_game_over(self) -> bool:
        """Check if the game is over (blocks in the top row)."""
        return any(color != BLACK for color in self.grid[0])

    def get_grid(self) -> List[List[Tuple[int, int, int]]]:
        """Return the current grid state."""
        return self.grid