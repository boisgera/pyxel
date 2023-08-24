# Pyxel
import pyxel


# Constants
WIDTH, HEIGHT = 30, 30
CELL_SIZE = 20
FPS = 10
WHITE = 7
BLACK = 0
FPS = 5


def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()


def draw_background():
    pyxel.cls(BLACK)


def draw_walls(maze):
    h = CELL_SIZE
    for x, y in maze:
        pyxel.rect(x * h, y * h, h, h, WHITE)


def draw():
    global maze
    draw_background()
    draw_walls(maze)


def display_maze(maze_):
    global maze
    maze = maze_
    pyxel.init(WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE, fps=FPS)
    pyxel.run(update, draw)


filename = "mazes/random-maze.py"
file = open(filename, mode="rt", encoding="utf-8")
random_maze_repr = file.read()
file.close()
random_maze = eval(random_maze_repr)
display_maze(random_maze)
