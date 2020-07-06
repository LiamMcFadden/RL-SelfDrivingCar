import cv2
import numpy as np
import os
from screen_cap import screen_cap
from time import sleep

# list of images
imgs = os.listdir("./ball-img")

# name of window for try except
hwnd = "Rocket League (64-bit, DX11, Cooked)"

def process_image(img, img_index):
    # get an image from 'img' directory
    template = cv2.imread("./ball-img/{}".format(imgs[img_index]))

    # original image to draw rectangles on
    og_img = img

    # define region of interest
    roi_xy1 = (450, 219)
    roi_xy2 = (830, 549)
    img = img[roi_xy1[1]:roi_xy2[1], roi_xy1[0]:roi_xy2[0]]

    """
    Kind of crappy rn...
    TODO: try contour/edge detection
    """

    # find matches
    minimized = False
    try:
        img = cv2.matchTemplate(template, img, cv2.TM_CCOEFF_NORMED)
    except Exception as ex:
        minimized = True
        print("The window cannot be minimized...")

    # wait until user reopens window
    while minimized:
        try:
            img = screen_cap(hwnd=hwnd)
            img = cv2.matchTemplate(template, img, cv2.TM_CCOEFF_NORMED)
        except Exception as ex:
            pass
        else:
            print("Resuming...")
            sleep(1)
            break

    # get location and confidence
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(img)

    # only draw rectangle and calc location if the confidence is greater than 0.6
    if max_val > 0.65:
        # convert location to be relative to og_img
        top_left = (max_loc[0] + roi_xy1[0], max_loc[1] + roi_xy1[1])
        bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])

        cv2.rectangle(og_img, top_left, bottom_right, color=(0,0,255),
                thickness=2, lineType=cv2.LINE_4)

        print("Ball location: ", max_loc)
        print("Confidence: ", max_val)

    return og_img













