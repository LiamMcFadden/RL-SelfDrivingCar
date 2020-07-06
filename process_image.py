import cv2
import numpy as np
import os
import time

def process_image(img):
    curr = time.time()
    cwd = os.getcwd()
    img = cv2.GaussianBlur(img, (5, 5), 0)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #print("Elapsed time: {}".format(time.time() - curr))


    return img
