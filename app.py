from ursina import *
from ursina.application import pause, resume

app = Ursina()

player = Entity(model='quad', y = -0.5, color=color.red, scale_y=2)
player2 = Entity(model='quad', y = -0.5, color=color.blue, scale_y=2)

ground = Entity(
    model = 'quad',
    color = color.black,
    z = -.1,
    y = -3,
    origin = (0, .5),
    scale = (100, 100, 10),
    collider = 'box',
    )

wall = Entity(
    model = 'quad',
    color = color.black,
    x = 5,
    scale = (2, 100, 0),
    collider = 'box'
)

camera.parent = player

def update():
    player.x += held_keys['d'] * time.dt * 9 
    player.x -= held_keys['a'] * time.dt * 9
    player2.x += held_keys['l'] * time.dt * 9
    player2.x -= held_keys['j'] * time.dt * 9

def input(key):
    if key == 'w':
        player.y += 2
        invoke(setattr, player, 'y', player.y-2, delay=.5)
    elif key == 'i':
        player2.y +=2
        invoke(setattr, player2, 'y', player2.y-2, delay=.5)


app.run()