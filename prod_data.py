from screen_cap import screen_cap
import cv2
from key_list import key_check
import random
import time

"""
Automatically produces a collection of images with ROI pre-defined. Images are captured every 2-6 seconds.
"""

hwnd = "Rocket League (64-bit, DX11, Cooked)"

# image number
ball_num = 0
# random interval
interval = random.randint(2,6)
elapsed = time.time()
paused = False
numPics = 0

print("Press q to quit, p to pause.")
print("Running...")

while True:
    if not paused:
        keys = key_check()
        img = screen_cap(hwnd=hwnd)
        # cv2.imshow("data", img)
        # quit on press of 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # take a screenshot on a random interval of 2-6 seconds
        if time.time()-elapsed > interval:
            elapsed = time.time()
            interval = random.randint(2, 6)
            roi_xy1 = (450, 219)
            roi_xy2 = (830, 549)
            img = img[roi_xy1[1]:roi_xy2[1], roi_xy1[0]:roi_xy2[0]]
            cv2.imshow("data", img)
            # cv2.imwrite('ball-img/ball{}.png'.format(ball_num), img)
            numPics += 1
            ball_num += 1

        elif 'q' in keys:
            break
    elif 'q' in keys:
        break

    # pausing
    keys = key_check()
    if 'p' in keys:
        if paused:
            paused = False
            print("Unpaused...")
            time.sleep(1)
        elif not paused:
            paused = True
            print("paused...")
            time.sleep(1)

    pass

print("{} frames captured!".format(numPics))






