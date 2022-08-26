import cv2
src = cv2.imread("C:\\Users\\User\\Desktop\\Image\\apple.jpg")
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

sobel_x = cv2.Sobel(gray, cv2.CV_8U, dx = 1, dy = 0, ksize = 3, scale = 3)
sobel_y = cv2.Sobel(gray, cv2.CV_8U, dx = 0, dy = 1, ksize = 3, scale = 3)
sum = abs(sobel_x) + abs(sobel_y)
# 소벨 함수 :: cv2.Sobel(src, ddepth, dx, dy, ksize, scale, delta, borderType)
# 인접한 픽셀들의 차이로 기울기의 크기를 구한다.
# src : 원본 이미지
# ddepth : 출력 이미지 데이터 타입, default = -1 (입력과 같은 타입)
# dx : x방향 미분 차수
# dy : y방향 미분 차수
# ksize : 커널 크기, 1,3,5,7 등의 홀수 값 사용, 최대 31까지 설정 가능
# scale : 연산 결과에 추가적으로 곱할 값, default = 1
# delta : 연산 결과에 추가적으로 더할 값, default = 0
# borderType : 테두리 외삽법
# 비율과 오프셋은 출력 이미지를 반환하기 전에 적용되며, 주로 시각적으로 확인하기 위해 적용

cv2.imshow("sobel_x", sobel_x)
cv2.imshow("sobel_y", sobel_y)
cv2.imshow("sum", sum)
cv2.waitKey()
cv2.destroyAllWindows()
