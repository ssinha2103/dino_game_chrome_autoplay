import pyautogui as pg
from PIL import Image, ImageGrab
import time


import numpy as np


def hit(key):
    pg.keyDown(key)
    return


def isCollide(data):
    for i in range(290, 486):
        for j in range(515, 530):
            if data[i, j] < 100:
                return True
    return False


def isUp(data):
    for i in range(290, 486):
        for j in range(430, 435):
            if data[i, j] < 100:
                return True
    return False

def isUpTwo(data):
    for i in range(180, 372):
        for j in range(500, 505):
            data[i, j] = 0
            return True
    return False


if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    # time.sleep(2)
    hit('up')
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        if isCollide(data):
            hit('up')
        if isUp(data):
            hit('down')
        # if isUpTwo(data):
        #     hit('up')
    # print(np.asarray(image))
    # for i in range(284, 375):
    #     for j in range(485, 527):
    #         data[i, j] = 0

    # image.show()
