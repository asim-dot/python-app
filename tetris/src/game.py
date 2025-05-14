import pygame
import sys
from typing import Optional
from board import Board
from pieces import Tetromino
from constants import (
    WINDOW_WIDTH, WINDOW_HEIGHT, BLOCK_SIZE,
    GRID_WIDTH, GRID_HEIGHT, BLACK, WHITE, GRAY,
    FPS, INITIAL_FALL_SPEED
)

class TetrisGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        
        self.board = Board()
        self.current_piece = Tetromino()
        self.next_piece = Tetromino()
        self.game_over = False
        self.paused = False
        
        # Time tracking
        self.last_fall_time = pygame.time.get_ticks()
        self.fall_speed = INITIAL_FALL_SPEED
        
    def handle_input(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_p:
                    self.paused = not self.paused
                if not self.game_over and not self.paused:
                    if event.key == pygame.K_LEFT:
                        self.current_piece.move(-1, 0, self.board.get_grid())
                    elif event.key == pygame.K_RIGHT:
                        self.current_piece.move(1, 0, self.board.get_grid())
                    elif event.key == pygame.K_DOWN:
                        self.current_piece.move(0, 1, self.board.get_grid())
                    elif event.key == pygame.K_UP:
                        self.current_piece.rotate(self.board.get_grid())
                    elif event.key == pygame.K_SPACE:
                        self._hard_drop()

    def _hard_drop(self) -> None:
        """Drop the piece to the bottom instantly."""
        while self.current_piece.move(0, 1, self.board.get_grid()):
            pass

    def update(self) -> None:
        if self.game_over or self.paused:
            return

        current_time = pygame.time.get_ticks()
        if current_time - self.last_fall_time > 1000 / self.fall_speed:
            if not self.current_piece.move(0, 1, self.board.get_grid()):
                self.board.add_piece(self.current_piece)
                lines_cleared = self.board.clear_lines()
                self.board.update_score(lines_cleared)
                
                # Update fall speed based on level
                self.fall_speed = INITIAL_FALL_SPEED + (self.board.level - 1) * 0.5
                
                # Get new piece
                self.current_piece = self.next_piece
                self.next_piece = Tetromino()
                
                # Check for game over
                if not self.current_piece._is_valid_position(self.board.get_grid()):
                    self.game_over = True
            
            self.last_fall_time = current_time

    def draw(self) -> None:
        self.screen.fill(BLACK)
        
        # Draw board grid
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                pygame.draw.rect(
                    self.screen,
                    self.board.grid[y][x],
                    (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE),
                    0
                )
                pygame.draw.rect(
                    self.screen,
                    GRAY,
                    (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE),
                    1
                )

        # Draw current piece
        for x, y in self.current_piece.get_positions():
            if y >= 0:  # Only draw if piece is visible
                pygame.draw.rect(
                    self.screen,
                    self.current_piece.color,
                    (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE),
                    0
                )

        # Draw score and level
        score_text = self.font.render(f"Score: {self.board.score}", True, WHITE)
        level_text = self.font.render(f"Level: {self.board.level}", True, WHITE)
        self.screen.blit(score_text, (GRID_WIDTH * BLOCK_SIZE + 10, 10))
        self.screen.blit(level_text, (GRID_WIDTH * BLOCK_SIZE + 10, 50))

        # Draw next piece preview
        next_text = self.font.render("Next:", True, WHITE)
        self.screen.blit(next_text, (GRID_WIDTH * BLOCK_SIZE + 10, 100))
        
        # Draw next piece
        preview_x = GRID_WIDTH * BLOCK_SIZE + 50
        preview_y = 150
        for y, row in enumerate(self.next_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(
                        self.screen,
                        self.next_piece.color,
                        (preview_x + x * BLOCK_SIZE, preview_y + y * BLOCK_SIZE,
                         BLOCK_SIZE, BLOCK_SIZE),
                        0
                    )

        # Draw game over or pause text
        if self.game_over:
            game_over_text = self.font.render("GAME OVER", True, WHITE)
            text_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            self.screen.blit(game_over_text, text_rect)
        elif self.paused:
            pause_text = self.font.render("PAUSED", True, WHITE)
            text_rect = pause_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            self.screen.blit(pause_text, text_rect)

        pygame.display.flip()

    def run(self) -> None:
        while True:
            self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = TetrisGame()
    game.run()