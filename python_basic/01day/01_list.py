import random
## 함수부



## 변수
ary1 = []


## 메인부
# 배열의 값 초기화
for i in range(10):
    ary1.append(0)

print(ary1)

# 배열의 값 대입하자 짝수만
num = 2
for i in range(0, 10, 1):  # i는 첨자로만 사용하기
    ary1[i] = random.randint(0, 1000)
    # num += 2

print(ary1)


# 배열
# 1. 배열의 값의 합계
# 2. 배열 중 홀수만 합계

# 1번
hap = 0
for i in range(len(ary1)):
    hap += ary1[i]

# 2번
odd_hap = 0
for i in range(len(ary1)):
    if ary1[i] % 2 == 1:
        odd_hap += ary1[i]

print(hap)
print(odd_hap)