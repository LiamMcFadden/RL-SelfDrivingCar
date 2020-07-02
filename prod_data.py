from screen_cap import screen_cap
import os
import time
import cv2
from key_list import key_check

def main():

    paused = False

    while True:
        if not paused:
            keys = key_check()
            img = screen_cap()
            cv2.imshow('test', img)
            cv2.waitKey(1)

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

if __name__ == "__main__":
    main()
