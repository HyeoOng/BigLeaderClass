## 파일처리는 2가지
# 텍스트 파일 - 메모장에서 열어서 글자처럼 보이면 텍스트 파일 - 1byte를 끊어서 뿌림
# 바이너리 파일 - 고유 소프트웨어 필요/
#               - 이미지 파일 중 raw 파일 (bit => [0, 255]가 아닌 1byte(= 8bit =>[-128, 128))에 한 픽셀 표현
import os.path
import math

filename = '../Etc_Raw(squre)/LENA256.RAW'
# 파일 크기 알아내기
fSize = os.path.getsize(filename) # Byte 단위
height = width = int(math.sqrt(fSize))
print(height, 'x', width)

# 메모리 확보 (영상 크기)
image = [ [0 for _ in range(width)] for _ in range(height)]


# 파일 ---> 메모리 로딩
rfp = open(filename, 'rb')
for i in range(height):
    for k in range(width):
        image[i][k] = ord(rfp.read(1)) # ord는 이상한 문자 1바이트를 0-255사이의 숫자로 반환
rfp.close()

# 일부만 확인
for i in range(100, 105, 1):
    for k in range(100, 105, 1):
        print("%3d  " % image[i][k], end='')
    print()
print()


# 함수부(화면 출력)
def display():
    ## 디스플레이 (화면 출력)
    for i in range(250, 255):
        for j in range(250, 255):
            print("%3d  " % image[i][j], end='')
        print()
    print()

# 반전처리
# for i in range(height):
#     for k in range(width):
#         image[i][k] = 255 - image[i][k]
# display()

# 흑백처리
for i in range(height):
    for k in range(width):
        if image[i][k] < 128:
            image[i][k] = 255
        else :
            image[i][k] = 0
display()