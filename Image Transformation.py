import cv2 as cv
import numpy as np

img = cv.imread("Pictures/Cat1.jpg")

# def translate(img, x, y):
#     transmat = np.float32([[1,0,x], [0,1,y]])
#     print(transmat)
#     dimension = (img.shape[1], img.shape[0])
#     return cv.warpAffine(img, transmat, dimension)
# # x = Right
# # -x = Left
# # y = Down
# # -y = Up
# translated = translate(img, 100, 200)
# cv.imshow("img", translated)

# def rotate(img, angle, rotate_point = None):
#     (height, width) = img.shape[:2]
#     if rotate_point == None:
#         rotate_point = (width//2, height//2)
#     rotmat = cv.getRotationMatrix2D(rotate_point, angle, scale=1)
#     dimension = (width, height)
#     return cv.warpAffine(img, rotmat, dimension)
#
# rotated = rotate(img, 90)
# cv.imshow("Rotated",rotated)

# cat = cv.imread("Pictures/Cat2.jpg")
# resized = cv.resize(cat, (650, 680), interpolation=cv.INTER_CUBIC)
# resized_low = cv.resize(cat, (650, 680), interpolation=cv.INTER_AREA)
# resized_linear = cv.resize(cat, (650, 680), interpolation=cv.INTER_LINEAR)
# cv.imshow("Resized", resized)
# cv.imshow("Resized_low", resized_low)
# cv.imshow("Resized_linear", resized_linear)

# cat = cv.imread("Pictures/Cat2.jpg")
# flip = cv.flip(cat, 2)
# # 0 for upside down, and 1 for rightleft flip
# cv.imshow("Flipped", flip)

# cat = cv.imread("Pictures/Cat2.jpg")
# cropped = cat[100:200, 200:300]
# cv.imshow("crooped", cropped)
cv.waitKey(0)