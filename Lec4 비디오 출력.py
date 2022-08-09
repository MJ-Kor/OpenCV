# OpenCv는 FFmpeg를 지원하므로 avi나 mp4등 다양한 형식의 동영상 파일을 손쉽게 읽을 수 있습니다.
# GIF 확장자는 프레임이 존재하므로, 동영상 파일을 읽는 방법과 동일하게 처리합니다.

import cv2

capture = cv2.VideoCapture("C:\\Users\\User\\Desktop\\Image\\Star.mp4")
# 비디오 출력 클래스 :: cv2.VideoCapture 도용사

while cv2.waitKey(33) < 0:
    if capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT):
        capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
    # 동영상의 현재 프레임 수 (cv2.CAP_PROP_POS_FRAMES)와 동영상 총 프레임 수 (cv2.CAP_PROP_FRAME_COUNT)를 받아와서 두 프레임을 비교한다.
    # 현재 프레임 수가 총 프레임 수와 같다면, 현재 재생되고 있는 프레임은 가장 마지막이다.
    # 마지막 프레임은 동영상이 종료되는 시점이 되므로, 동영상의 현재 프레임을 초기화 한다.
    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)

capture.release()
cv2.destroyAllWindows()

# VideoCapture 메서드
# capture.isOpened()	        동영상 파일 열기 성공 여부 확인
# capture.open(filename)	    동영상 파일 열기
# capture.set(propid, value)	동영상 속성 설정
# capture.get(propid)	        동영상 속성 반환
# capture.release()	            동영상 파일을 닫고 메모리 해제

# VideoCapture 속성
# cv2.CAP_PROP_FRAME_WIDTH	프레임의 너비	            -
# cv2.CAP_PROP_FRAME_HEIGHT	프레임의 높이	            -
# cv2.CAP_PROP_FRAME_COUNT	총 프레임 수	            -
# cv2.CAP_PROP_FPS	        프레임 속도	            -
# cv2.CAP_PROP_FOURCC	    코덱 코드	            -
# cv2.CAP_PROP_BRIGHTNESS	이미지 밝기	        카메라만 해당
# cv2.CAP_PROP_CONTRAST	    이미지 대비	        카메라만 해당
# cv2.CAP_PROP_SATURATION	이미지 채도	        카메라만 해당
# cv2.CAP_PROP_HUE	        이미지 색상	        카메라만 해당
# cv2.CAP_PROP_GAIN	        이미지 게인	        카메라만 해당
# cv2.CAP_PROP_EXPOSURE	    이미지 노출	        카메라만 해당
# cv2.CAP_PROP_POS_MSEC	    프레임 재생 시간	    ms 반환
# cv2.CAP_PROP_POS_FRAMES	현재 프레임	        프레임의 총 개수 미만
# CAP_PROP_POS_AVI_RATIO	비디오 파일 상대 위치	0 = 시작, 1 = 끝