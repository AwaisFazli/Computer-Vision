import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("Pictures/Cat1.jpg")
img = cv.resize(img, (int(img.shape[1]*0.75), int(img.shape[0]*0.75)), interpolation=cv.INTER_CUBIC)

#BGR to GRAY Scale (BGR The OpenCV Default Way Of Reading Images) BGR = Blue, Green , Red
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

#BGR to L*a*b
lab = cv.cvtColor(hsv, cv.COLOR_BGR2LAB)

#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

cv.imshow("IMG", img)
# cv.imshow("Converted", lab)

# plt.imshow(rgb) #matplotlib read images in RBG format which is inverse Of BGR thats why it shows iverse colors
## First convert BGR to RGB to get actual picture to be displayed by Matplotlib
plt.show()
cv.waitKey(0)
