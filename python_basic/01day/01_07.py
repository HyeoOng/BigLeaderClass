# alpha 버전..?
from tkinter import *
from tkinter import messagebox
import os.path
import math

## 함수
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

# 흑백처리
def blackImage():
    for i in range(height):
        for k in range(width):
            if (image[i][k] < 128):
                image[i][k] = 255
            else :
                image[i][k] = 0
    displayImage()

## 변수
window, canvas, paper = None, None, None
filename = ""
height, width = 0, 0
image = []

## 메인
window = Tk()
window.geometry('500x520')
window.title('영상처리 Alpha')


btnReverse = Button(window, text='반전', command=reverseImage)
btnReverse.pack()

btnBright = Button(window, text='밝게', command=brightImage)
btnBright.pack()

btnDark = Button(window, text='어둡게', command=darkImage)
btnDark.pack()

btnBlack = Button(window, text='완전 흑백처리', command=blackImage)
btnBlack.pack()

filename = '../Etc_Raw(squre)/dog.raw'
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