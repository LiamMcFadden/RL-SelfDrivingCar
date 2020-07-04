from screen_cap import screen_cap
import os
import time
import cv2
from key_list import key_check

def main():

    paused = False
    elapsed = time.time()

    while True:
        if not paused:
            img = screen_cap()
            cv2.imshow('test', img)

            if cv2.waitKey(1) & 0xFF == ord('q'):
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

        fps = 1//(time.time() - elapsed)
        print("{} FPS".format(fps))
        elapsed = time.time()

if __name__ == "__main__":
    main()
