import cv2
import fnmatch
import os

'''
Destroys old window, writes to sorted path, and removes image from 'images' folder.

Parameters
----------
sorted_path : str
	Path of sorted location for img
img_path : str
	Path to old location of img
img : image
	Screenshot of application
'''
def sort_img(sorted_path, img_path, img):
	# destroy old window
	cv2.destroyAllWindows()
	# write to new folder
	cv2.imwrite(sorted_path, img)
	# delete image from images folder
	os.remove(img_path)

	print('{} sorted...'.format(sorted_path))

def main():
	# index of image in 'images' folder
	i = 0
	# path to data folder
	data_path = '../data'
	img = cv2.imread('{}/images/img{}.jpg'.format(data_path, i))

	# get number of positive and negative files already sorted
	pos = len(fnmatch.filter(os.listdir('{}/positive'.format(data_path)), '*.*'))
	neg = len(fnmatch.filter(os.listdir('{}/negative'.format(data_path)), '*.*'))

	while img is not None:
		# capture image
		cv2.imshow('img{}'.format(i), img)
		cv2.setWindowProperty('img{}'.format(i), cv2.WND_PROP_TOPMOST, 1)
		img_path = '{}/images/img{}.jpg'.format(data_path, i)
		img = cv2.imread(img_path)
			
		# positive image
		if cv2.waitKey(10) & 0xFF == ord('p'):
			sorted_path = '{}/positive/pos{}.jpg'.format(data_path, pos)
			i += 1
			pos += 1

			sort_img(sorted_path, img_path, img)

		# negative image
		elif cv2.waitKey(10) & 0xFF == ord('n'):
			sorted_path = '{}/negative/neg{}.jpg'.format(data_path, neg)
			i += 1
			neg += 1

			sort_img(sorted_path, img_path, img)

		elif cv2.waitKey(10) & 0xFF == ord('q'):
			break


if __name__ == '__main__':
	main()