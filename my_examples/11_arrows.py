import pyxel

global arrow_keys

def update():
    global arrow_keys
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    arrow_keys = []
    for key in (pyxel.KEY_UP, pyxel.KEY_DOWN, pyxel.KEY_LEFT, pyxel.KEY_RIGHT):
        if pyxel.btn(key):
            arrow_keys.append(key)

def draw():
    pyxel.cls(0)
    if pyxel.KEY_UP in arrow_keys:
        color = 7
    else:
        color = 13
    pyxel.rect(10, 0, 10, 10, color)
    if pyxel.KEY_LEFT in arrow_keys:
        color = 7
    else:
        color = 13
    pyxel.rect(0, 10, 10, 10, color)
    if pyxel.KEY_DOWN in arrow_keys:
        color = 7
    else:
        color = 13
    pyxel.rect(10, 10, 10, 10, color)
    if pyxel.KEY_RIGHT in arrow_keys:
        color = 7
    else:   
        color = 13
    pyxel.rect(20, 10, 10, 10, color)

pyxel.init(30, 20)
pyxel.run(update, draw)
