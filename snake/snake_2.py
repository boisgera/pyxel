import random
import pyxel

# Settings
# ------------------------------------------------------------------------------

# ## Geometry
WIDTH = HEIGHT = 30
CELL_LENGTH = 20

# ## Frames per second
FPS = 5

# # Constants
#
# ## Colors
# Sources:
#   - https://kitao.github.io/pyxel/wasm/examples/05_color_palette.html
#   - https://www.color-name.com/
BLACK = 0
VIRIDIAN_GREEN = 3
BRIGHT_GREY = 7
DOGWOOD_ROSE = 8

# Geometry
WIDTH = HEIGHT = 30
CELL_LENGTH = 20

UP = [0, -1]
DOWN = [0, 1]
LEFT = [-1, 0]
RIGHT = [1, 0]


## Game State
snake_geometry = [
    [10, 15],
    [11, 15],
    [12, 15],
]

snake_direction = [1, 0]
fruit = [10, 10]
score = 0


def handle_events():
    global snake_direction

    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

    if pyxel.btnp(pyxel.KEY_DOWN):
        snake_direction = DOWN
    elif pyxel.btnp(pyxel.KEY_UP):
        snake_direction = UP
    elif pyxel.btnp(pyxel.KEY_LEFT):
        snake_direction = LEFT
    elif pyxel.btnp(pyxel.KEY_RIGHT):
        snake_direction = RIGHT


def move_snake():
    global snake_geometry, fruit, score

    head = snake_geometry[-1]
    new_head = [head[0] + snake_direction[0], head[1] + snake_direction[1]]
    if (
        new_head in snake_geometry
        or new_head[0] < 0
        or new_head[0] >= WIDTH
        or new_head[1] < 0
        or new_head[1] >= HEIGHT
    ):
        pyxel.quit()
    if new_head == fruit:
        score = score + 1
        snake_geometry = snake_geometry + [new_head]
        fruit = [random.randint(0, 29), random.randint(0, 29)]
    else:
        snake_geometry = snake_geometry[1:] + [new_head]


def update():
    handle_events()
    move_snake()


def draw():
    pyxel.cls(BRIGHT_GREY)
    for x, y in snake_geometry:
        pyxel.rect(x * 20, y * 20, 20, 20, VIRIDIAN_GREEN)
    pyxel.rect(fruit[0] * 20, fruit[1] * 20, 20, 20, DOGWOOD_ROSE)


pyxel.init(
    width=WIDTH * CELL_LENGTH,
    height=HEIGHT * CELL_LENGTH,
    title="🐍 Snake Game",
    fps=FPS,
)
pyxel.run(update, draw)
