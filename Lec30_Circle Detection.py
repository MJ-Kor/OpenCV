import numpy as np
import cv2

src = cv2.imread("C:\\Users\\User\\Desktop\\Image\\Circle.jpg")
dst = src.copy()
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 200, param1 = 250, param2 = 2, minRadius = 80, maxRadius = 120)

for i in circles[0]:
    center = np.array([i[0], i[1]], np.int32)
    cv2.circle(dst, center, int(i[2]), (255, 255, 255), 5)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

