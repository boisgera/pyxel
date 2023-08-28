import pyxel

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw():
    pyxel.cls(0)
    for i in range(40):
        for j in range(20):
            pyxel.text(i*4, j*6, "X", 1)
    pyxel.text(56, 54, "Hello Snake!", pyxel.frame_count % 16)


pyxel.init(160, 120, title="🐍 Snake")
pyxel.run(update, draw)
