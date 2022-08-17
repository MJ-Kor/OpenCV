import cv2

src = cv2.imread("C:\\Users\\User\\Desktop\\Image\\tomato.jpg")
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

h = cv2.inRange(h, 8, 20)
# 배열 요소의 범위 설정 함수 :: cv2.inRange(src, lowerb, upperb)
# src : 입력 이미지
# lowerb : 낮은 범위
# upperb : 높은 범위

orange = cv2.bitwise_and(hsv, hsv, mask = h)
# 비트 연산 AND :: cv2.bitwise_and(src1, src2, mask)
# src1 : 입력 이미지1
# src2 : 입력 이미지2
# mask : 마스크 영역
orange = cv2.cvtColor(orange, cv2.COLOR_HSV2BGR)

cv2.imshow("orange", orange)
cv2.waitKey()
cv2.destroyAllWindows()
