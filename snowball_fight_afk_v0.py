"""
Project Winter雪球战脚本挂机刷钱,每一次雪球命中游戏币加一

然后发现每个房间雪球战上限300币
换房间可以重置
但我没学好opencv
告辞
"""

import random
import threading
import time

import win32api
import win32con
from pynput import keyboard


def mouse_hold_click():
    """
    调用win32api模拟鼠标左右键。
    一个循环为：右键按住 n + random.uniform(0, 0.05) 秒，左键点击，左键松开，右键松开
    未优化到最佳
    """
    rn = round(random.uniform(0, 0.05), 2)
    pos = win32api.GetCursorPos()
    cox = int(pos[0])
    coy = int(pos[1])
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, cox, coy, 0, 0)
    time.sleep(0.2 + rn)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, cox, coy, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, cox, coy, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, cox, coy, 0, 0)
    time.sleep(rn)


f10t = 0  # 或者用False
flag = False


def start_f10():
    """
    调用 mouse_hold_click
    """
    while flag:
        mouse_hold_click()


def on_press_f10():
    global f10t, flag, th
    f10t += 1
    print(f10t)
    if f10t % 2 != 0:
        flag = True
        th = threading.Thread(target=start_f10)  # idk how to do it without multi-threading
        th.start()
    elif f10t % 2 == 0:
        flag = False
        print("paused")
        if th.is_alive():
            th.join()


if __name__ == "__main__":
    """
    按alt+f10开始，偶数次按下暂停
    """
    print("Press Alt+F10 to start")
    with keyboard.GlobalHotKeys({
        '<alt>+<f10>': on_press_f10
    }) as f10key:
        f10key.join()

    # -------------------------------
    # 全局检测会报错
    # with keyboard.Listener(on_press=on_press) as listener:
    #     listener.join()
    # -------------------------------
    # current_window = (win32gui.GetWindowText(win32gui.GetForegroundWindow()))
    # desired_window_name = "WinterProject"
    # if current_window == desired_window_name:
    # windows_titles = set()
    # win32gui.EnumWindows(gwt.window_traverse, 0)
    # lt = [t for t in windows_titles if t]
    # lt.sort()
    # print(lt)
    # while "ProjectWinter" in lt:
    # else:
    # print("game is not on or on top")
    # os.system("pause")
