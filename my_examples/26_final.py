import pyxel

def spawn_new_fruit():
    global fruit 
    fruit = [
        pyxel.rndi(0, 29), 
        pyxel.rndi(0, 29)
    ]

def spawn_new_snake():
    global snake_geometry, snake_direction
    snake_geometry = [
        [10, 15],
        [11, 15],
        [12, 15],
    ]
    snake_direction = [1, 0]
 
checkerboard = False

arrow_keys = [
    pyxel.KEY_UP, 
    pyxel.KEY_DOWN, 
    pyxel.KEY_LEFT, 
    pyxel.KEY_RIGHT
]

started = False

def update():
    global checkerboard, snake_geometry, snake_direction, started
    if not started:
        if pyxel.btnp(pyxel.KEY_SPACE):
            started = True
            spawn_new_snake()
            spawn_new_fruit()
        return
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
            snake_direction = [0, -1]
        elif key == pyxel.KEY_DOWN:
            snake_direction = [0, 1]
        elif key == pyxel.KEY_LEFT:
            snake_direction = [-1, 0]  
        elif key == pyxel.KEY_RIGHT:
            snake_direction = [1, 0]
    snake_head = snake_geometry[-1]
    new_snake_head = [
      snake_head[0] + snake_direction[0],
      snake_head[1] + snake_direction[1]
    ]
    if new_snake_head in snake_geometry:
        started = False
    elif ( 
        new_snake_head[0] < 0 or 
        new_snake_head[0] > 29 or 
        new_snake_head[1] < 0 or 
        new_snake_head[1] > 29
        ):
        started = False
    elif new_snake_head == fruit:
        snake_geometry = snake_geometry + [new_snake_head]
        spawn_new_fruit()
    else:
        snake_geometry = snake_geometry[1:] + [new_snake_head]

def draw():
    pyxel.cls(7)
    if not started:
        pyxel.text(5, 3, "Press", 0)
        pyxel.text(5, 9, "SPACE", pyxel.frame_count % 16)
        pyxel.text(11, 15, "to", 0)
        pyxel.text(5, 21, "start", 0)
        return
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

pyxel.init(30, 30, fps=10)
pyxel.run(update, draw)