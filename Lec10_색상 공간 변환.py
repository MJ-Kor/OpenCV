# 본래의 색상 공간에서 다른 색상 공간으로 변환할 때 사용
# 데이터 타입을 같게 유지하고 채널을 변환
# 입력된 이미지는 8비트, 16비트, 32비트의 정밀도를 갖는 배열을 사용
# 출력된 이미지는 입력된 이미지의 이미지 크기와 정밀도가 동일한 배열이 된다.
# 채널의 수가 감소하게 되어 이미지 내부의 데이터는 설정한 색상 공간과 일치하는 값으로 변환되며, 데이터 값이 변경되거나 채널 순서가 변경될 수 있다.

import cv2

src = cv2.imread("C:\\Users\\User\\Desktop\\Image\\crow.jpg", cv2.IMREAD_COLOR)
dst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 색상 공간 변환 함수 :: cv2.cv2Color(src, code, dstCn)
# src : 원본 이미지
# code : 색상 변환 코드, 원본 이미지 색상 공간2결과 이미지 색상 공간을 의미
# 원본 이미지 색상 공간은 원본 이미지와 일치해야 한다.
# 출력 채널은 출력 이미지에 필요한 채널의 수를 설정한다.
# BGR은 RGB 색상 채널 의미(BYTE 역순)
# 출력 채널은 기본값을 사용하여 자동으로 채널의 수를 결정하게 한다.

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()

# 채널 범위
# CV_8U	0 ~ 255
# CV_16U	0 ~ 65535
# CV_32F	0 ~ 1

# 색상 공간 코드
# BGR	        Blue, Green, Red 채널	            -
# BGRA	        Blue, Green, Red, Alpha 채널	        -
# RGB	        Red, Green, Blue 채널	            -
# RGBA	        Red, Green, Blue, Alpha 채널	        -
# GRAY      	단일 채널	그레이스케일
# BGR565	    Blue, Green, Red 채널	            16 비트 이미지
# XYZ	        X, Y, Z 채널	                        CIE 1931 색 공간
# YCrCb	        Y, Cr, Cb 채널	                    YCC (크로마)
# HSV	        Hue, Saturation, Value 채널	        색상, 채도, 명도
# Lab	        L, a, b 채널	                        반사율, 색도1, 색도2
# Luv	        L, u, v 채널	                        CIE Luv
# HLS	        Hue, Lightness, Saturation 채널	    색상, 밝기, 채도
# YUV	        Y, U, V 채널	                        밝기, 색상1, 색상2
# BG, GB, RG	디모자이킹	                        단일 색상 공간으로 변경
# _EA	        디모자이킹	                        가장자리 인식
# _VNG	        디모자이킹	                        그라데이션 사용