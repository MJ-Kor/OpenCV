import cv2

src = cv2.imread("C:\\Users\\User\\Desktop\\Image\\tomato.jpg")
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

print(h)
print(h.shape)
print(hsv.shape)
cv2.imshow("hsv", hsv)
cv2.imshow("h", h)
cv2.imshow("s", s)
cv2.imshow("v", v)
cv2.waitKey()
cv2.destroyAllWindows()
