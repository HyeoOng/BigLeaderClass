import math
import os
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
from tkinter.simpledialog import *

## 함수 선언부
### 공통 함수부 ###
def loadImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    filename = askopenfilename(parent=window, filetypes=(("RAW파일", "*.raw"), ("모든 파일", "*.*")))
    # 파일 크기 알아내기
    fSize = os.path.getsize(filename)  # Byte 단위
    inH = inW = int(math.sqrt(fSize))
    # 메모리 확보 (영상 크기)
    inImage = [[0 for _ in range(inW)] for _ in range(inH)]
    # 파일 ---> 메모리 로딩
    rfp = open(filename, 'rb')
    for i in range(inH):
        for k in range(inW):
            inImage[i][k] = ord(rfp.read(1))  # ord는 이상한 문자 1바이트를 0-255사이의 숫자로 반환
    rfp.close()
    equalImage()

def displayImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    if canvas != None:
        canvas.destroy()

    window.geometry(str(outH) + 'x' + str(outW))
    canvas = Canvas(window, height=outH, width=outW)
    paper = PhotoImage(height=outH, width=outW)
    canvas.create_image((outH / 2, outW / 2), image=paper, state='normal') # 중앙점 찾음

    # for i in range(outH):
    #     for k in range(outW):
    #         r = g = b = outImage[i][k]
    #         paper.put('#%02x%02x%02x' % (r, g, b), (k, i))  # r, g, b를 %02x 순서대로 (i,k)위치에 찍어라(화면에 찍는 것)

    # 속도 향상을 위해 메모리 상에 이미지의 픽셀을 먼저 찍고, 바로 화면으로 출력하게끔 코딩
    rgbString = ""
    for i in range(outH):
        tmpString = ""
        for k in range(outW):
            r = g = b = outImage[i][k]
            tmpString += '#%02x%02x%02x ' % (r, g, b)
        rgbString += '{' + tmpString + '} '
    paper.put(rgbString)

    canvas.pack()

def saveImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    saveFp = asksaveasfile(parent=window, mode='wb', defaultextension='*.raw', filetypes=(("RAW파일", "*.raw"), ("모든 파일", "*.*")))  # wb : write binary
    import struct
    for i in range(outH):
        for k in range(outW):
            saveFp.write(struct.pack('B', outImage[i][k]))  # B : byte
    saveFp.close()
    messagebox.showinfo('성공', saveFp.name + '으로 저장')

### 영상 처리 함수부 ###
def equalImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! - 출력이미지의 크기를 결정 --> 알고리즘에 따라 달라짐(ex. 확대: 입력이미지의 2배)
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]
    ## 찐 영상처리 알고리즘 ##
    for i in range(inH):
        for k in range(inW):
            outImage[i][k] = inImage[i][k]
    #####################################
    displayImage()

def reverseImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! - 출력이미지의 크기를 결정 --> 알고리즘에 따라 달라짐(ex. 확대: 입력이미지의 2배)
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]
    ## 찐 영상처리 알고리즘 ##
    for i in range(inH):
        for k in range(inW):
            outImage[i][k] = 255 - inImage[i][k]
    #####################################
    displayImage()

def addImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! - 출력이미지의 크기를 결정 --> 알고리즘에 따라 달라짐(ex. 확대: 입력이미지의 2배)
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]
    ## 찐 영상처리 알고리즘 ##
    value = askinteger("밝기 입력", "밝게할 값을 입력해주세요. (-255 ~ 255)", minvalue=-255, maxvalue=255)
    for i in range(inH):
        for k in range(inW):
            if inImage[i][k] + value > 255 :
                outImage[i][k] = 255
            elif inImage[i][k] + value < 0:
                outImage[i][k] = 0
            else:
                outImage[i][k] = inImage[i][k] + value
    #####################################
    displayImage()

def blackImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! - 출력이미지의 크기를 결정 --> 알고리즘에 따라 달라짐(ex. 확대: 입력이미지의 2배)
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]
    ## 찐 영상처리 알고리즘 ##
    for i in range(inH):
        for k in range(inW):
            if (inImage[i][k] < 128):
                outImage[i][k] = 255
            else:
                outImage[i][k] = 0
    #####################################
    displayImage()

def blackImage_mean():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 평균값 구하기
    mean = 0
    for i in range(inH):
        for k in range(inW):
            mean += inImage[i][k]
    mean = mean / (inH * inW)
    # 중요! - 출력이미지의 크기를 결정 --> 알고리즘에 따라 달라짐(ex. 확대: 입력이미지의 2배)
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]
    ## 찐 영상처리 알고리즘 ##
    for i in range(inH):
        for k in range(inW):
            if (inImage[i][k] < mean):
                outImage[i][k] = 255
            else:
                outImage[i][k] = 0
    #####################################
    displayImage()

def blackImage_center():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중앙값 구하기
    center = 0
    li = [inImage[i][k] for i in range(inH) for k in range(inW)]
    if len(li) % 2 == 0:
        center = (li[len(li)/2 -1] + li[len(li)/2])/2
    else :
        center = li[len(li)//2]
    # 중요! - 출력이미지의 크기를 결정 --> 알고리즘에 따라 달라짐(ex. 확대: 입력이미지의 2배)
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]
    ## 찐 영상처리 알고리즘 ##
    for i in range(inH):
        for k in range(inW):
            if (inImage[i][k] < center):
                outImage[i][k] = 255
            else:
                outImage[i][k] = 0
    #####################################
    displayImage()

def rotate90Image():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! - 출력이미지의 크기를 결정 --> 알고리즘에 따라 달라짐(ex. 확대: 입력이미지의 2배)
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]
    ## 찐 영상처리 알고리즘 ##
    for i in range(inH):
        for k in range(inW):
            outImage[k][inW - i - 1] = inImage[i][k]
    #####################################
    displayImage()

def rotate180Image():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! - 출력이미지의 크기를 결정 --> 알고리즘에 따라 달라짐(ex. 확대: 입력이미지의 2배)
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]
    ## 찐 영상처리 알고리즘 ##
    for i in range(inH):
        for k in range(inW):
            outImage[inH-i-1][inH-k-1] = inImage[i][k]
    #####################################
    displayImage()

def rotate270Image():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! - 출력이미지의 크기를 결정 --> 알고리즘에 따라 달라짐(ex. 확대: 입력이미지의 2배)
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]
    ## 찐 영상처리 알고리즘 ##
    for i in range(inH):
        for k in range(inW):
            outImage[inH-k-1][i] = inImage[i][k]
    #####################################
    displayImage()

## 전역 변수부
window, canvas, paper = None, None, None
filename = ""
inImage, outImage = None, None
inH, inW, outH, outW = 0, 0, 0, 0

## 메인 코드부
window = Tk()
window.geometry('300x300')
window.title('GrayScale Image Processing (Beta 1)')

mainMenu = Menu(window)  # button들을 넣을 메뉴의 틀
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)  # 상위 메뉴(파일)
mainMenu.add_cascade(label='파일', menu=fileMenu)  # cascade는 확장형
fileMenu.add_command(label='열기', command=loadImage)  # command는 실행되는 것
fileMenu.add_command(label='저장', command=saveImage)  # command는 실행되는 것
fileMenu.add_separator()
fileMenu.add_command(label='종료', command=None)  # command는 실행되는 것

image1Menu = Menu(mainMenu)
mainMenu.add_cascade(label='영상처리1', menu=image1Menu)
image1Menu.add_command(label='동일영상', command=equalImage)  # 원본 영상
image1Menu.add_command(label='반전', command=reverseImage)
image1Menu.add_command(label='밝게/어둡게', command=addImage)
image1Menu.add_command(label='흑백', command=blackImage)
image1Menu.add_command(label='흑백(평균값)', command=blackImage_mean)
image1Menu.add_command(label='흑백(중앙값)', command=blackImage_center)
image1Menu.add_command(label='90도 회전', command=rotate90Image)
image1Menu.add_command(label='180도 회전', command=rotate180Image)
image1Menu.add_command(label='270도 회전', command=rotate270Image)




window.mainloop()