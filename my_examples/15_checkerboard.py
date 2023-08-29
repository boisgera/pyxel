import pyxel

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw():
    pyxel.cls(13)
    for i in range(30):
        for j in range(30):
            if (i+j) % 2 == 0:
                pyxel.pset(i, j, 7) 

pyxel.init(30, 30)
pyxel.run(update, draw)