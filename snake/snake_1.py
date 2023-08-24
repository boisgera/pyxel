import random
import pyxel

snake_geometry = [
    [10, 15],
    [11, 15],
    [12, 15],
]

snake_direction = [1, 0]
fruit = [10, 10]
score = 0


def update():
    global snake_geometry, snake_direction, fruit, score

    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

    if pyxel.btnp(pyxel.KEY_DOWN):
        snake_direction = [0, 1]
    elif pyxel.btnp(pyxel.KEY_UP):
        snake_direction = [0, -1]
    elif pyxel.btnp(pyxel.KEY_LEFT):
        snake_direction = [-1, 0]
    elif pyxel.btnp(pyxel.KEY_RIGHT):
        snake_direction = [1, 0]

    head = snake_geometry[-1]
    new_head = [head[0] + snake_direction[0], head[1] + snake_direction[1]]
    if (
        new_head in snake_geometry
        or new_head[0] < 0
        or new_head[0] >= 30
        or new_head[1] < 0
        or new_head[1] >= 30
    ):
        pyxel.quit()
    if new_head == fruit:
        score = score + 1
        snake_geometry = snake_geometry + [new_head]
        fruit = [random.randint(0, 29), random.randint(0, 29)]
    else:
        snake_geometry = snake_geometry[1:] + [new_head]


def draw():
    pyxel.cls(7)
    for x, y in snake_geometry:
        pyxel.rect(x * 20, y * 20, 20, 20, 3)
    pyxel.rect(fruit[0] * 20, fruit[1] * 20, 20, 20, 8)


pyxel.init(width=600, height=600, title="🐍 Snake Game", fps=5)
pyxel.run(update, draw)
