import copy
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
import copy


class Snake:
    def __init__(self, geometry, direction):
        self.direction = direction
        self.geometry = geometry

    def get_direction(self):
        return copy.deepcopy(self._direction)

    def set_direction(self, direction):
        self._direction = copy.deepcopy(direction)

    direction = property(get_direction, set_direction)

    def get_geometry(self):
        return copy.deepcopy(self._geometry)

    def set_geometry(self, geometry):
        self._geometry = copy.deepcopy(geometry)

    geometry = property(get_geometry, set_geometry)

    def get_head(self):
        return self.geometry[-1]

    head = property(get_head)


class State:
    def __init__(self, snake, fruit, score):
        self.snake = snake
        self.fruit = fruit
        self.score = score


state = State(
    snake=Snake(geometry=[[10, 15], [11, 15], [12, 15]], direction=RIGHT),
    fruit=[10, 10],
    score=0,
)


def handle_events():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

    if pyxel.btnp(pyxel.KEY_DOWN):
        state.snake.direction = DOWN
    elif pyxel.btnp(pyxel.KEY_UP):
        state.snake.direction = UP
    elif pyxel.btnp(pyxel.KEY_LEFT):
        state.snake.direction = LEFT
    elif pyxel.btnp(pyxel.KEY_RIGHT):
        state.snake.direction = RIGHT


def move_snake():
    head = state.snake.head
    new_head = [head[0] + state.snake.direction[0], head[1] + state.snake.direction[1]]
    if (
        new_head in state.snake.geometry
        or new_head[0] < 0
        or new_head[0] >= WIDTH
        or new_head[1] < 0
        or new_head[1] >= HEIGHT
    ):
        pyxel.quit()
    if new_head == state.fruit:
        state.score = state.score + 1
        state.snake.geometry = state.snake.geometry + [new_head]
        state.fruit = [random.randint(0, 29), random.randint(0, 29)]
    else:
        state.snake.geometry = state.snake.geometry[1:] + [new_head]


def update():
    handle_events()
    move_snake()


def draw():
    pyxel.cls(BRIGHT_GREY)
    for x, y in state.snake.geometry:
        pyxel.rect(x * 20, y * 20, 20, 20, VIRIDIAN_GREEN)
    pyxel.rect(state.fruit[0] * 20, state.fruit[1] * 20, 20, 20, DOGWOOD_ROSE)


pyxel.init(
    width=WIDTH * CELL_LENGTH,
    height=HEIGHT * CELL_LENGTH,
    title="🐍 Snake Game",
    fps=FPS,
)
pyxel.run(update, draw)
