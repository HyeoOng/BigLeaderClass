import math
import os
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
from tkinter.simpledialog import *
from PIL import Image  # 필로우 라이브러리 중 Image 객체만 사용

## 함수 선언부
### 공통 함수부 ###
def loadImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    filename = askopenfilename(parent=window, filetypes=(("칼라", "*.jpg;*.png;*.bmp;*.gif;"), ("모든 파일", "*.*")))
    # 파일 크기 알아내기
    pillow = Image.open(filename)
    inH = pillow.height
    inW = pillow.width
    # 메모리 확보 (영상 크기)
    inImage = [[[0 for _ in range(inW)] for _ in range(inH)] for _ in range(3)]
    # 파일 ---> 메모리 로딩
    pillowRGB = pillow.convert('RGB') # 내부적으로 RGB 모델로 변경
    for i in range(inH):
        for k in range(inW):
            r, g, b = pillowRGB.getpixel((k, i))
            inImage[0][i][k] = r
            inImage[1][i][k] = g
            inImage[2][i][k] = b
    equalImage()

def displayImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    if canvas != None:
        canvas.destroy()

    window.geometry(str(outW) + 'x' + str(outH))
    canvas = Canvas(window, height=outH, width=outW)
    paper = PhotoImage(height=outH, width=outW)
    canvas.create_image((outW / 2, outH / 2), image=paper, state='normal') # 중앙점 찾음

    rgbString = ""
    for i in range(outH):
        tmpString = ""
        for k in range(outW):
            r = outImage[0][i][k]
            g = outImage[1][i][k]
            b = outImage[2][i][k]
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
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## 찐 영상처리 알고리즘 ##
    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                outImage[rgb][i][k] = inImage[rgb][i][k]
    #####################################
    displayImage()

def grayImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! - 출력이미지의 크기를 결정 --> 알고리즘에 따라 달라짐(ex. 확대: 입력이미지의 2배)
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## 찐 영상처리 알고리즘 ##
    for i in range(inH):
        for k in range(inW):
            hap = inImage[0][i][k] + inImage[1][i][k] + inImage[2][i][k]
            outImage[0][i][k] = outImage[1][i][k] = outImage[2][i][k] = hap // 3
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

def moveImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! - 출력이미지의 크기를 결정 --> 알고리즘에 따라 달라짐(ex. 확대: 입력이미지의 2배)
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]
    ## 찐 영상처리 알고리즘 ##
    xVal = askinteger("X값", "")
    yVal = askinteger("Y값", "")
    for i in range(inH):
        for k in range(inW):
            if (0 <= i+xVal < outH) and (0 <= k+yVal < outW):
                outImage[i+xVal][k+yVal] = inImage[i][k]
    #####################################
    displayImage()

def zoomOutImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! - 출력이미지의 크기를 결정 --> 알고리즘에 따라 달라짐(ex. 확대: 입력이미지의 2배)
    scale = askinteger("축소배율", "")
    outH = inH // scale
    outW = inW // scale
    # 메모리 할당
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]
    ## 찐 영상처리 알고리즘 ##
    for i in range(inH):
        for k in range(inW):
                outImage[i // scale][k // scale] = inImage[i][k]
    #####################################
    displayImage()

def zoomInImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! - 출력이미지의 크기를 결정 --> 알고리즘에 따라 달라짐(ex. 확대: 입력이미지의 2배)
    scale = askinteger("학대배율", "")
    outH = inH * scale
    outW = inW * scale
    # 메모리 할당
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]
    ## 찐 영상처리 알고리즘 ##
    for i in range(outH):
        for k in range(outW):
                outImage[i][k] = inImage[i//scale][k//scale]
    #####################################
    displayImage()

def rotateImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    angle = askinteger("각도", "0 ~ 360")
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]
    radian = math.radians(angle)  # angle * math.pi / 180.0
    ## 찐 영상처리 알고리즘 ##
    for i in range(outH):
        for k in range(outW):
            cx = inH // 2
            cy = inW // 2
            # inH, inW를 기준으로 돌릴 떄는 아래의 변수 이용해서 outImage[newI][newK] = inImage[i][k]
            # newI = int(math.cos(radian) * (i - cx) - math.sin(radian) * (k - cy) + cx)
            # newK = int(math.sin(radian) * (i - cx) + math.cos(radian) * (k - cy) + cy)
            # backpropagetion느낌 inImage를 이용해 outImage 채우기
            oldI = int(math.cos(radian) * (i - cx) + math.sin(radian) * (k - cy) + cx)
            oldK = int(-math.sin(radian) * (i - cx) + math.cos(radian) * (k - cy) + cy)
            if (0 <= oldI < inH) and (0 <= oldK < inW):
                outImage[i][k] = inImage[oldI][oldK]
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
fileMenu.add_command(label='저장', command=saveImage)
fileMenu.add_separator()
fileMenu.add_command(label='종료', command=None)

image1Menu = Menu(mainMenu)
mainMenu.add_cascade(label='영상처리1', menu=image1Menu)
image1Menu.add_command(label='동일영상', command=equalImage)  # 원본 영상
image1Menu.add_command(label='그레이스케일', command=grayImage)
image1Menu.add_command(label='반전', command=reverseImage)
image1Menu.add_command(label='밝게/어둡게', command=addImage)

image2Menu = Menu(mainMenu)
mainMenu.add_cascade(label='기하학 처리', menu=image2Menu)
image2Menu.add_command(label='이동', command=moveImage)  # 원본 영상
image2Menu.add_command(label='측소', command=zoomOutImage)
image2Menu.add_command(label='확대', command=zoomInImage)
image2Menu.add_command(label='회전', command=rotateImage)




window.mainloop()