import cv2 as cv
import numpy as np

img = cv.imread("Pictures/Cat1.jpg")
img = cv.resize(img, (int(img.shape[1]*0.75), int(img.shape[0]*0.75)), interpolation=cv.INTER_CUBIC)

blank = np.zeros(img.shape[:2], dtype="uint8")

#Splitting The Image
b, g, r = cv.split(img) # Splits the image into 3 color Components  (B,G,R)
# It is Depicted As Grascale Where Particular Color Has High Intensity Is Depicted as White And Dark or Black Region Describes
# That In that Region There is No or very Less that particular Color Is


# cv.imshow("Blue", b)
# cv.imshow("Green", g)
# cv.imshow("Red", r)
# cv.imshow("IMG", img)

#Reconstructing The COLORS

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])


print("Blue = ", b.shape)
print("Green = ", g.shape)
print("Red = ", r.shape)
print("Img = ", img.shape) #The Shape Of Img has 3 elements in its tuple the last one describig the color coponents
# While the b , g,r have only 2 elements in tuple because the have only one color components each

#Merging The Components
# merge = cv.merge([b,g,r])
# cv.imshow("Merged", merge)
cv.imshow("Red", red)

# reconstruct = cv.cvtColor(b, cv.COLOR_GRAY2BGR)
# cv.imshow("Recontructing The Blue", reconstruct)

cv.waitKey(0)