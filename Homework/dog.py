import cv2

image=cv2.imread("Lesson 1/Homework/images/dog.jpg",0)

cv2.imwrite("black and white dog.jpg",image)

cv2.imshow("cockapoo",image)

cv2.waitKey(0)
