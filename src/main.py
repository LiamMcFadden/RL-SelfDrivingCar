import cv2
from screen_cap import screen_cap
import time


def main():
	window = 'Rocket League (64-bit, DX11, Cooked)'

	# elapsed time between frames
	elapsed = 0

	while True:
		# quit on press of 'q'
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

		# get img
		img = screen_cap(hwnd=window)

		# calc fps
		fps = str(1 // (time.time() - elapsed))
		elapsed = time.time()

		# put fps on img and display it
		img = cv2.putText(img, "{} FPS".format(fps), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 1, cv2.LINE_AA)
		cv2.imshow('img', img)

		# find ball on screen
		
		
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()