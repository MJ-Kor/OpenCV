import cv2

capture = cv2.VideoCapture(0)
# 비디오 출력 클래스 :: cv2.VideoCapture(index)
# index : 카메라의 장치 번호, 내장 장치는 0, 외장 장치는 1~n

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# 카메라 속성 설정 메서드 :: capture.set(propid, value)
# propid : 변경하려는 카메라의 설정
# value : 변경하려는 카메라 설정의 속성 값

while cv2.waitKey(33) < 0:
    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)
# while로 카메라에서 프레임을 지속적으로 받아옴
# cv2.waitkey(delay)는 지정된 시간 동안 키 입력이 있을 때까지 프로그램을 지연시킨다.
# delay : 지연 시간을 의미하며 단위는 milesecond
# delay = 0일 경우 무한 대기를 뜻하며, 키 입력이 없을 때까지 프레임이 넘어가지 않는다.
# cv2.waitkey(delay) != ord('q') 일 경우 q가 입력되면 while문을 종료한다.
# ret은 카메라의 상태가 저장되며 정상 작동할 경우 True를 반환, 작동하지 않을 경우 False를 반환
# frame에 현재 시점의 프레임이 저장
# 이미지 표시함수 :: cv2.imshow(winname, mat)
# winname : 윈도우 창의 제목, 할당 문자열이 변수와 비슷한 역할
# mat : 이미지, 윈도우 창에 할당할 이미지

capture.release()
cv2.destroyAllwindows()
# 메모리 해제 메서드 :: capture.release()
# 윈도우 창 제거 함수 :: cv2.destroyAllWindows()
# 특정 윈도우 창 제거 함수 :: cv2.destroyWindow(winname)