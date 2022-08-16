import cv2

src = cv2.imread("C:\\Users\\User\\Desktop\\Image\\geese.jpg")

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, dst = cv2.threshold(gray, 100, 255, cv2.THRESH_TRIANGLE)
# 이진화 함수 :: cv2.threshold(src, thresh, maxval, type)
# src : 원본 이미지
# thresh : 임계값
# maxval : 최댓값
# ret : 설정 임계값
# dst : 결과 이미지
# 임계값을 초과한 값은 최댓값으로 변경하고 임계값 이하의 값은 0으로 바꾸는 등의 연산 적용
# 설정 임계값은 일반 적으로 임곗값과 동일하지만 임곗값을 대신 계산해주는 Otsu, Triangle 알고리즘을 사용하면 계산해준 임곗값을 알 수 있다.
# dst = (src > thresh) ? maxval : 0
# 다중 채널 이미지를 입력 이미지로 사용했을 때, 각 채널마다 이미지를 분리해 이진화 연산을 적용한다.

print(ret)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()

# 임계값 형식
# cv2.THRESH_BINARY	        dst = (src > thresh) ? maxval : 0   (임곗값을 초과할 경우 maxval, 아닐 경우 0)
# cv2.THRESH_BINARY_INV	    dst = (src > thresh) ? 0 : maxval   (임곗값을 초과할 경우 0, 아닐 경우 maxval)
# cv2.THRESH_TRUNC	        dst = (src > thresh) ? thresh : src (임곗값을 초과할 경우 thresh, 아닐 경우 변형 없음)
# cv2.THRESH_TOZERO	        dst = (src > thresh) ? src : 0      (임곗값을 초과할 경우 변형 없음, 아닐 경우 0)
# cv2.THRESH_TOZERO_INV	    dst = (src > thresh) ? 0 : src      (임곗값을 초과할 경우 0, 아닐 경우 변형 없음)
# cv2.THRESH_MASK	검은색 이미지로 변경(마스크용)
# cv2.THRESH_OTSU	오츠 알고리즘 적용(단일 채널 이미지에만 적용 가능)
# cv2.THRESH_TRIANGLE	삼각형(Triangle) 알고리즘 적용(단일 채널 이미지에만 적용 가능)

