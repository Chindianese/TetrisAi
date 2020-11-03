import cv2
from PIL import ImageGrab
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
from termcolor import colored
import keyboard  # using module keyboard

screen_left = -1
screen_bottom = -1
screen_top = -1


def grab_board(target_hwnd):  # screenshot board based on borders
    left, top, right, bottom = win32gui.GetWindowRect(target_hwnd)
    game_screen = getRectAsImage((left + screen_left, top + screen_top, right - screen_left, bottom - screen_bottom))
    game_screen = np.array(game_screen)
    height, width, channels = game_screen.shape
    cv2.imshow("Screen", game_screen)
    # key = cv2.waitKey(0)
    cv2.destroyAllWindows()
    game_screen = np.array(game_screen)
    return game_screen, width, height


def find_borders(target_hwnd):  # get borders of tetris board
    left, top, right, bottom = win32gui.GetWindowRect(target_hwnd)
    # Capture an arbitrary rectangle of the virtual screen: (left, top, right, bottom)
    game_screen = getRectAsImage((left, top, right, bottom))
    game_screen = np.array(game_screen)
    height, width, channels = game_screen.shape
    min_val = 10
    max_val = 80
    board_color_max = np.array([max_val, max_val, max_val])
    board_color_min = np.array([min_val, min_val, min_val])
    mask = cv2.inRange(game_screen, board_color_min, board_color_max)
    # cv2.imshow("Screen", mask)
    # key = cv2.waitKey(-1)
    global screen_top
    global screen_bottom
    global screen_left

    for col in range(200, width):
        color = mask[int(height / 2), col]
        if color > 0:  # found blank
            global screen_left
            screen_left = col
            break

    for row in range(50, height):
        color = mask[height - row, screen_left + 10]
        if color > 0:  # found blank
            screen_bottom = row
            break

    for row in range(150, height):
        color = mask[row, screen_left + 10]
        if color > 0:  # found blank
            screen_top = row
            break

    print(f"left: {screen_left}")
    print(f"bot: {screen_bottom}")
    print(f"top: {screen_top}")
    cv2.destroyAllWindows()


def screenshot_to_board_array(game_screen, screen_width, screen_height):
    board = np.zeros((20, 10))
    tile_width = screen_width / 10
    for row in range(20):
        for col in range(10):
            x = tile_width * row + tile_width / 2
            y = tile_width * col + tile_width/2
            col_val = game_screen[int(x), int(y)][0]
            if col_val > 0:
                board[row][col] = 1
            else:
                board[row][col] = 0

    return board

