import numpy as np
import cv2
from pyautogui import screenshot

def screen_cap(roi=None):
    img = screenshot(region=roi)

    # convert to usable format
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    return img



