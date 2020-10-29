from ursina import *

class settings(object):
    def __init__(self):
        self.title = "Schoolgame"
        self.borderless = False
        self.show_x = False

data = settings()

window.title = data.title
window.borderless = data.borderless
window.exit_button.visible = data.show_x

camera.fov = 90
