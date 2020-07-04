import numpy as np
import cv2
import win32gui
import win32ui
import win32con

def screen_cap(roi=None):
    # width and height
    w = 1920
    h = 1080


    # hwnd = win32gui.FindWindow(None, windowname)
    hwnd = None

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

    # Free Resources
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())

    return img



