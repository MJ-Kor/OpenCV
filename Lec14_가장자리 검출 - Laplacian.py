import cv2
src = cv2.imread("C:\\Users\\User\\Desktop\\Image\\apple.jpg")
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
gray_Gauss = cv2.GaussianBlur(gray, (0,0), 1)
laplacian = cv2.Laplacian(gray, cv2.CV_8U, ksize=3)
laplacian2 = cv2.Laplacian(gray_Gauss, cv2.CV_8U, ksize=3, scale=1)
# 라플라시안 함수 :: Laplacian(src, ddepth, ksize, scale, delta, borderType)
# 2차 미분의 형태로 가장자리가 밝은 부분에서 발생한 것인지, 어두운 부분에서 발생한 것인지 알 수 있다.
# 2차 미분 방식은 X축과 Y축을 따라 2차 미분한 합을 의미
# src : 원본 이미지
# ddepth : 출력 이미지 정밀도
# ksize : 라플라시안 필터 크기 설정, 커널 값이 1일 경우 중심 값이 -4인 3X3 Aperture Size를 사용한다.
# scale : 비율
# delta : 오프셋
# borderType : 테두리 외삽법

cv2.imshow("laplacian", laplacian)
cv2.imshow("laplacian2", laplacian2)
cv2.waitKey()
cv2.destroyAllWindows()

