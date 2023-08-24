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


class Game:
    def __init__(self, snake, fruit, score):
        self.snake = snake
        self.fruit = fruit
        self.score = score
        pyxel.init(WIDTH * CELL_LENGTH, HEIGHT * CELL_LENGTH, fps=FPS)
        pyxel.run(self.update, self.draw)

    def handle_events(self):
        snake = self.snake
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_DOWN):
            snake.direction = DOWN
        elif pyxel.btnp(pyxel.KEY_UP):
            snake.direction = UP
        elif pyxel.btnp(pyxel.KEY_LEFT):
            snake.direction = LEFT
        elif pyxel.btnp(pyxel.KEY_RIGHT):
            snake.direction = RIGHT

    def move_snake(self):
        snake = self.snake
        head = snake.head
        new_head = [
            head[0] + snake.direction[0],
            head[1] + snake.direction[1],
        ]
        if (
            new_head in snake.geometry
            or new_head[0] < 0
            or new_head[0] >= WIDTH
            or new_head[1] < 0
            or new_head[1] >= HEIGHT
        ):
            pyxel.quit()
        if new_head == self.fruit:
            self.score = self.score + 1
            snake.geometry = snake.geometry + [new_head]
            self.fruit = [random.randint(0, 29), random.randint(0, 29)]
        else:
            snake.geometry = snake.geometry[1:] + [new_head]

    def update(self):
        self.handle_events()
        self.move_snake()

    def draw(self):
        snake = self.snake
        pyxel.cls(BRIGHT_GREY)
        for x, y in snake.geometry:
            pyxel.rect(x * 20, y * 20, 20, 20, VIRIDIAN_GREEN)
        pyxel.rect(self.fruit[0] * 20, self.fruit[1] * 20, 20, 20, DOGWOOD_ROSE)


game = Game(
    snake=Snake(geometry=[[10, 15], [11, 15], [12, 15]], direction=RIGHT),
    fruit=[10, 10],
    score=0,
)
