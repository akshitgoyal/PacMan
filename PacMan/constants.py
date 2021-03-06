from vector import Vector2

WIDTH = 16
HEIGHT = 16
ROWS = 36
COLS = 28
SCREENSIZE = (COLS * WIDTH, ROWS * HEIGHT)

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PINK = (255, 192, 203)
TEAL = (0, 128, 128)
ORANGE = (255, 127, 0)
TRANSPARENT = (255,0,255)

# Directions
UP = Vector2(0, -1)
DOWN = Vector2(0, 1)
LEFT = Vector2(-1, 0)
RIGHT = Vector2(1, 0)
STOP = Vector2(0, 0)

