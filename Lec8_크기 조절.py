import cv2

src = cv2.imread("C:\\Users\\User\\Desktop\\Image\\ara.jpg", cv2.IMREAD_COLOR)

dst = cv2.resize(src, dsize=(640, 480), interpolation=cv2.INTER_AREA)
dst2 = cv2.resize(src, dsize=(0, 0), fx=0.3, fy=0.7, interpolation=cv2.INTER_LINEAR)
# 이미지 크기 조절 함수 :: cv2.resize(src, dstSize, fx, fy, interpolation)
# src : 원본 이미지
# dstSize : 절대 크기, dsize.width = round(fx X src.cols), dsize.height = round(fy X src.rows)
# fx : 상대 크기, dsize.width/src.cols
# fy : 상대 크기, dsize.height/src.rows
# 상대 크기는 절대 크기에 (0, 0)을 할당한 다음에 상대 크기의 값을 할당해 사용, 이유는 fx, fy에서 계산된 크기가 dsize에 할당되기 때문

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)
cv2.waitKey()
cv2.destroyAllWindows()

# interpolation 속성
# cv2.INTER_NEAREST	        이웃 보간법
# cv2.INTER_LINEAR	        쌍 선형 보간법
# cv2.INTER_LINEAR_EXACT	비트 쌍 선형 보간법
# cv2.INTER_CUBIC	        바이큐빅 보간법
# cv2.INTER_AREA	        영역 보간법
# cv2.INTER_LANCZOS4	    Lanczos 보간법

# 확대하는 경우 바이큐빅이나 쌍 선형 보간법 자주 사용
# 축소하는 경우 영역 보간법 자주 사용
# 영역 보간법으로 확대하는 경우 이웃 보간법과 비슷한 결과 반영