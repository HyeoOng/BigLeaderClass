# print('Hello World!')

# num = 100
# if (num > 100 ):
#     print('100보다 크다')
# else :
#     print('100보다 작거나 같다')
#
# hap = 0
# for i in range(1, 101, 1):
#     hap += i
#
# print(hap)

# quiz (while문으로 바꾸기)
# hap = 0
# i = 1
# while(i<101):
#     hap += i
#     i += 1
# print(hap)

# 함수로 바꾸기

## 함수 선언부
def addNumber(start, end):
    add_hap = 0
    for i in range(start, end +1, 1):
        add_hap += i
    return add_hap

## 전역 변수부
hap = 0

## 메인 코드부
hap = addNumber(1, 100)
print(hap)