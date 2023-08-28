import math
import time
import pyxel


def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()


t = None


def draw():
    global t
    dt = math.inf
    if t is None:
        t = time.time()
    else:
        t_now = time.time()
        dt = t_now - t
        t = t_now
    fps = 1.0 / dt
    pyxel.cls(0)
    pyxel.text(0, 0, f"fps: {int(round(fps))}", 7)


pyxel.init(160, 120, title="🐍 Snake")
t0 = time.time()
pyxel.run(update, draw)
