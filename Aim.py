import pydirectinput
from pynput import mouse
import tools
import threading


def mouse_listen(x, y, button, pressed):
    if pressed:
        if button == button.x2:
            Aim.is_open = True
            print('自瞄开启')
        elif button == button.x1:
            Aim.is_open = False
            print('自瞄关闭')


def move2(x, y):
    final_x = int(x - tools.get_capture_x()/2)
    final_y = int(y - tools.get_capture_y()/2)
    pydirectinput.moveRel(final_x, final_y, relative=True)
    # pydirectinput.click()
    
    
def move(x, y):
    tools.get_capture_x()
    tools.get_capture_y()
    pydirectinput.moveTo(int(x) + tools.get_capture_x(), int(y) + tools.get_capture_y())
        
        
class Aim:
    is_open = True

    def __init__(self):
        self.listener = mouse.Listener(on_click=mouse_listen)
        self.listener.start()