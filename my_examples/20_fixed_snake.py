import pyxel
import random

fruit = [
    random.randint(0, 29), 
    random.randint(0, 29)
]

snake_geometry = [
    [10, 15],
    [11, 15],
    [12, 15],
]

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw():
    pyxel.cls(13)
    for i in range(30):
        for j in range(30):
            if (i+j) % 2 == 0:
                pyxel.pset(i, j, 7) 
    pyxel.pset(fruit[0], fruit[1], 8)
    for x, y in snake_geometry[:-1]:
        pyxel.pset(x, y, 3)
    head = snake_geometry[-1]
    pyxel.pset(head[0], head[1], 11)

pyxel.init(30, 30)
pyxel.run(update, draw)