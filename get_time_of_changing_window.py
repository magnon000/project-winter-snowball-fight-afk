"""
get the time needed to change from a window to another one.
"""
import os
import time

import win32gui

n = 0

while True:
    global begin_time, end_time
    hwnd = win32gui.GetForegroundWindow()
    title_text = win32gui.GetWindowText(hwnd)
    n += 1
    if title_text != 'Search':  # target window (WIN button)
        begin_time = time.time()
    else:
        end_time = time.time()
        print("\ntime needed:", end_time - begin_time, "s", "\nexecution:", n)  # sometimes it prints "0.0 s", idk why.
        os._exit(0)
    print(hwnd, title_text)
    time.sleep(0.014)  # my threshold > 0.015
