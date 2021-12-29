import cv2 as cv

# img  = cv.imread("/home/shahrukh/Desktop/Awais/OpenCV/Pictures/Cat1.jpg")
#
# cv.imshow("Cat1",img)
# capture = cv.VideoCapture(0)
# while True:
#     isTrue, frame = capture.read()
#     cv.imshow("Video", frame)
#     if cv.waitKey(20) & 0xFF == ord("d"):
#         break
# capture.release()
# cv.destroyAllWindows()

def rescale(frame, ratio):
    width = int(frame.shape[1]*ratio)
    height = int(frame.shape[0]*ratio)
    dimension = (width, height)
    # print(frame.shape[0])

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

# img  = cv.imread("/home/shahrukh/Desktop/Awais/OpenCV/Pictures/Cat1.jpg")
# img_resized = rescale(img, 0.75)
# cv.imshow("Resized",img_resized)
# cv.waitKey(0)
#
video = cv.VideoCapture(0)

while True:
    isTrue, frame = video.read()
    resized = rescale(frame, 0.76)
    cv.imshow("video", resized)
    print(isTrue)

    if cv.waitKey(20) & 0xFF == ord("f"):
        break

video.release()
cv.destroyAllWindows()