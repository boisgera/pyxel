# Python Standard Library
import math

# Pyxel
import pyxel

import numpy as np
import matplotlib.cm


# Constants
WIDTH, HEIGHT = 30, 30
CELL_SIZE = 20
BRIGHT_GREY = 7
VIRIDIAN_GREEN = 3
DOGWOOD_ROSE = 8
BLACK = 0
FPS = 5


# TODO: assign 8 named colors, 8 for the colormap
def make_new_colormap():
    global BLACK, BRIGHT_GREY, DOGWOOD_ROSE, VIRIDIAN_GREEN

    old_palette = pyxel.colors.to_list()

    # Keep the 8 one you like or create new ones
    new_palette = 8 * [0]
    new_palette[BLACK:=0] = old_palette[BLACK]
    new_palette[BRIGHT_GREY:=1] = old_palette[BRIGHT_GREY]
    new_palette[VIRIDIAN_GREEN:=2] = old_palette[VIRIDIAN_GREEN]
    new_palette[DOGWOOD_ROSE:=3] = old_palette[DOGWOOD_ROSE]
    ...

    # Use the viridis colormap to create 8 new colors
    viridis_8_rgb_samples = matplotlib.cm.viridis(np.linspace(0, 1, 8))
    for rgb in viridis_8_rgb_samples:
        r, g, b, _ = [round(x * 255) for x in rgb]
        new_palette.append(r << 16 | g << 8 | b)
    pyxel.colors.from_list(new_palette)


def color_index(x):
    x = np.clip(x, 0.0, 1.0)
    return int(x * 7) + 8


def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()


def draw_background():
    pyxel.cls(BLACK)


def draw_walls(maze):
    h = CELL_SIZE
    for x, y in maze:
        pyxel.rect(x * h, y * h, h, h, BRIGHT_GREY)


def maze_to_graph(maze):
    vertices = set(maze)
    edges = set()
    weights = {}
    for vertex in vertices:
        x, y = vertex
        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            neighbor = (x + dx, y + dy)
            if neighbor in vertices:
                edge = (vertex, neighbor)
                edges.add(edge)
                weights[edge] = 1
    return (vertices, edges, weights)


def reachable_cells(maze, source):
    vertices, edges, _ = maze_to_graph(maze)
    todo = {source}
    done = set()
    while todo:
        current = todo.pop()
        neighbors = {v for v in vertices if (current, v) in edges}
        for n in neighbors:
            if n not in done:
                todo.add(n)
        done.add(current)
    return done


def path_from(maze, source):
    vertices, edges, _ = maze_to_graph(maze)
    todo = set()
    done = set()
    path = {}
    if source in maze:
        todo.add(source)
        path[source] = [source]
    while todo:
        current = todo.pop()
        neighbors = {v for v in vertices if (current, v) in edges}
        for n in neighbors:
            if n not in done and n not in todo:
                path[n] = path[current] + [n]
                todo.add(n)
        done.add(current)
    return path


import math


def shortest_path_from(maze, source):
    vertices, edges, weight = maze_to_graph(maze)
    distance, path = {}, {}
    todo = {source}
    distance[source] = 0
    path[source] = [source]
    while todo:
        current = todo.pop()
        neighbors = {v for v in vertices if (current, v) in edges}
        for n in neighbors:
            d = distance[current] + weight[(current, n)]
            if d < distance.get(n, math.inf):
                distance[n] = d
                path[n] = path[current] + [n]
                todo.add(n)
    return path


def draw_cells(cells):
    h = CELL_SIZE
    for x, y in cells:
        pyxel.rect(x * h, y * h, h, h, VIRIDIAN_GREEN)


def draw_path(path):
    h = CELL_SIZE
    for x, y in path:
        pyxel.rect(x * h, y * h, h, h, DOGWOOD_ROSE)


def draw_map(map):
    h = CELL_SIZE
    v_max = max(v for v in map.values())
    for (x, y), v in map.items():
        pyxel.rect(x * h, y * h, h, h, color_index(float(v / v_max)))


def display_maze(maze, cells=None, path=None, map=None):
    pyxel.init(WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE, fps=FPS)
    make_new_colormap()

    def draw():
        draw_background()
        draw_walls(maze)
        if cells is not None:
            draw_cells(cells)
        if path is not None:
            draw_path(path)
        if map is not None:
            draw_map(map)

    pyxel.run(update, draw)


filename = "mazes/random-maze.py"
file = open(filename, mode="rt", encoding="utf-8")
random_maze_repr = file.read()
file.close()
random_maze = eval(random_maze_repr)

TOP_LEFT = (0, 0)
cells = reachable_cells(random_maze, source=TOP_LEFT)
target_to_path = path_from(random_maze, TOP_LEFT)
BOTTOM_RIGHT = (WIDTH - 1, HEIGHT - 1)
path = target_to_path[BOTTOM_RIGHT]
map = {target: len(path) - 1 for target, path in target_to_path.items()}
display_maze(random_maze, map=map)
