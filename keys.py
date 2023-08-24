import pyxel

keys = [name for name in dir(pyxel) if name.startswith("KEY_")]

key_code = {key: getattr(pyxel, key) for key in keys}

# We need a SHIFT + Symbol map ...


BLACK = 0
WHITE = 7

WIDTH = 160
HEIGHT = 120


CHARACTER_WIDTH = 4
CHARACTER_HEIGHT = 6

pyxel.init(WIDTH, HEIGHT, title="Hello Keyboard")


def update():
    key_pressed = []
    for key, code in key_code.items():
        if pyxel.btnp(code):
            key_pressed.append(key)
    if key_pressed:
        print(
            key_pressed,
            [key_code[key] for key in key_pressed],
            [chr(key_code[key]) for key in key_pressed if key_code[key] < 256],
        )


def draw():
    pyxel.cls(BLACK)


pyxel.run(update, draw)
