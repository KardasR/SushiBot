"""
Screen Resolution: 1920 x 1080
Browser: Chrome Maximized. Toolbars enabled. Down arrow 5 times.
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
import win32api, win32con
from PIL import ImageOps
from numpy import *

# Globals
# ---------------------
x_pad = 340  # X1 - 1
y_pad = 215  # Y1 - 1

class Cord:
    # 'f_' prefix means it's referring to the food locations.

    f_shrimp = (43, 410)
    f_rice = (122, 413)
    f_nori = (37, 492)
    f_roe = (106, 479)
    f_salmon = (40, 564)
    f_unagi = (132, 548)

    # 't_' prefix means it's referring to the phone menu locations.

    phone = (716, 452)

    menu_toppings = (683, 339)

    t_shrimp = (655, 270)       # Greyed out:    (127, 102, 90)
    t_nori = 649, 330         # Greyed out:    (51, 127, 70)
    t_roe = 694, 340          # Greyed out:    (225, 181, 105)
    t_salmon = (583, 411)       # Greyed out:    (127, 71, 47)
    t_unagi =(684, 270)         # Greyed out:    (94, 49, 8)
    t_exit = (742, 412)

    menu_rice = (698, 364)
    buy_rice = 673, 346       # Greyed out:    (127, 127, 127)

    delivery_norm = (614, 364)


class Blank:
    seat_1 = 2978
    seat_2 = 3220
    seat_3 = 5403
    seat_4 = 4898
    seat_5 = 5689
    seat_6 = 4580


# Dictionary used to store how many ingredients are available
foodOnHand = {'shrimp': 5,
              'rice': 10,
              'nori': 10,
              'roe': 10,
              'salmon': 5,
              'unagi': 5}

# Dictionary used to store possible outcomes of each food
sushiTypes = {
    2852: 'onigiri',
    2916: 'onigiri',
    2980: 'onigiri',
    3516: 'caliroll',
    3389: 'caliroll',
    3050: 'gunkan',
    2796: 'gunkan',
    2923: 'gunkan',
}


def screenGrab():
    box = (x_pad + 1, y_pad + 1, x_pad + 799, y_pad + 599)
    im = ImageGrab.grab(box)

    ##im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im


def grab():
    box = (x_pad + 1, y_pad + 1, x_pad + 799, y_pad + 599)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    return a


def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    print("Click.")  # Debugging


def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    print("Left Down")


def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(.1)
    print("Left Up")


def startGame():
    # location of first menu (Play Button)
    mousePos((458, 254))
    leftClick()
    time.sleep(.1)

    # location of second menu
    mousePos((380, 483))
    leftClick()
    time.sleep(.1)

    # location of third menu
    mousePos((735, 565))
    leftClick()
    time.sleep(.1)

    # location of fourth menu
    mousePos((479, 458))
    leftClick()
    time.sleep(.1)


def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))


def get_cords():
    x, y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print(x, y)


def get_seat_one():
    box = (34 + x_pad, 68 + y_pad, 108 + x_pad, 88 + y_pad)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print("Seat 1")
    print(a)
    im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a


def get_seat_two():
    box = (160 + x_pad, 68 + y_pad, 234 + x_pad, 88 + y_pad)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print("Seat 2")
    print(a)
    im.save(os.getcwd() + '\\seat_two__' + str(int(time.time())) + '.png', 'PNG')
    return a


def get_seat_three():
    box = (286 + x_pad, 68 + y_pad, 360 + x_pad, 88 + y_pad)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print("Seat 3")
    print(a)
    im.save(os.getcwd() + '\\seat_three__' + str(int(time.time())) + '.png', 'PNG')
    return a


def get_seat_four():
    box = (413 + x_pad, 68 + y_pad, 487 + x_pad, 88 + y_pad)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print("Seat 4")
    print(a)
    im.save(os.getcwd() + '\\seat_four__' + str(int(time.time())) + '.png', 'PNG')
    return a


def get_seat_five():
    box = (539 + x_pad, 68 + y_pad, 613 + x_pad, 88 + y_pad)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print("Seat 5")
    print(a)
    im.save(os.getcwd() + '\\seat_five__' + str(int(time.time())) + '.png', 'PNG')
    return a


def get_seat_six():
    box = (665 + x_pad, 68 + y_pad, 739 + x_pad, 88 + y_pad)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print("Seat 6")
    print(a)
    im.save(os.getcwd() + '\\seat_six__' + str(int(time.time())) + '.png', 'PNG')
    return a


def get_all_seats():
    get_seat_one()
    get_seat_two()
    get_seat_three()
    get_seat_four()
    get_seat_five()
    get_seat_six()


def clear_tables():
    mousePos((112, 255))
    leftClick()

    mousePos((244, 255))
    leftClick()

    mousePos((353, 255))
    leftClick()

    mousePos((496, 255))
    leftClick()

    mousePos((612, 255))
    leftClick()

    mousePos((750, 255))
    leftClick()
    time.sleep(1)
    """
    Plate cords:

    112, 255
    244, 255
    353, 255
    496, 255
    612, 255
    750, 255
    """


def foldMat():
    mousePos((250, 474))
    leftClick()
    time.sleep(.1)


def makeFood(food):
    if food == 'caliroll':
        print("Making a caliroll")
        foodOnHand['rice'] -= 1     # Subtracts 1 from amount of Rice
        foodOnHand['nori'] -= 1     # Subtracts 1 from amount of Nori
        foodOnHand['roe'] -= 1      # Subtracts 1 from amount of Roe
        mousePos(Cord.f_rice)       # Get Rice
        leftClick()
        time.sleep(.1)
        mousePos(Cord.f_nori)       # Get Nori
        leftClick()
        time.sleep(.1)
        mousePos(Cord.f_roe)        # Get Roe
        leftClick()
        time.sleep(.1)
        foldMat()                   # Fold Mat
        time.sleep(1.5)

    elif food == 'onigiri':
        print("Making an Onigiri")
        foodOnHand['rice'] -= 2  # Subtracts 2 from amount of Rice
        foodOnHand['nori'] -= 1  # Subtracts 1 from amount of Nori
        mousePos(Cord.f_rice)    # Get Rice
        leftClick()
        time.sleep(.5)
        mousePos(Cord.f_rice)    # Get Rice
        leftClick()
        time.sleep(.1)
        mousePos(Cord.f_nori)       # Get Nori
        leftClick()
        time.sleep(.1)
        foldMat()                   # Fold Mat
        time.sleep(1.5)

    elif food == 'gunkan':
        print("Making a Gunkan")
        foodOnHand['rice'] -= 1  # Subtracts 1 from amount of Rice
        print(foodOnHand['rice'])
        foodOnHand['nori'] -= 1  # Subtracts 1 from amount of Nori
        foodOnHand['roe'] -= 2  # Subtracts 2 from amount of Roe
        mousePos(Cord.f_rice)     # Get Rice
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)     # Get Nori
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)      # Get Roe
        leftClick()
        time.sleep(.5)
        mousePos(Cord.f_roe)      # Get Roe
        leftClick()
        time.sleep(.1)
        foldMat()                 # Fold Mat
        time.sleep(1.5)


def buyFood(food):
    print("buying food")

    if food == 'rice':
        mousePos(Cord.phone)            # Open Phone
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_rice)        # Open Menu Toppings
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        if s.getpixel(Cord.buy_rice) != (127, 127, 127):
            print("Rice is available")
            mousePos(Cord.buy_rice)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['rice'] += 10    # Add 10 to amount of Rice
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print("Rice is NOT available")
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)


    if food == 'nori':
        mousePos(Cord.phone)  # Open Phone
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)  # Open Menu Toppings
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        print("Test for Nori")
        time.sleep(.1)
        if s.getpixel(Cord.t_nori) != (109, 123, 127):
            print("Nori is available")
            mousePos(Cord.t_nori)       # Get Nori
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)  # Normal Delivery
            foodOnHand['nori'] += 10    # Add 10 to amount of Nori
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print("Nori is not available")
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

    if food == 'roe':
        mousePos(Cord.phone)            # Open Phone
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)  # Open Menu Toppings
        time.sleep(.05)
        leftClick()
        s = screenGrab()

        time.sleep(.1)
        if s.getpixel(Cord.t_roe) != (109, 123, 127):
            print("Roe is available")
            mousePos(Cord.t_roe)          # Get Roe
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)  # Normal Delivery
            foodOnHand['roe'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)

        else:
            print("Roe is NOT available")
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)


def checkFood():
    print("Checking Food")
    for i, j in foodOnHand.items():
        if i == 'nori' or i == 'rice' or i == 'roe':
            if j <= 4:
                print("%s is low and needs to be replenished" % i)
                buyFood(i)


def check_bubs():

    checkFood()
    s1 = get_seat_one()             # Seat 1
    if s1 != Blank.seat_1:
        if s1 in sushiTypes:
            print("Table 1 is occupied and needs %s" % sushiTypes[s1])
            makeFood(sushiTypes[s1])
        else:
            print("Sushi not found!\n SushiType = %i" % s1)
    else:
        print("Table 1 unoccupied")

    print("Clearing tables")
    clear_tables()
    checkFood()
    s2 = get_seat_two()             # Seat 2
    if s2 != Blank.seat_2:
        if s2 in sushiTypes:
            print("Table 2 is occupied and needs %s" % sushiTypes[s2])
            makeFood(sushiTypes[s2])
        else:
            print("Sushi not found!\n SushiType = %i" % s2)

    else:
        print("Table 2 unoccupied")

    checkFood()
    s3 = get_seat_three()           # Seat 3
    if s3 != Blank.seat_3:
        if s3 in sushiTypes:
            print("Table 3 is occupied and needs %s" % sushiTypes[s3])
            makeFood(sushiTypes[s3])
        else:
            print("Sushi not found!\n SushiType = %i" % s3)

    else:
        print("Table 3 unoccupied")

    checkFood()
    s4 = get_seat_four()            # Seat 4
    if s4 != Blank.seat_4:
        if s4 in sushiTypes:
            print("Table 4 is occupied and needs %s" % sushiTypes[s4])
            makeFood(sushiTypes[s4])
        else:
            print("Sushi not found!\n SushiType = %i" % s4)

    else:
        print("Table 4 unoccupied")

    print("Clearing Tables")
    clear_tables()
    checkFood()
    s5 = get_seat_five()
    if s5 != Blank.seat_5:
        if s5 in sushiTypes:
            print("Table 5 is occupied and needs %s" % sushiTypes[s5])
            makeFood(sushiTypes[s5])
        else:
            print("Sushi not found!\n SushiType = %i" % s5)

    else:
        print("Table 5 unoccupied")

    checkFood()
    s6 = get_seat_six()             # Seat 6
    if s6 != Blank.seat_6:
        if s6 in sushiTypes:
            print("Table 6 is occupied and needs %s" % sushiTypes[s6])
            makeFood(sushiTypes[s6])
        else:
            print("Sushi not found!\n SushiType = %i" % s6)

    else:
        print("Table 6 unoccupied")

    print("Clearing Tables")
    clear_tables()
    print("Sleeping")
    time.sleep(10)


def main():
    startGame()
    time.sleep(10)
    while True:
        check_bubs()


if __name__ == '__main__':
    main()
