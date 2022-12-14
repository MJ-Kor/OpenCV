import numpy as np
import cv2
src = cv2.imread("C:\\Users\\User\\Desktop\\Image\\road.jpg")
dst = src.copy()
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 5000, 1500, apertureSize = 5, L2gradient = True)
lines = cv2.HoughLines(canny, 1, np.pi / 180, 150, min_theta = 0, max_theta = np.pi)

for i in lines:
    rho, theta = i[0][0], i[0][1]
    a, b = np.cos(theta), np.sin(theta)
    print(i)
    print("\n")
    x0, y0 = a*rho, b*rho
    point = np.array([x0, y0], np.int32)
    print(point)
    scale = src.shape[0] + src.shape[1]

    x1 = int(x0 + scale * -b)
    y1 = int(y0 + scale * a)
    x2 = int(x0 - scale * -b)
    y2 = int(y0 - scale * a)

    cv2.line(dst, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv2.circle(dst, point, 3, (255, 0, 0), 5, cv2.FILLED)

cv2.imshow("dst", dst)
cv2.imshow("canny", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
