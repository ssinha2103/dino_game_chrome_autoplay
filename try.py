import pyautogui as pg
from PIL import Image, ImageGrab
import time


def takeScreenshot():
    image = ImageGrab.grab().convert('L')
    return image


time.sleep(1)
image = takeScreenshot()
data = image.load()
for i in range(290, 486):
    for j in range(515, 530):
        data[i, j] = 0

for i in range(290, 486):
    for j in range(430, 435):
        data[i, j] = 0

for i in range(180, 372):
    for j in range(500, 505):
        data[i, j] = 0
image.show()