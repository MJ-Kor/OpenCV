import cv2
src = cv2.imread("C:\\Users\\User\\Desktop\\Image\\fruits.jpg")
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 3)
# 소벨 함수 :: cv2.Sobel(src, ddepth, dx, dy, ksize, scale, delta, borderType)
# 인접한 픽셀들의 차이로 기울기의 크기를 구한다.
# src : 원본 이미지
# ddepth : 출력 이미지 정밀도
# dx : x방향 미분 차수
# dy : y방향 미분 차수
# ksize : 커널 크기, 1,3,5,7 등의 홀수 값 사용, 최대 31까지 설정 가능
# scale : 비율
# delta : 오프셋
# borderType : 테두리 외삽법
# 비율과 오프셋은 출력 이미지를 반환하기 전에 적용되며, 주로 시각적으로 확인하기 위해 적용

laplacian = cv2.Laplacian(gray, cv2.CV_8U, ksize=3)
# 라플라시안 함수 :: Laplacian(src, ddepth, ksize, scale, delta, borderType)
# 2차 미분의 형태로 가장자리가 밝은 부분에서 발생한 것인지, 어두운 부분에서 발생한 것인지 알 수 있다.
# 2차 미분 방식은 X축과 Y축을 따라 2차 미분한 합을 의미
# src : 원본 이미지
# ddepth : 출력 이미지 정밀도
# ksize : 라플라시안 필터 크기 설정, 커널 값이 1일 경우 중심 값이 -4인 3X3 Aperture Size를 사용한다.
# scale : 비율
# delta : 오프셋
# borderType : 테두리 외삽법

canny = cv2.Canny(src, 100, 255)
# 캐니 함수 :: cv.Canny(src, threshold1, threshold2, apertureSize, L2gradient)
# 라플라스 필터 방식을 개선한 방식으로 x와 y에 대해 1차 미분을 계산한 다음 네 방향으로 미분한다.
# 네 방향으로 미분한 결과로 극댓값을 갖는 지점들이 가장자리가 된다.
# 노이즈에 민감하지 않고, 성능이 월등히 좋아 강한 가장자리를 검출하는 데 많이 쓰인다.
# src : 원본 이미지
# threshold1 : 하위 임곗값, 다른 엣지와의 인접 부분에 있어 엣지인지 아닌지를 판단하는 임계값
# threshold2 : 상위 임곗값, 엣지인지 아닌지 판단하는 임계값
# apertureSize : 소벨 연산자 마스크 크기
# L2 gradient : L2 그레디언트

cv2.imshow("sobel", sobel)
cv2.imshow("laplacian", laplacian)
cv2.imshow("canny", canny)

cv2.waitKey()
cv2.destroyAllWindows()