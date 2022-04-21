import os
import pyautogui
import time
import keyboard
print('打开腾讯会议——应用——签到')
print('把鼠标移动到"点击签到"按钮位置，5秒后会获取坐标')
i = 1
for i in range(6):
    print(i)
    time.sleep(1)
p = pyautogui.position()
print('按下空格停止')
while True:
    flag = False
    def key_press(key):
        global flag
        if key.name == 'space':
            flag = True
    keyboard.on_press(key_press)
    pyautogui.click(p)
    time.sleep(1)
    if flag == True:
        flag = False
        os._exit(0)
