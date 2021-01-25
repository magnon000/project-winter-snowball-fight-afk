"""
Project Winter雪球战脚本挂机刷钱,每一次雪球命中游戏币加一

然后发现每个房间雪球战上限300币
换房间可以重置上限
但我没学好opencv
告辞
"""

import random
import threading
import time

import win32api
import win32con
import win32gui
from pynput import keyboard


def mouse_hold_click():
    """
    调用win32api模拟鼠标左右键。
    一个循环为：右键按住 n + random.uniform(0, 0.05) 秒，左键点击，左键松开，右键松开
    n未优化到最佳
    """
    rn = round(random.uniform(0, 0.05), 2)
    pos = win32api.GetCursorPos()
    cox = int(pos[0])
    coy = int(pos[1])
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, cox, coy, 0, 0)
    time.sleep(0.1 + rn)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, cox, coy, 0, 0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, cox, coy, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, cox, coy, 0, 0)
    time.sleep(0.1 + rn)


flag = False
count = 0
start_time = end_time = total_time = 0


def start_f10():
    """
    调用 mouse_hold_click
    """
    global count
    while flag:
        mouse_hold_click()
        count += 1
        # if count == 300:
        #     print(time.ctime())
        #     break


def check_windows_if_on_top():
    """
    切换到非 ProjectWinter 窗口后暂停
    """
    global flag, start_time
    while flag:
        hwnd = win32gui.GetForegroundWindow()
        window_name = win32gui.GetWindowText(hwnd)
        if window_name != 'ProjectWinter':
            flag = not flag
            start_time = time.time()
            print("---paused--- window changed, fail-safe triggered")
        time.sleep(0.014)  # my threshold of changing window


def on_press_f10():
    global flag, start_time, end_time, total_time
    flag = not flag
    ch = threading.Thread(target=check_windows_if_on_top)
    ch.start()
    th = threading.Thread(target=start_f10)  # idk how to do it without multi-threading
    th.start()
    if flag:
        start_time = time.time()
        print("---started--- at", time.ctime())
    else:
        end_time = time.time()
        total_time += round(end_time - start_time, 1)
        print("---paused--- at", time.ctime(), "\n", "time passed:", round(end_time - start_time, 1), "s")
        print(" total time passed:", round(total_time / 60, 2), "min |", round(total_time / 3600, 1), "h\n",
              "total round passed:", count, "\n")


if __name__ == "__main__":
    """
    按alt+f10开始，再次按下暂停
    """
    print("Press Alt+F10 to start, press again to pause\n")
    with keyboard.GlobalHotKeys({
        '<alt>+<f10>': on_press_f10
    }) as f10key:
        f10key.join()
