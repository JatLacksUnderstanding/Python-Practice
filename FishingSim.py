import time

import pyautogui as pg
import pygetwindow as gw

white = (255, 255, 255)
slot_color = (0, 213, 255)
toggle = True


def main():
    global toggle
    while True:
        time.sleep(0.05)
        if get_focused_window('Roblox'):
            if pg.pixelMatchesColor(625, 977, slot_color, tolerance=50):
                if bubble_check():
                    pg.click(button='left')
                    toggle = True
                if fish_on():
                    if pg.pixelMatchesColor(940, 822, white):
                        pg.click(button='left')
                if pg.pixelMatchesColor(990, 315, white, tolerance=10) and toggle:
                    time.sleep(0.5)
                    pg.click(button='left')
                    toggle = False
                    print(toggle)


def get_focused_window(title):
    try:
        if gw.getActiveWindow().title == title:
            return True
    except:
        return False


def fish_on():
    bar_color = (83, 250, 83)
    if pg.pixelMatchesColor(1086, 837, bar_color) and pg.pixelMatchesColor(846, 830, bar_color):
        return True
    else:
        return False


def bubble_check():
    rod = (0, 213, 255)
    alert = (255, 24, 0)
    x, y = pg.position()
    if pg.pixelMatchesColor(x, y, alert, tolerance=100):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
