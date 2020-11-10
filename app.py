from ursina import *
from ursina.application import pause, resume
from ursina.prefabs.first_person_controller import FirstPersonController
import time

app = Ursina()


a = Audio('bruh', autoplay=True)
printvar(a)


player = FirstPersonController()

ground = Entity(
    model = 'cube',
    color = color.black,
    z = -.1,
    y = -1,
    origin_y = .5,
    scale = (100, 10, 100),
    collider = 'box',
    ignore = True,
    )

wall = Entity(
    model = 'cube',
    color = color.white,
    z = -50,
    y = 5,
    origin_y = .5,
    scale = (100, 50, 0),
    collider = 'box',
    ignore = True,
    )

wall2 = Entity(
    model = 'cube',
    color = color.white,
    z = 50,
    y = 5,
    origin_y = .5,
    scale = (100, 50, 0),
    collider = 'box',
    ignore = True,
    )

wall3 = Entity(
    model = 'cube',
    color = color.white,
    x = -50,
    y = 5,
    origin_y = .5,
    scale = (0, 50, 100),
    collider = 'box',
    ignore = True,
    )

wall4 = Entity(
    model = 'cube',
    color = color.white,
    x = 50,
    y = 5,
    origin_y = .5,
    scale = (0, 50, 100),
    collider = 'box',
    ignore = True,
    )

camera.fov = 90

speed = 0

def update():
    #Updates player location
    player.right = held_keys['d'] * time.dt * 15
    player.left = held_keys['a'] * time.dt * 15
    player.forward = held_keys['w'] * time.dt * 15
    player.back = held_keys['s'] * time.dt * 15 



Sky()
app.run()