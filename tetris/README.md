# Pygame Tetris

A classic implementation of Tetris using Pygame.

## Project Structure
```
tetris/
├── src/
│   ├── __init__.py
│   ├── game.py
│   ├── pieces.py
│   ├── board.py
│   └── constants.py
├── tests/
│   ├── __init__.py
│   ├── test_game.py
│   ├── test_pieces.py
│   └── test_board.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the game:
```bash
python src/game.py
```

## Game Controls

- Left Arrow: Move piece left
- Right Arrow: Move piece right
- Down Arrow: Move piece down faster
- Up Arrow: Rotate piece clockwise
- Space: Drop piece instantly
- P: Pause game
- Q: Quit game

## Running Tests

To run the tests:
```bash
pytest tests/
```

To run tests with coverage:
```bash
pytest --cov=src tests/
```

## Game Features

- Classic Tetris gameplay
- Score tracking
- Level progression
- Next piece preview
- Game over detection
- Piece rotation
- Line clearing

## Development

The game is structured into several modules:
- `game.py`: Main game loop and pygame initialization
- `pieces.py`: Tetromino pieces and their rotation logic
- `board.py`: Game board state and collision detection
- `constants.py`: Game constants and configuration 