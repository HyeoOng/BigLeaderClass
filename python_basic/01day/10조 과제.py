from tkinter import *
import os.path
import math

## 함수

def qSort(li,l1,l2):  #퀵소트 정렬
    print(*li)
    if l1>=l2:
        return
    t=l1 # 피봇(기준)
    a=l1+1
    b=l2
    while a<=b:
        while a<=l2 and li[a]<=li[t]:
            a+=1
        while b>l1 and li[b]>=li[t]:
            b-=1
        if a>b:# 이식 덕분에 피봇이 제 자리를 찾아감.
            li[b], li[t] = li[t], li[b]
        else:
            li[b], li[a] = li[a], li[b]
    qSort(li,l1,b-1)
    qSort(li,b+1,l2)
def displayImage():
    global window, canvas, paper, height, width, filename
    if canvas != None:
        canvas.destroy()

    canvas = Canvas(window, height=512, width=512)
    paper = PhotoImage(height=512, width=512)
    canvas.create_image((512 / 2, 512 / 2), image=paper, state='normal')

    for i in range(height):
        for k in range(width):
            r = g = b = image[i][k]
            paper.put('#%02x%02x%02x' % (r, g, b), (k, i))  # r, g, b를 %02x 순서대로 (i,k)위치에 찍어라
    canvas.pack()

# 반전처리
def reverseImage():
    for i in range(height):
        for k in range(width):
            image[i][k] = 255 - image[i][k]
    displayImage()

# 밝게
def brightImage():
    for i in range(height):
        for k in range(width):
            if (image[i][k] + 50 > 255):
                image[i][k] = 255
            else:
                image[i][k] += 50
    displayImage()

# 어둡게
def darkImage():
    for i in range(height):
        for k in range(width):
            if (image[i][k] - 50 < 0):
                image[i][k] = 0
            else:
                image[i][k] -= 50
    displayImage()

# 흑백처리(127)
def blackImage_127():
    for i in range(height):
        for k in range(width):
            if (image[i][k] < 127):
                image[i][k] = 255
            else :
                image[i][k] = 0
    displayImage()

# 흑백처리(평균값)
def blackImage_mean():
    mean = 0
    for i in range(height):
        for k in range(width):
            mean += image[i][k]
    mean = mean / (height * width)
    for i in range(height):
        for k in range(width):
            if (image[i][k] < mean):
                image[i][k] = 255
            else:
                image[i][k] = 0
    displayImage()

# 흑백처리(중앙값)
def blackImage_center():
    center = 0
    li = [image[i][k] for i in range(height) for k in range(width)]
    # 퀵소트 이용
    qSort(li, 0, len(li)-1)
    if len(li) % 2 == 0:
        center = (li[len(li)/2 -1] + li[len(li)/2])/2
    else :
        center = li[len(li)//2]
    for i in range(height):
        for k in range(width):
            if (image[i][k] < center):
                image[i][k] = 255
            else:
                image[i][k] = 0
    displayImage()

# 90도 회전
def rotateImage_90():
    global image
    rotated_image = [[0 for _ in range(height)] for _ in range(width)]
    # rotated_image = image
    for i in range(height):
        for k in range(width):
            rotated_image[k][height - i - 1] = image[i][k]
    image = rotated_image
    displayImage()

# # 180도 회전
def rotateImage_180():
    global image
    rotated_image = [[0 for _ in range(height)] for _ in range(width)]
    for i in range(height):
        for k in range(width):
            rotated_image[height-i-1][height-k-1] = image[i][k]
    image = rotated_image
    displayImage()

# 270도 회전
def rotateImage_270():
    global image
    rotated_image = [[0 for _ in range(height)] for _ in range(width)]
    for i in range(height):
        for k in range(width):
            rotated_image[height-k-1][i] = image[i][k]
    image = rotated_image
    displayImage()

# 좌우 미러링
def reverseLRImage():
    global image, height, width
    reversed_image = [[0 for _ in range(height)] for _ in range(width)]
    for i in range(height):
        for k in range(width):
            reversed_image[i][k] = image[i][width - k - 1]
    image = reversed_image
    displayImage()

# 상하 미러링
def reverseUPImage():
    global image, height, width
    reversed_image = [[0 for _ in range(height)] for _ in range(width)]
    for i in range(height):
        for k in range(width):
            reversed_image[i][k] = image[height - i - 1][k]
    image = reversed_image
    displayImage()

# # 파라볼라 연산
def parabolaImage():
    for i in range(height):
        for k in range(width):
            image[i][k] = int(255 * (image[i][k]/128 - 1) **2)
    displayImage()

# # 감마 연산
def gammaImage():
    for i in range(height):
        for k in range(width):
            gamma_val = int(image[i][k]**(1.0/2.2)) # 2.2가 감마값에 가장 근접한 값
            if gamma_val>255:
                image[i][k] = 255
            elif gamma_val <0 :
                image[i][k] = 0
            else :
                image[i][k] = gamma_val
    displayImage()


def rotateImage_45():
    global window, canvas, paper, height, width, filename
    canvas.destroy()
    rotated_image = [[0 for _ in range(width)] for _ in range(height)]
    center_x = width / 2
    center_y = height / 2
    theta = math.radians(45)  # 각도를 라디안으로 변환

    for i in range(height):
        for k in range(width):
            x = k - center_x
            y = i - center_y
            new_x = int(x * math.cos(theta) - y * math.sin(theta) + center_x)
            new_y = int(x * math.sin(theta) + y * math.cos(theta) + center_y)

            if 0 <= new_x < width and 0 <= new_y < height:
                rotated_image[i][k] = image[new_y][new_x]

    print(len(rotated_image))
    canvas = Canvas(window, height=256, width=256)
    paper = PhotoImage(height=256, width=256)
    canvas.create_image((256 / 2, 256 / 2), image=paper, state='normal')
    for i in range(height):
        for k in range(width):
            r = g = b = rotated_image[i][k]  # 3원색이 같으면 그레이 스케일
            paper.put('#%02x%02x%02x' % (r, g, b), (i, k))  # rgb를 16진수로 찍겠다.
    canvas.pack()

## 2배 확대
def size2():  # 두배로~
    global window, canvas, paper, height, width, filename
    canvas.destroy()
    canvas = Canvas(window, height=512, width=512)
    paper = PhotoImage(height=512, width=512)
    canvas.create_image((512 / 2, 512 / 2), image=paper, state='normal')
    for i in range(512):
        for k in range(512):
            r = g = b = image2[i][k]  # 3원색이 같으면 그레이 스케일
            paper.put('#%02x%02x%02x' % (r, g, b), (i, k))  # rgb를 16진수로 찍겠다.

    canvas.pack()

## 변수
window, canvas, paper = None, None, None
filename = ""
height, width = 0, 0
image = []
image2 = [[] for _ in range(height*2)]

rfp2 = open(filename, 'rb')
for i in range(0,height*2,2):
    for j in range(width):
        u= ord(rfp2.read(1))
        image2[i].append(u)
        image2[i].append(u)
        image2[i+1].append(u)
        image2[i+1].append(u)
rfp2.close()

## 메인
window = Tk()
window.geometry('800x800')
window.title('영상처리 Alpha')

btnReverse = Button(window, text='반전', command=reverseLRImage)
btnBright = Button(window, text='밝게', command=brightImage)
btnDark = Button(window, text='어둡게', command=darkImage)
btnBlack = Button(window, text='흑백처리', command=blackImage_127)
btnBlack_mean = Button(window, text='흑백(평균값)', command=blackImage_mean)
btnBlack_center = Button(window, text='픅백(중앙값)', command=blackImage_center)
btnRotate90 = Button(window, text='90도 회전', command=rotateImage_90)
btnRotate180 = Button(window, text='180도 회전', command=rotateImage_180)
btnRotate270 = Button(window, text='270도 회전', command=rotateImage_270)
btnRotate45 = Button(window, text='45도 회전', command=rotateImage_45)
btnSize2 = Button(window, text='2배 확대', command=size2)

btnReverse.pack()
btnBright.pack()
btnDark.pack()
btnBlack.pack()
btnBlack_mean.pack()
btnBlack_center.pack()
btnRotate90.pack()
btnRotate180.pack()
btnRotate270.pack()
btnRotate45.pack()
btnSize2.pack()





filename = '../Etc_Raw(squre)/hw.raw'
# 파일 크기 알아내기
fSize = os.path.getsize(filename) # Byte 단위
height = width = int(math.sqrt(fSize))
# 메모리 확보 (영상 크기)
image = [ [0 for _ in range(width)] for _ in range(height)]
# 파일 ---> 메모리 로딩
rfp = open(filename, 'rb')
for i in range(height):
    for k in range(width):
        image[i][k] = ord(rfp.read(1)) # ord는 이상한 문자 1바이트를 0-255사이의 숫자로 반환
rfp.close()

displayImage()


window.mainloop()

