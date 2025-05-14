# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Tetromino colors
COLORS = {
    'I': (0, 255, 255),   # Cyan
    'O': (255, 255, 0),   # Yellow
    'T': (128, 0, 128),   # Purple
    'S': (0, 255, 0),     # Green
    'Z': (255, 0, 0),     # Red
    'J': (0, 0, 255),     # Blue
    'L': (255, 165, 0),   # Orange
}

# Game dimensions
BLOCK_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
PREVIEW_SIZE = 4

# Window dimensions
WINDOW_WIDTH = BLOCK_SIZE * (GRID_WIDTH + 8)  # Extra space for score and next piece
WINDOW_HEIGHT = BLOCK_SIZE * GRID_HEIGHT

# Game settings
FPS = 60
INITIAL_FALL_SPEED = 1.0  # Blocks per second
SPEED_INCREASE = 0.5  # Speed increase per level
LINES_PER_LEVEL = 10

# Scoring system
SCORES = {
    1: 100,    # Single line
    2: 300,    # Double line
    3: 500,    # Triple line
    4: 800,    # Tetris
} 