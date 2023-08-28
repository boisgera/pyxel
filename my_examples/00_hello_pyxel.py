import pyxel

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw():
    pyxel.cls(0)
    pyxel.text(56, 54, "Hello Snake!", pyxel.frame_count % 16)


pyxel.init(160, 120, title="🐍 Snake")
pyxel.run(update, draw)
