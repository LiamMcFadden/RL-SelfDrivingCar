import cv2
from screen_cap import screen_cap
import time
import os
import fnmatch

'''
This script is for generating positve and negative image data for training.

Every INTERVAL seconds a screen shot will be taken and placed in the 'images' 
folder under 'data'. Once complete, you will need to run the 'sort_images.py'
tool to place images in the proper 'negative' or 'positive' folder.
'''

INTERVAL = 3

def main():
	window = 'Rocket League (64-bit, DX11, Cooked)'

	elapsed_time = time.time()

	# get num images to not overwrite old ones
	img_num = len(fnmatch.filter(os.listdir('../data/images'), '*.*'))

	while True:
		if int(time.time() - elapsed_time) == INTERVAL:
			# get img
			img = screen_cap(hwnd=window)

			# save img
			cv2.imwrite('../data/images/img{}.jpg'.format(img_num), img)
			print('img{}.jpg saved...'.format(img_num))
			
			img_num += 1
			elapsed_time = time.time()

if __name__ == '__main__':
	main()