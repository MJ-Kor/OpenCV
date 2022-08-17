import cv2

src = cv2.imread("C:\\Users\\User\\Desktop\\Image\\tomato.jpg")
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
# 채널 분리 함수 :: cv2.split(img)
# 입력 이미지의 채널을 분리하여 배열 형태로 반환한다.

cv2.imshow("hsv", hsv)
cv2.imshow("h", h)
cv2.imshow("s", s)
cv2.imshow("v", v)
cv2.waitKey()
cv2.destroyAllWindows()
