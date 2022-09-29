import cv2

src = cv2.imread("C:\\Users\\User\\Desktop\\Image\\convex3.jpg")
dst = src.copy()

gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
ret, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

x, y= gray.shape

M = cv2.moments(binary, True)

cX = int(M['m10']/M['m00'])
cY = int(M['m01']/M['m00'])

cv2.circle(dst,(cX, cY), 3, (255, 0, 0), -1)

print(M['m00'])
print(M['m10'])
print(x, y, x*y)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

