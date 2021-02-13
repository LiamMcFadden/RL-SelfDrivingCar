from screen_cap import screen_cap
import os
import time
import cv2
from key_list import key_check
from process_image import process_image

def main():

    paused = False
    elapsed = time.time()
    # name of window to capture
    hwnd = "Rocket League (64-bit, DX11, Cooked)"
    img_index = 0

    while True:
        if not paused:
            # get screen capture
            img = screen_cap(hwnd=hwnd)

            img = process_image(img, img_index)
            if img_index == 6:
                img_index = 0
            else:
                img_index += 1

            # calc fps
            fps = 1//(time.time() - elapsed)
            elapsed = time.time()

            # put fps on stream
            fps = str(fps)
            img = cv2.putText(img, "{} FPS".format(fps), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.imshow('test', img)

            # handle quit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        else:
            # handle quit
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


if __name__ == "__main__":
    main()
