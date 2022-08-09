# OpenCV 학습
* 사용 코드 : 해당 실습파일에서 사용되는 코드, 이전 실습에서 사용했던 코드는 작성하지 않음
* 용어 : 해당 실습에 필요한 용어 정리

## Lec1 - OpenCV 설치
OpenCV 설치, opencv-python

## Lec2 - 카메라 출력
* 사용 코드

  * 비디오 출력 클래스 : cv2.VideoCapture(index)
  * 카메라 속성 설정 메서드 : cv2.VideoCapture(index).set(propid, value)
  * 키 입력 대기 함수 : cv2.waitKey(delay)
  * 이미지 표시 함수 : cv2.imshow(winname, mat)
  * 메모리 해제 메서드 : cv2.VideoCapture(index).release()
  * 모든 윈도우 창 제거 함수 : cv2.destroyAllWindows()
  * 특정 윈도우 창 제거 함수 : cv2.destroyWindow(winname)
  
## Lec3 - 이미지 출력
* 사용 코드
  * 이미지 입력 함수 : cv2.imread(filename, flags)
  * 이미지 속성(height, width, channel을 튜플로 반환) : image.shape
  
* 용어
  * 크기 : 이미지의 높이와 너비
  * 정밀도 : 이미지 처리 결과의 정밀성, 유효 비트가 많을 수록 더 정밀해진다.
  * 채널 : 이미지의 색상 정보, 채널은 각각의 색깔에 해당, RGB 이미지는 3개의 채널을 가진 이미지
  
## Lec4 - 비디오 출력
* 사용 코드
  * 비디오 출력 클래스 : cv2.VideoCapture(fileName)
  * 비디오 속성 반환 메서드 : cv2.VideoCapture.get(property)
  
* VideoCapture 메서드
  * capture.isOpened() : 동영상 파일 열기 성공 여부 확인
  * capture.open(filename) : 동영상 파일 열기
  * capture.set(propid, value) : 동영상 속성 설정
  * capture.get(propid)	: 동영상 속성 반환
  * capture.release()	 : 동영상 파일을 닫고 메모리 해제
  
* VideoCapture 속성

속성 | 의미 | 너비
-----|----- |-----|
cv2.CAP_PROP_FRAME_WIDTH	| 프레임의 너비	| -
cv2.CAP_PROP_FRAME_HEIGHT	|프레임의 높이	|-
cv2.CAP_PROP_FRAME_COUNT	|총 프레임 수	|-
cv2.CAP_PROP_FPS	|프레임 속도	|-
cv2.CAP_PROP_FOURCC	|코덱 코드	|-
cv2.CAP_PROP_BRIGHTNESS	|이미지 밝기	|카메라만 해당
cv2.CAP_PROP_CONTRAST	|이미지 대비	|카메라만 해당
cv2.CAP_PROP_SATURATION	|이미지 채도	|카메라만 해당
cv2.CAP_PROP_HUE	|이미지 색상	|카메라만 해당
cv2.CAP_PROP_GAIN	|이미지 게인	|카메라만 해당
cv2.CAP_PROP_EXPOSURE	|이미지 노출	|카메라만 해당
cv2.CAP_PROP_POS_MSEC	|프레임 재생 시간	|ms 반환
cv2.CAP_PROP_POS_FRAMES	|현재 프레임	|프레임의 총 개수 미만
CAP_PROP_POS_AVI_RATIO	|비디오 파일 상대 위치	|0 = 시작, 1 = 끝

## Lec5 - 대칭
* 원리
  * 변환할 행렬에 대해 2X2 행렬(x축, y축, y=x 반사 표준행렬)을 왼쪽 곱셈한다.
  
* 사용 코드
  * 대칭 함수 : cv2.flip(src, flipCode)
  * filpCode < 0은 y=x 대칭
  * flipCode = 0은 x축 대칭
  * flipCode > 0은 y축 대칭
  
## Lec6 - 회전
* 원리
  * 1. 좌표 값을 회전시키는 회전 행렬 : 원점을 중심으로 좌표 값을 회전시켜 매핑
  * 2. 좌표 축을 회전시키는 회전 행렬 (OpenCV) : 원점을 중심으로 행렬 자체를 회전시켜 새로운 행렬의 값을 구성
  
* 사용 코드
  * 2X3 회전 행렬 생성 함수 : cv2.getRotationMatrix2D(center, angle, scale)
  * 아핀 변환 함수 : cv2.warpAffine(src, matrix, (width, height))
  
* 용어
  * 아핀 공간 : 유클리드 공간의 아핀 기하학적 성질들을 일반화해서 만들어지는 구조이다. 아핀 공간에서는 점에서 점을 빼서 벡터를 얻거나 점에 벡터를 더해 다른 점을 얻을 수는 있지만 원점이 없으므로 점과 점을 더할 수는 없다. 원점이 없음
  
## Lec7 - 확대 & 축소
* 원리 
  * 이미지 피라미드를 활용해 이미지의 크기를 원하는 단계까지 샘플링한다.
  * 가우시안 피라미드와 라플라시안 피라미드를 활용한다.

* 사용 코드
  * 이미지 확대 함수 : cv2.pyrUp(src, dstSize, borderType)
  * 이미지 축소 함수 : cv2.pyrDown(src, dstSize, borderType)
  
* 용어 
  * 이미지 피라미드 : 해상도에 따른 다단계 이미지 세트
  * 가우시안 피라미드 
  
    * Downsampling은 하위 단계 이미지의 짝수열, 짝수행에 해당하는 픽셀을 제거하여 이미지 해상도를 줄인다. 
    * Upsampling은 반대로 픽셀을 추가하여 이미지 해상도를 높인다. 
    * 이때 생성된 이미지는 블러링 효과를 낸 듯한 이미지로 보이게 된다.
  * 라플라시안 피라미드 : 가우시안 피라미드 결과로 생성한다. 
  
    * 1. 원본을 가우시안 피라미드 상위 단계 이미지2로 생성한다.
    * 2. 이미지2를 다시 가우시안 피라미드 하위 단계 이미지3로 생성한다.
    * 3. 원본과 이미지3은 해상도는 같지만 완벽히 같지 않다
    * 4. 여기서 원본 - 이미지3을 연산한 것이 라플라시안 피라미드 최하위 단계이다.
  * Upsampling : 원본 이미지에서 크기를 확대하는 것 (하위 단계 이미지) 
  * Downsampling : 원본 이미지에서 크기를 축소하는 것 (상위 단계 이미지)
  * 테두리 외삽법 : 이미지를 확대하거나 축소할 경우, 이미지 영역 밖의 픽셀은 추정을 통해 값을 할당하는 방법
  
## Lec8
## Lec9
## Lec10
