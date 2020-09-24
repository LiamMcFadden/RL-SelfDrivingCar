import numpy as np
import cv2
import win32gui
import win32ui
import win32con

def screen_cap(hwnd = None):
    # width and height
    w = 1920
    h = 1080

    if hwnd:
        hwnd = win32gui.FindWindow(None, hwnd)
        x1, y1, x2, y2 = win32gui.GetWindowRect(hwnd)
        w = x2 - x1
        h = y2 - y1

    # get window data
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj=win32ui.CreateDCFromHandle(wDC)
    cDC=dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0,0),(w, h) , dcObj, (0,0), win32con.SRCCOPY)

    # convert to usable format
    raw = dataBitMap.GetBitmapBits(True)
    img = np.fromstring(raw, dtype='uint8')
    img.shape = (h, w, 4)

    # get rid of alpha channel
    img = img[:,:,:3]

    # make img contiguous so we can draw shapes and what not on it
    img = np.ascontiguousarray(img)

    # Free Resources
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())

    return img



