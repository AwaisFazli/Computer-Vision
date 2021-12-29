import numpy as np
import cv2 as cv

# img = cv.imread("Pictures/Cat1.jpg")
# cv.imshow("Cat", img)

blank = np.zeros((500, 500, 3), dtype="uint8")
# blank[:] = 0,255,0
# cv.rectangle(blank, (0,0), (250,500),color=(0,255,0) ,thickness=cv.FILLED)
# cv.circle(blank, (250, 250),(60), (0,255, 0), thickness= cv.FILLED)
# cv.line(blank, (0,0), (255, 255), color = (0,255,0), thickness=10)

cv.putText(blank, "Hello World", (170,255),cv.FONT_HERSHEY_DUPLEX ,1.0, (0,255, 255), 2)
cv.imshow("lank", blank)
cv.waitKey(0)