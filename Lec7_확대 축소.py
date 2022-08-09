# 이미지 피라미드를 활용해 이미지 크기를 원하는 단계까지 샘플링한다.
# 업 샘플링 : 원본을 확대하는 것, 하위 단계의 이미지 생성
# 다운 샘플링 : 원본을 축소하는 것, 상위 단계의 이미지 생성
# 가우시안 피라미드, 라플라시안 피라미드 활용

import cv2

src = cv2.imread("C:\\Users\\User\\Desktop\\Image\\ara.jpg", cv2.IMREAD_COLOR)
height, width, channel = src.shape

dst = cv2.pyrUp(src, dstsize=(width * 2, height * 2), borderType=cv2.BORDER_DEFAULT)
# 이미지 2배 확대 함수 :: cv2.pyrUp(src, dstSize, borderType)
# src : 원본 이미지
# dstSize : 출력 이미지 크기, 매우 세밀한 크기 조정을 필요로 할 때 사용
# borderType : 테두리 외삼법, 이미지를 확대하거나 축소할 경우, 이미지 영역 밖의 픽셀은 추정을 통해 값을 할당해야 한다. 따라서 이미지 밖의 픽셀을 외삽하는 데 사용되는 테두리 모드이다.
# 확대 함수는 BORDER_DEFAULT의 픽셀 외삼법만 사용할 수 있다.
# dstSize : |dstSize.width - src.colsX2| <= (dstSize.width mod 2)
#           |dstSize.height - src.rowsX2| <= (dstSize.height mod 2)

dst2 = cv2.pyrDown(src)
# 이미지 2배 축소 함수 :: cv2.pyrDown(src, dstSize, borderType)
# 축소 함수는 BORDER_CONSTANT의 픽셀 외삼법만 사용할 수 있다.
# dstSize : |dstSize.widthX2 - src.cols| <= 2
#           |dstSize.heightX2 - src.rows| <= 2


cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)
cv2.waitKey()
cv2.destroyAllWindows()

# 픽셀 외삼법 종류
# cv2.BORDER_CONSTANT	    iiiiii | abcdefgh | iiiiiii
# cv2.BORDER_REPLICATE	    aaaaaa | abcdefgh | hhhhhhh
# cv2.BORDER_REFLECT	    fedcba | abcdefgh | hgfedcb
# cv2.BORDER_WRAP	        cdefgh | abcdefgh | abcdefg
# cv2.BORDER_REFLECT_101	gfedcb | abcdefgh | gfedcba
# cv2.BORDER_REFLECT101	    gfedcb | abcdefgh | gfedcba
# cv2.BORDER_DEFAULT	    gfedcb | abcdefgh | gfedcba
# cv2.BORDER_TRANSPARENT	uvwxyz | abcdefgh | ijklmno
# cv2.BORDER_ISOLATED	    관심 영역 (ROI) 밖은 고려하지 않음



