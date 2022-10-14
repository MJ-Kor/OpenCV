import cv2

src = cv2.imread("C:\\Users\\User\\Desktop\\Image\\convex3.jpg")
dst = src.copy()

gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
ret, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
for i in contours:
    hull = cv2.convexHull(i, clockwise=True)
    for i in hull:
        cv2.circle(dst, i[0], 5, (0, 255, 0), -1)

for i in contours:
    hull2 = cv2.convexHull(i, clockwise=False)
    for i in hull:
        cv2.circle(dst, i[0], 5, (0, 255, 0), -1)

print(hull)
print(hull2)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

