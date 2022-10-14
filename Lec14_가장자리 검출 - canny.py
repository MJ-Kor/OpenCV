import cv2
src = cv2.imread("C:\\Users\\User\\Desktop\\Image\\apple.jpg")

canny = cv2.Canny(src, 50, 180, L2gradient=True)
# 캐니 함수 :: cv.Canny(src, threshold1, threshold2, apertureSize, L2gradient)
# 라플라스 필터 방식을 개선한 방식으로 x와 y에 대해 1차 미분을 계산한 다음 네 방향으로 미분한다.
# 네 방향으로 미분한 결과로 극댓값을 갖는 지점들이 가장자리가 된다.
# 노이즈에 민감하지 않고, 성능이 월등히 좋아 강한 가장자리를 검출하는 데 많이 쓰인다.
# src : 원본 이미지
# threshold1 : 하위 임곗값, 다른 엣지와의 인접 부분에 있어 엣지인지 아닌지를 판단하는 임계값
# threshold2 : 상위 임곗값, 엣지인지 아닌지 판단하는 임계값
# apertureSize : 소벨 연산자 마스크 크기
# L2 gradient : L2 그레디언트

cv2.imshow("canny", canny)
cv2.waitKey()
cv2.destroyAllWindows()

