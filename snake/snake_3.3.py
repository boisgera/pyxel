# Pyxel
import pyxel


# Constants
WIDTH, HEIGHT = 30, 30
CELL_SIZE = 20
FPS = 10
BRIGHT_GREY = 7
VIRIDIAN_GREEN = 3
DOGWOOD_ROSE = 8
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


def draw_cells(cells):
    h = CELL_SIZE
    for x, y in cells:
        pyxel.rect(x * h, y * h, h, h, VIRIDIAN_GREEN)


def draw_path(path):
    h = CELL_SIZE
    for x, y in path:
        pyxel.rect(x * h, y * h, h, h, DOGWOOD_ROSE)


def display_maze(maze, cells=None, path=None):
    pyxel.init(WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE, fps=FPS)

    def draw():
        draw_background()
        draw_walls(maze)
        if cells is not None:
            draw_cells(cells)
        if path is not None:
            draw_path(path)

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
display_maze(random_maze, path=path)
