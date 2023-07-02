import cv2
import numpy as np
import pyautogui
import mss
import pyglet
import win32api
import win32con
import win32gui
from PIL import ImageGrab
from pyglet import window

screen_width, screen_height = pyautogui.size()
capture_width = screen_width // 3
capture_height = screen_height // 3
capture_x = (screen_width - capture_width) // 2
capture_y = (screen_height - capture_height) // 2
sec = mss.mss()


def screen_shot1():
    # 0.08
    image = pyautogui.screenshot(region=[capture_x, capture_y, capture_width, capture_height])
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    return image


def screen_shot2():
    # 0.06
    image = sec.grab({'left': capture_x, 'top': capture_y, 'width': capture_width, 'height': capture_height})
    image = np.array(image)

    return image


def screen_shot3():
    # 0.07
    image = ImageGrab.grab()
    image = cv2.cvtColor(np.asarray(image), cv2.COLOR_RGB2BGR)

    return image


def screen_shot4():
    pass


def get_capture_width():
    return capture_width


def get_capture_height():
    return capture_height


def get_capture_x():
    return capture_x


def get_capture_y():
    return capture_y
