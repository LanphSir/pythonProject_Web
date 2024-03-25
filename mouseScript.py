import pyautogui as gui
import time
import keyboard


def copy_text():
    # print(gui.size())
    print(gui.position())
    # gui.moveTo(1314, 1003)
    time.sleep(1)
    # gui.hotkey('ctl', 'c')
    # gui.mouseInfo()
    # gui.moveTo(1422, 976)
    # gui.click(1000, 1003)
    # gui.hotkey('ctrl', 'v')


def loop_copy():
    while True:
        if keyboard.is_pressed('space'):
            print('暂停')
            break
        copy_text()
        time.sleep(20)


keyboard.hook(loop_copy, args=('a',))

keyboard.add_hotkey('ctrl+1', copy_text)
keyboard.add_hotkey('ctrl+2', loop_copy)
keyboard.wait('esc')
