import cv2 as cv
import numpy as np

img = cv.imread("Pictures/Cat1.jpg")
height = int((img.shape[1]*0.75))
width = int((img.shape[0]*0.75))

img = cv.resize(img, (height, width), interpolation=cv.INTER_CUBIC)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# blur = cv.GaussianBlur(gray,(5,5), cv.BORDER_DEFAULT )
canny = cv.Canny(img, 125, 125)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) # another way of finding contours
# threshold one actually set the floor limit that pixel having intensity below this would not e considered as be set to black
# and and if value is above 125 it would e set to 255 (max_value) which is white
#and type is actually the thresholding type and as we are binarizing th image so we will use THRESH_BINARY

contours, hierarchy = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# findcontours return actually 2 values one ins contours and other is heirarchy we will discuss hierarcy later on
# it takes the image to get find contours second it asks for the mode to be used
# Retr_list returns all the contours
# Retr_External retrives only the external contours
# Retr_Tree retuurn all the heirarchical contours
# method is actually the contour approximation method
# Chain_APPROX_NONE does nothing
# CHAIN_APPROX_SIMPLE compress all the contours into simple ones which makes more sense

print(len(contours)) # as it is the list of contours find we can find how many number of have been found
blank = np.zeros(img.shape, dtype="uint8")

cv.drawContours(blank, contours, -1, (0,255,255), 1) #drawing contours on blank
# requires a source image on to be drawn the contours
# require list of contours
# contour index that how many or which contours to be drawn (-1for all)
# specify the color
# the thickness of contours to be drawn

# cv.imshow("cont", cont)
cv.imshow("Blank", blank)
cv.imshow("Contour", canny)
cv.waitKey(0)