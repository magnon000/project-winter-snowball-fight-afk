#! /usr/bin/env python
# -*- coding: utf-8 -*
"""
识别窗口
"""
import win32gui

# 0.遍历窗口
windows_titles = set()

# 不知道为什么window_traverse要有两个参数，后面那个why没用上
def window_traverse(hwnd,why):
    # Determines whether the specified window handle identifies an existing window.
    # Indicates if the window is enabled.
    # Indicates if the window has the WS_VISIBLE style.
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        windows_titles.add(win32gui.GetWindowText(hwnd))


# Enumerates all top-level windows on the screen by passing the handle to each window, in turn,
#   to an application-defined callback function.
win32gui.EnumWindows(window_traverse, 0)

# Enumerates the child windows that belong to the specified parent window by passing the handle to each child window,
#   in turn, to an application-defined callback function. EnumChildWindows continues until the last child window is
#   enumerated or the callback function returns FALSE.
#win32gui.EnumChildWindows(hwnd, callback, extra)

if __name__ == "__main__":
    lt = [t for t in windows_titles if t]
    lt.sort()
    for t in lt:
        print(t)