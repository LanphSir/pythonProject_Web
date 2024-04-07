from pynput.keyboard import Key, Listener
import threading
from pyautogui import sleep, hotkey, countdown, click

is_looping = False
exit_program = False
runs = 0
time_stop = 50


def copy_text():
    # print(gui.size())
    # print(gui.position())
    # gui.mouseInfo()
    click(1422, 976)
    sleep(.5)
    hotkey('ctrl', 'c')
    sleep(.5)
    click(1000, 1003)
    sleep(1)
    hotkey('ctrl', 'v')
    sleep(2)
    hotkey('enter')
    # gui.click(1314, 1003)


def perform_looping_action():
    global is_looping, runs
    while is_looping:
        copy_text()
        runs += 1
        print("执行完成第", runs, "次  进程等待中 等待", time_stop, '秒')
        sleep(time_stop)
        countdown(time_stop)


def on_press(key):
    global is_looping, exit_program
    # 触发
    if key == Key.f3:
        if not is_looping:
            is_looping = True
            threading.Thread(target=perform_looping_action).start()
    # 停止
    elif key == Key.space:
        is_looping = False
        print('暂停运行')
    # 退出
    elif key == Key.esc:
        is_looping = False
        exit_program = True
        return False


def on_release(key):
    print(key)


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

if exit_program:
    print("退出 Exiting program.")
