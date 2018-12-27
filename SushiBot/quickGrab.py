"""
Screen Resolution: 1920 x 1080
Browser: Chrome Maximized. Toolbars enabled.
Name: Ryan Kardas
Game: https://www.miniclip.com/games/sushi-go-round/en/

PLAY AREA:
X1: 341
Y1: 216

X2: 1140
Y2: 815
"""
from PIL import ImageGrab
import os
import time

# Globals
#---------------------
x_pad = 340                 # X1 - 1
y_pad = 215                 # Y1 - 1


def screenGrab():
    box = (x_pad+1, y_pad+1, x_pad+799, y_pad+599)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')


def main():
    screenGrab()


if __name__ == '__main__':
    main()