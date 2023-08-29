import pyxel

pyxel.init(30, 30, fps=10)

fruit = None

def spawn_new_fruit():
    global fruit 
    fruit = [
        pyxel.rndi(0, 29), 
        pyxel.rndi(0, 29)
    ]

spawn_new_fruit()

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

def update():
    global checkerboard, snake_geometry, snake_direction
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
    if new_snake_head == fruit:
        snake_geometry = snake_geometry + [new_snake_head]
        spawn_new_fruit()
    else:
        snake_geometry = snake_geometry[1:] + [new_snake_head]

def draw():
    pyxel.cls(7)
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

pyxel.run(update, draw)