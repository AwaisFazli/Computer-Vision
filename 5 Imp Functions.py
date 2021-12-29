import cv2 as cv

img = cv.imread("Pictures/vlcsnap-2020-10-21-13h58m57s918_1.png")

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# blur = cv.blur(img, (3,3), cv.BORDER_DEFAULT)
# canny = cv.Canny(img, 125, 125)
# dilated = cv.dilate(img, (7,7), iterations=3)
# eroded = cv.erode(img, (3,3), 3)
# resize = cv.resize(img, (500,500))
# cropped = img[100:400, 200:500]

cv.imshow("Org", img)
cv.waitKey(0)