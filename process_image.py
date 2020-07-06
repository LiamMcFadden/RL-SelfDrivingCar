import cv2
import numpy as np
import os

# list of images
imgs = os.listdir("./img")

def process_image(img, img_index):
    # get an image from 'img' directory
    template = cv2.imread("./img/{}".format(imgs[img_index]))

    # original image to draw rectangles on
    og_img = img

    # img = cv2.GaussianBlur(img, (9, 9), 0)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # find matches
    img = cv2.matchTemplate(template, img, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(img)

    # only draw rectangle and calc location if the confidence is greater than 0.6
    if max_val > 0.6:
        top_left = max_loc
        bottom_right = (top_left[0] + img.shape[1], top_left[1] + img.shape[0])
        cv2.rectangle(og_img, top_left, bottom_right, color=(0,0,255),
                thickness=2, lineType=cv2.LINE_4)

        print("Ball location: ", max_loc)
        print("Confidence: ", max_val)

    return og_img
