import cv2
import imutils
import numpy as np
import os
from screen_cap import screen_cap
from time import sleep

# name of window for try except
hwnd = "Rocket League (64-bit, DX11, Cooked)"

# determines canny parameters based on frame
def getCanny(img):
    v = np.median(img)
    lower = int(max(0, (1.0 - 0.23) * v))
    upper = int(min(255, (1.0 + 0.23) * v))
    ret = cv2.Canny(img, lower, upper)
    return ret

def process_image(img):
    # original image to draw rectangles on
    og_img = img

    # define region of interest
    roi_xy1 = (450, 219)
    roi_xy2 = (830, 549)
    # img = img[roi_xy1[1]:roi_xy2[1], roi_xy1[0]:roi_xy2[0]]

    # make the image easier to work with
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img, (11, 11), 0)
    img = getCanny(img)

    # find circles
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1.2, 10)
    # ensure at least some circles were found
    if circles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")

        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            # draw the circle in the output image, then draw a rectangle
            # corresponding to the center of the circle
            cv2.circle(og_img, (x + roi_xy1[0], y + roi_xy1[1]), r, (0, 255, 0), 4)
            cv2.rectangle(og_img, (x - 5 + roi_xy1[0], y - 5 + roi_xy1[1]), (x + 5 + roi_xy1[0], y + 5 + roi_xy1[1]), (0, 128, 255), -1)

        return og_img













