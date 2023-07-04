# 2차원 배열
import random
## 함수
def display():
    ## 디스플레이 (화면 출력)
    for i in range(row):
        for j in range(col):
            print("%3d  " % image[i][j], end='')
        print()
    print()


## 변수
# image = [[0,0,0,0,0],
#          [0,0,0,0,0],
#          [0,0,0,0,0],
#          [0,0,0,0,0],
#          [0,0,0,0,0]]
row, col = 5, 5
image = None

## 메인
## 메모리 할당
image = []
tmpAry = []
for i in range(row):
    for j in range(col):
        tmpAry.append(0)
    image.append(tmpAry)
    tmpAry = []

## 파일 --> 메모리로 로딩(Loading)
# 메모리는 동적( 끄면 사라짐 )
for i in range(row):
    for j in range(col):
        pixel = random.randint(0, 255) # grqyscale(흑백사진) 빛의 정도(0-255)
        image[i][j] = pixel

display()

## 영상처리
#(1) 영상을 50 밝게 처리하자
# for i in range(row):
#     for j in range(col):
#         if (image[i][j] + 50 > 255):
#             image[i][j] = 255
#         else :
#             image[i][j] += 50
display()

# quiz : 100 어둡게
# for i in range(row):
#     for j in range(col):
#         if (image[i][j] - 100 < 0):
#             image[i][j] = 0
#         else :
#             image[i][j] -= 100
# display()
#
# # quiz : 완전 흑백 처리
# for i in range(row):
#     for j in range(col):
#         if (image[i][j] < 128):
#             image[i][j] = 255
#         else :
#             image[i][j] = 0
# display()

#  평균값을 기준으로 흑백 처리
# hap = 0
# for i in range(row):
#     for j in range(col):
#         hap += image[i][j]
# avg = hap / (row * col)
#
# for i in range(row):
#     for j in range(col):
#         if (image[i][j] < avg):
#             image[i][j] = 255
#         else :
#             image[i][j] = 0
# display()

# quiz : 반전처리
# for i in range(row):
#     for j in range(col):
#         image[i][j] = 255 - image[i][j]
# display()