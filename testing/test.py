import cv2
# import matplotlib.pyplot as plt
# import cvlib as cv
# from cvlib.object_detection import draw_bbox

# img = cv2.imread('./img/apple.jpeg')
# bbox, label, conf = cv.detect_common_objects(img)
# output_image = draw_bbox(img, bbox, label, conf)
# plt.imshow(output_image)
# plt.show()

dim = (1280, 768)

img = cv2.imread("sample.JPG")

roi = img[244:524, 500:780]

cv2.imshow("test", roi)
cv2.waitKey(0)


