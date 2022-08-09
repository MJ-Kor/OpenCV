# 래스터 그래픽스 이미지 파일 포맷 : JPG, DIB, GIF, PNG, BMP
# 도트 이미지를 표현하기 위해 매트릭스 구조의 형태로 데이터를 저장
# OpenCV는 이 래스터 그래픽스 이미지 파일 포맷을 쉽게 불러올 수 있는 별도의 함수를 제공한다.
# 압축 해제된 이미지 데이터 구조에 필요한 메모리 할당과 같은 작업 처리, 파일 시그니처를 읽어 적절한 코덱 결정
# 파일 시그니처 = 파일 매직 넘버, 각 파일 형식마다 몇 개의 바이터가 지정
import sys
import cv2

image = cv2.imread("C:\\Users\\User\\Desktop\\Image\\lunar.jpg", cv2.IMREAD_UNCHANGED)
# 이미지 입력함수 :: cv2.imread(fileName, flags)
# fileName : 파일 경로
# fiags : 이미지를 초기에 불러올 때 적용할 초기 상태
# cv2.IMREAD_UNCHANGED : 원본 사용
# cv2.IMREAD_GRAYSCALE : 1 채널, 그레이스케일 적용
# cv2.IMREAD_COLOR : 3 채널, BGR 이미지 사용
# cv2.IMREAD_ANYDEPTH : 이미지에 따라 정밀도를 16/32비트 또는 8비트로 사용
# cv2.IMREAD_ANYCOLOR : 가능한 3 채널, 색상 이미지로 사용
# cv2.IMREAD_REDUCED_GRAYSCALE_2 : 1 채널, 1/2 크기, 그레이스케일 적용
# cv2.IMREAD_REDUCED_GRAYSCALE_4 : 1 채널, 1/4 크기, 그레이스케일 적용
# cv2.IMREAD_REDUCED_GRAYSCALE_8 : 1 채널, 1/8 크기, 그레이스케일 적용
# cv2.IMREAD_REDUCED_COLOR_2 : 3 채널, 1/2 크기, BGR 이미지 사용
# cv2.IMREAD_REDUCED_COLOR_4 : 3 채널, 1/4 크기, BGR 이미지 사용
# cv2.IMREAD_REDUCED_COLOR_8 : 3 채널, 1/8 크기, BGR 이미지 사용

if image is None:
    print("Image load failed")
    sys.exit
cv2.imshow("Moon", image)
cv2.waitKey()
# 이 때 키 대기 함수를 사용하지 않으면 윈도우 창이 유지되지 않고 프로그램이 종료된다.

cv2.destroyAllWindows()

height, width, channel = image.shape
# 여기서 흑백 이미지일 경우 height, width만 얻어짐
# channel : 이미지의 색상 정보
# channel = 3 : 다색 이미지, channel = 1 : 단색 이미지

print(height, width, channel)