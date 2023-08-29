
import pyxel

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

pyxel.init(30, 30)

fruit = [
    pyxel.rndi(0, 29), 
    pyxel.rndi(0, 29)
]

def draw():
    pyxel.cls(13)
    for i in range(30):
        for j in range(30):
            if (i+j) % 2 == 0:
                pyxel.pset(i, j, 7) 
    pyxel.pset(fruit[0], fruit[1], 8)

pyxel.run(update, draw)
