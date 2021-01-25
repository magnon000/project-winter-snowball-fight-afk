# project-winter-snowball-fight-afk
python script for project winter(steam app id: 774861), afk for in-game currency

***

***

Python script for Project Winter snowball fight, each hit of snowball on other characters results in +1 in-game currency, however for each room there is a limitation of receiving no more than 300 coins.

## Key functions:

* simulate mouse clicks using ***win32api***
* detect hwnd （***ProjectWinter.exe***)
* detect input (alt + F10)

## How to use?

* press "alt + F10" once to start
* press again to pause
* if ***ProjectWinter.exe*** is not open or on the top of the screen, pause

## Testing the time needed to change your window

* open ***get_time_of_changing_window.py***
* press "win" (change to a different window)
* read the result and make your adjustment in ***snowball_fight_afk.py***

***

Project Winter雪球战python脚本挂机刷钱，每一次雪球命中游戏币加一，但每个房间雪球战上限300币。

## 关键

* 调用***win32api***模拟鼠标左右键
* 检测窗口（是否为***ProjectWinter.exe***）
* 检测按键 （alt + F10）

## 用法

* 按 “alt + F10” 开始
* 再次按下则暂停
* 如果没有打开***ProjectWinter.exe***或者最小化了窗口，则暂停

## 测试切换窗口所需时间

* 打开 ***get_time_of_changing_window.py***
* 按下 "win" (以改变窗口)
* 得到数值并自己更改 ***snowball_fight_afk.py***



*p.s.* 不是因为实习的话我都不好意思公开我写的bug们（懒

