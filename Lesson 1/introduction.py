import cv2

image=cv2.imread("Lesson 1/images/pikachu.png")

cv2.imwrite("black & white Pikachu.jpeg",image)

cv2.imshow("pikachu",image)

cv2.waitKey(0)

b, g, r=cv2.split(image)

cv2.imshow("blue",b)
cv2.waitKey(0)

cv2.imshow("green",g)
cv2.waitKey(0)

cv2.imshow("red",r)
cv2.waitKey(0)

cv2.destroyAllWindows()