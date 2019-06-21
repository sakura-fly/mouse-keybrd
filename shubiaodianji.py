from datetime import datetime
import time, threading

from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Listener

isRun = False
timeSkip = 2


# 每n秒执行一次
def timer(n):
    global isRun
    print(datetime.now().strftime("%Y-%m-%d  %H:%M:%S"))
    mouseCtr()
    time.sleep(n)
    if isRun:
        timer(n)


def mouseCtr():
    '''
    控制鼠标
    '''
    # 读鼠标坐标
    mouse = Controller()
    # 点击鼠标
    mouse.click(Button.left)


def on_release(key):
    global isRun
    # print('{0} release'.format(key))

    if key == Key.esc:
        # Stop listener
        isRun = False
        return False

    if key == Key.f12:
        # Stop listener
        isRun = not isRun
        if isRun:
            startT()
        # print(not isRun)


def setKetBordListern():
    # 连接事件以及释放
    with Listener(on_release=on_release) as listener:
        listener.join()


def startT():
    t = threading.Thread(target=timer, args=(timeSkip,))
    t.start()


def main():
    t = threading.Thread(target=setKetBordListern)
    t.start()


main()
