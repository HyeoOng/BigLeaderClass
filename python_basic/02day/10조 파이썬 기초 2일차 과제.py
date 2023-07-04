import math
import os
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
from tkinter.simpledialog import *
from PIL import Image  # 필로우 라이브러리 중 Image 객체만 사용

## 함수 선언부
### 공통 함수부 ##############################################################################
def loadImage():
    global window, canvas, paper, filename, pillow
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
    saveFp = asksaveasfile(parent=window, mode='wb', defaultextension='*.jpg',
                           filetypes=(("칼라", "*.jpg;*.png;*.bmp;*.gif;"), ("모든 파일", "*.*")))
    if saveFp == "" or saveFp == None:
        return
    outArray = [[[] for _ in range(outW)] for _ in range(outH)]
    for i in range(outH):
        for j in range(outW):
            outArray[i][j] = tuple(outImage[rgb][i][j] for rgb in range(3))
    newImage = Image.new('RGB', (outW, outH))
    newImage.putdata([item for sublist in outArray for item in sublist])
    newImage.save(saveFp.name)
    messagebox.showinfo("저장 성공", saveFp.name + " 파일로 저장되었습니다.")

def exit_gui():
    messagebox.showinfo('종료', '종료합니다.')
    exit()

def imageToList():
    global inH, inW, inImage
    li = []
    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                li.append(inImage[rgb][i][k])
    return li

### 영상 처리 함수부 ##########################################################
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
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## 찐 영상처리 알고리즘 ##
    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                outImage[rgb][i][k] = 255 - inImage[rgb][i][k]
    #####################################
    displayImage()

def addImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! - 출력이미지의 크기를 결정 --> 알고리즘에 따라 달라짐(ex. 확대: 입력이미지의 2배)
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## 찐 영상처리 알고리즘 ##
    value = askinteger("밝기 입력", "밝게할 값을 입력해주세요. (-255 ~ 255)", minvalue=-255, maxvalue=255)
    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                if inImage[rgb][i][k] + value > 255 :
                    outImage[rgb][i][k] = 255
                elif inImage[rgb][i][k] + value < 0:
                    outImage[rgb][i][k] = 0
                else:
                    outImage[rgb][i][k] = inImage[rgb][i][k] + value
    #####################################
    displayImage()

def blackImage():
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
                if inImage[rgb][i][k] < 127:
                    outImage[rgb][i][k] = 255
                else:
                    outImage[rgb][i][k] = 0
    #####################################
    displayImage()

def blackMeanImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! - 출력이미지의 크기를 결정 --> 알고리즘에 따라 달라짐(ex. 확대: 입력이미지의 2배)
    outH = inH
    outW = inW
    meanVal = sum(imageToList()) / len(imageToList())
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## 찐 영상처리 알고리즘 ##
    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                if inImage[rgb][i][k] < meanVal:
                    outImage[rgb][i][k] = 255
                else:
                    outImage[rgb][i][k] = 0
    #####################################
    displayImage()

def blackCenterImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    center = 0
    li = sorted(imageToList())
    if len(li) % 2 == 0 :
        center = (li[len(li) // 2 - 1] + li[len(li) // 2]) / 2
    else:
        center = li[len(li) // 2]
    # 중요! - 출력이미지의 크기를 결정 --> 알고리즘에 따라 달라짐(ex. 확대: 입력이미지의 2배)
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## 찐 영상처리 알고리즘 ##
    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                if inImage[rgb][i][k] < center:
                    outImage[rgb][i][k] = 255
                else:
                    outImage[rgb][i][k] = 0
    #####################################
    displayImage()

def parabolaImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                outImage[rgb][i][k] = int(255 * (inImage[rgb][i][k]/128 - 1) **2)
    displayImage()

def gammaImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    gVal = askfloat("gamma값 입력", "0.1 ~ 3.0 사이의 실수를 입력해주세요.", minvalue=0.1, maxvalue=3.0)
    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                gamma_val = int((inImage[rgb][i][k]/255.0)**(1.0/gVal) * 255) # 2.2가 감마값에 가장 근접한 값
                if gamma_val>255:
                    outImage[rgb][i][k] = 255
                elif gamma_val < 0:
                    outImage[rgb][i][k] = 0
                else :
                    outImage[rgb][i][k] = gamma_val
    displayImage()

def moveImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! - 출력이미지의 크기를 결정 --> 알고리즘에 따라 달라짐(ex. 확대: 입력이미지의 2배)
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## 찐 영상처리 알고리즘 ##
    xVal = askinteger("X값", "")
    yVal = askinteger("Y값", "")
    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                if (0 <= i+xVal < outH) and (0 <= k+yVal < outW):
                    outImage[rgb][i+xVal][k+yVal] = inImage[rgb][i][k]
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
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## 찐 영상처리 알고리즘 ##
    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                    outImage[rgb][i // scale][k // scale] = inImage[rgb][i][k]
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
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## 찐 영상처리 알고리즘 ##
    for rgb in range(3):
        for i in range(outH):
            for k in range(outW):
                    outImage[rgb][i][k] = inImage[rgb][i//scale][k//scale]
    #####################################
    displayImage()

def rotateImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    angle = askinteger("각도", "0 ~ 360")
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    radian = angle * math.pi / 180.0 # math.radians(angle)
    ## 찐 영상처리 알고리즘 ##
    cx = inH // 2
    cy = inW // 2
    for rgb in range(3):
        for i in range(outH):
            for k in range(outW):
                # inH, inW를 기준으로 돌릴 떄는 아래의 변수 이용해서 outImage[newI][newK] = inImage[i][k]
                # newI = int(math.cos(radian) * (i - cx) - math.sin(radian) * (k - cy) + cx)
                # newK = int(math.sin(radian) * (i - cx) + math.cos(radian) * (k - cy) + cy)
                # backpropagetion느낌 inImage를 이용해 outImage 채우기
                oldI = int(math.cos(radian) * (i - cx) + math.sin(radian) * (k - cy) + cx)
                oldK = int(-math.sin(radian) * (i - cx) + math.cos(radian) * (k - cy) + cy)
                if (0 <= oldI < inH) and (0 <= oldK < inW):
                    outImage[rgb][i][k] = inImage[rgb][oldI][oldK]
        #####################################
    displayImage()

def blurImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    pad_size = askinteger("필터 사이즈", "")
    outH = inH;
    outW = inW;
    # 메모리 할당
    conImage = [[[0 for _ in range(outW + (pad_size - 1))] for _ in range(outH + (pad_size - 1))] for _ in range(3)]  # 패딩 이미지
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## ** 찐 영상처리 알고리즘 ** ##
    blur_filter = [[1/(pad_size**2) for _ in range(pad_size)]for _ in range(pad_size)]
    for rgb in range(3):
        for i in range(1, inH + 1):
            for k in range(1, inW + 1):
                conImage[rgb][i][k] = inImage[rgb][i - 1][k - 1]

    for rgb in range(3):
        for i in range(inH):  # 9 사이즈의 필터로 패딩1을 한 리스트를 콘볼루션 하려면 -2까지 하니깐 +2 했던 것과 오프셋
            for j in range(inW):
                s = 0
                for k in range(pad_size):
                    for l in range(pad_size):
                        s += int(conImage[rgb][i+k][j + l] * blur_filter[k][l])
                outImage[rgb][i][j] = s
    displayImage()


def embosingPositiveImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH;
    outW = inW;
    # 메모리 할당
    conImage = [[[0 for _ in range(outW + 2)] for _ in range(outH + 2)] for _ in range(3)]  # 패딩 이미지
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## ** 찐 영상처리 알고리즘 ** ##
    embosing_filter = [[1, 1, 1], [1, -8, 1], [1, 1, 1]]  # 양각
    for rgb in range(3):
        for i in range(1, inH + 1):
            for k in range(1, inW + 1):
                conImage[rgb][i][k] = inImage[rgb][i - 1][k - 1]

    for rgb in range(3):
        for i in range(inH):  # 9 사이즈의 필터로 패딩1을 한 리스트를 콘볼루션 하려면 -2까지 하니깐 +2 했던 것과 오프셋
            for j in range(inW):
                s = 0  # 컨볼루션한 값
                for w in range(3):
                    for m in range(3):
                        s += int(conImage[rgb][i + w][j + m] * embosing_filter[w][m])

                if s > 255:
                    outImage[rgb][i][j] = 255
                elif s < 0:
                    outImage[rgb][i][j] = 0
                else:
                    outImage[rgb][i][j] = s

    displayImage()


def embosingNegativeImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH;
    outW = inW;
    # 메모리 할당
    conImage = [[[0 for _ in range(outW + 2)] for _ in range(outH + 2)] for _ in range(3)]  # 패딩 이미지
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## ** 찐 영상처리 알고리즘 ** ##
    embosing_filter = [[-1, 0, 0], [0, 0, 0], [0, 0, 1]]  # 음각
    for rgb in range(3):
        for i in range(1, inH + 1):
            for k in range(1, inW + 1):
                conImage[rgb][i][k] = inImage[rgb][i - 1][k - 1]

    for rgb in range(3):
        for i in range(inH):  # 9 사이즈의 필터로 패딩1을 한 리스트를 콘볼루션 하려면 -2까지 하니깐 +2 했던 것과 오프셋
            for j in range(inW):
                s = 0  # 컨볼루션한 값
                for w in range(3):
                    for m in range(3):
                        s += int(conImage[rgb][i + w][j + m] * embosing_filter[w][m])

                if s > 255:
                    outImage[rgb][i][j] = 255
                elif s < 0:
                    outImage[rgb][i][j] = 0
                else:
                    outImage[rgb][i][j] = s

    displayImage()

def sharpeningImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH;
    outW = inW;
    # 메모리 할당
    conImage = [[[0 for _ in range(outW + 2)] for _ in range(outH + 2)] for _ in range(3)]  # 패딩 이미지
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## ** 찐 영상처리 알고리즘 ** ##
    sharpening_filter = [[-1, -1, -1],
                         [-1, 9, -1],
                         [-1, -1, -1]]
    for rgb in range(3):
        for i in range(1, inH + 1):
            for k in range(1, inW + 1):
                conImage[rgb][i][k] = inImage[rgb][i - 1][k - 1]

    for rgb in range(3):
        for i in range(inH):  # 9 사이즈의 필터로 패딩1을 한 리스트를 콘볼루션 하려면 -2까지 하니깐 +2 했던 것과 오프셋
            for j in range(inW):
                s = 0  # 컨볼루션한 값
                for w in range(3):
                    for m in range(3):
                        s += int(conImage[rgb][i + w][j + m] * sharpening_filter[w][m])

                if s > 255:
                    outImage[rgb][i][j] = 255
                elif s < 0:
                    outImage[rgb][i][j] = 0
                else:
                    outImage[rgb][i][j] = s
    displayImage()

def edgeImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH;
    outW = inW;
    # 메모리 할당
    conImage = [[[0 for _ in range(outW + 2)] for _ in range(outH + 2)] for _ in range(3)]  # 패딩 이미지
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## ** 찐 영상처리 알고리즘 ** ##
    edge_filterx = [[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]]
    edge_filtery = [[-1, -2, -1],
                    [0, 0, 0],
                    [1, 2, 1]]

    for rgb in range(3):
        for i in range(1, inH + 1):
            for k in range(1, inW + 1):
                conImage[rgb][i][k] = inImage[rgb][i - 1][k - 1]

    for rgb in range(3):
        for i in range(inH):  # 9 사이즈의 필터로 패딩1을 한 리스트를 콘볼루션 하려면 -2까지 하니깐 +2 했던 것과 오프셋
            for j in range(inW):
                s1 = 0  # 컨볼루션한 값
                s2 = 0
                for w in range(3):
                    for m in range(3):
                        s1 += int(conImage[rgb][i + w][j + m] * edge_filterx[w][m])
                        s2 += int(conImage[rgb][i + w][j + m] * edge_filtery[w][m])

                if s1 + s2 > 255:
                    outImage[rgb][i][j] = 255
                elif s1 + s2 < 0:
                    outImage[rgb][i][j] = 0
                else:
                    outImage[rgb][i][j] = s1 + s2
    displayImage()

## 전역 변수부 ###########################################################3
window, canvas, paper = None, None, None
filename = ""
inImage, outImage = None, None
inH, inW, outH, outW = 0, 0, 0, 0

## 메인 코드부 ##########################################################333
window = Tk()
window.geometry('300x300')
window.title('Color Image Processing (GA 1)')

mainMenu = Menu(window)  # button들을 넣을 메뉴의 틀
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)  # 상위 메뉴(파일)
mainMenu.add_cascade(label='파일', menu=fileMenu)  # cascade는 확장형
fileMenu.add_command(label='열기', command=loadImage)  # command는 실행되는 것
fileMenu.add_command(label='저장', command=saveImage)
fileMenu.add_separator()
fileMenu.add_command(label='종료', command=exit_gui)

image1Menu = Menu(mainMenu)
mainMenu.add_cascade(label='영상처리1', menu=image1Menu)
image1Menu.add_command(label='동일영상', command=equalImage)  # 원본 영상
image1Menu.add_command(label='그레이스케일', command=grayImage)
image1Menu.add_command(label='반전', command=reverseImage)
image1Menu.add_command(label='밝게/어둡게', command=addImage)
blackMenu = Menu(image1Menu)
image1Menu.add_cascade(label='흑백', menu=blackMenu)
blackMenu.add_command(label='기준값', command=blackImage)
blackMenu.add_command(label='평균값', command=blackMeanImage)
blackMenu.add_command(label='중앙값', command=blackCenterImage)
image1Menu.add_command(label='파라볼라 연산', command=parabolaImage)
image1Menu.add_command(label='감마 연산', command=gammaImage)


image2Menu = Menu(mainMenu)
mainMenu.add_cascade(label='기하학 처리', menu=image2Menu)
image2Menu.add_command(label='이동', command=moveImage)  # 원본 영상
image2Menu.add_command(label='측소', command=zoomOutImage)
image2Menu.add_command(label='확대', command=zoomInImage)
image2Menu.add_command(label='회전', command=rotateImage)

image3Menu = Menu(mainMenu)
mainMenu.add_cascade(label='화소영역 처리', menu=image3Menu)
image3Menu.add_command(label='블러링', command=blurImage)
embosingMenu = Menu(image3Menu)
image3Menu.add_cascade(label='엠보싱', menu=embosingMenu)
embosingMenu.add_command(label='양각', command=embosingPositiveImage)
embosingMenu.add_command(label='음각', command=embosingNegativeImage)
image3Menu.add_command(label='샤프닝', command=sharpeningImage)
image3Menu.add_command(label='경계선 처리', command=edgeImage)


window.mainloop()