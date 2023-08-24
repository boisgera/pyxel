import pyxel

# TODO: get rid of line height, introduce a print_char(),
#       make the stuff auto-scroll (?) and scrollable up/down?
#       Make prompt and a blinking cursor?
#       Make a HUD?

BLACK = 0
DARK_BLUE = 1
WHITE = 7

pyxel.init(160, 120, title="Hello Pyxel")

CHARACTER_WIDTH = 4
CHARACTER_HEIGHT = 6

LINE_HEIGHT = 6
MARGIN_LEFT = 4
MARGIN_RIGHT = MARGIN_LEFT
MARGIN_TOP = 3
COLUMNS = (pyxel.width - MARGIN_LEFT - MARGIN_RIGHT) // CHARACTER_WIDTH

PADDING_TOP = (LINE_HEIGHT - CHARACTER_HEIGHT) // 2
PADDING_BOTTOM = (LINE_HEIGHT - CHARACTER_HEIGHT) - PADDING_TOP

cursor_x, cursor_y = 0, 0
text_color = WHITE


def pyxel_print(text):
    global cursor_x, cursor_y
    text = str(text)
    lines = text.split("\n")
    short_lines = []
    for line in lines:
        while len(line) > COLUMNS:
            short_lines.append(line[:COLUMNS])
            line = line[COLUMNS:]
        short_lines.append(line)
    for line in short_lines:
        x = cursor_x * CHARACTER_WIDTH + MARGIN_LEFT
        y = cursor_y * LINE_HEIGHT + MARGIN_TOP + PADDING_TOP
        pyxel.text(x, y, line, text_color)
        cursor_x = 0
        cursor_y += 1


def update():
    global cursor_x, cursor_y
    cursor_x, cursor_y = 0, 0
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()


def draw():
    pyxel.cls(DARK_BLUE)

    pyxel_print({"a": 1, "g": 2, "c": 3, "M": "X"})

    for key in dir(pyxel):
        if key.startswith("KEY"):
            print(key)


pyxel.run(update, draw)
