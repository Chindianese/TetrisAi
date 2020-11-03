import screengrabber
import win32gui
import numpy as np
from desktopmagic.screengrab_win32 import (
    getDisplayRects, saveScreenToBmp, saveRectToBmp, getScreenAsImage,
    getRectAsImage, getDisplaysAsImages)
from PIL import ImageGrab
import win32api
import win32con
import win32com
import time
import tetrisboard
from termcolor import colored
import keyboard  # using module keyboard
# main loop
targetWindow = "TETR.IO - Google Chrome"
targetHWND = -1
topList = []


def enum_win(hwnd, result):
    global targetHWND
    if targetHWND >= 0:
        return
    # print(hwnd)
    win_text = win32gui.GetWindowText(hwnd)
    if targetWindow in win_text:
        targetHWND = hwnd
        print("found")


def main():
    win32gui.EnumWindows(enum_win, topList)

    if targetHWND < 0:
        print("failed to find")
    time.sleep(1)
    screengrabber.find_borders(targetHWND)
    game_screen, width, height = screengrabber.grab_board(targetHWND)
    board_array = screengrabber.screenshot_to_board_array(game_screen, width, height)
    tetrisboard.init_board(board_array)
    tetrisboard.print_current_board()


main()

