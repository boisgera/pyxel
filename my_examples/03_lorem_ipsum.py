import pyxel

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

LOREM_IPSUM = """Lorem ipsum dolor sit amet, consectetur 
adipiscing elit, sed do eiusmod tempor 
incididunt ut labore et dolore magna 
aliqua. 
Ut enim ad minim veniam, quis nostrud 
exercitation ullamco laboris nisi ut 
aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit 
in voluptate velit esse cillum dolore eu 
fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non 
proident, sunt in culpa qui officia 
deserunt mollit anim id est laborum.
"""

def draw():
    pyxel.cls(0)
    pyxel.text(0, 0, LOREM_IPSUM, 1)
    pyxel.text(56, 54, "Hello Snake!", pyxel.frame_count % 16)


pyxel.init(160, 120, title="🐍 Snake")
pyxel.run(update, draw)
