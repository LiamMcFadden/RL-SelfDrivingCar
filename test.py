from screen_cap import screen_cap
from process_image import process_image
import cv2

img = screen_cap()
img = process_image(img)

cv2.imshow("test", img)
cv2.waitKey(0)
