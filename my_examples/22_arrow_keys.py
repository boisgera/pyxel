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

checkerboard = False

arrow_keys = [
    pyxel.KEY_UP, 
    pyxel.KEY_DOWN, 
    pyxel.KEY_LEFT, 
    pyxel.KEY_RIGHT
]

def update():
    global checkerboard
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    if pyxel.btnp(pyxel.KEY_C):
        checkerboard = not checkerboard
    arrow_keys_pressed = []
    for key in arrow_keys:
        if pyxel.btnp(key):
            arrow_keys_pressed.append(key)
    for key in arrow_keys_pressed:
        if key == pyxel.KEY_UP:
            print("↑")
        elif key == pyxel.KEY_DOWN:
            print("↓")
        elif key == pyxel.KEY_LEFT:
            print("←")   
        elif key == pyxel.KEY_RIGHT:
            print("→")

def draw():
    pyxel.cls(7)
    if checkerboard:
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