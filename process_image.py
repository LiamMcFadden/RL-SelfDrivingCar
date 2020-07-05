import cv2
import numpy as np

def process_image(img):
    img = cv2.GaussianBlur(img, (5, 5), 0)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


    return img
