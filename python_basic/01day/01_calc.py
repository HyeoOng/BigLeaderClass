## 함수
def add_func(n1, n2):
    return n1 + n2

def minus_func(n1, n2):
    return n1 - n2

def square_func(n1):
    return n1 * n1

def multi_func(n1, n2):
    return n1 * n2

## 전역변수
num1, num2 = 0, 0


## 메인코드
# 두 숫자의 더하기/ 뺴기 등등을 계산하기
num1 = int(input("숫자1 : "))
num2 = int(input("숫자2 : "))

result = add_func(num1, num2)
result1 = minus_func(num1, num2)
result2 = square_func(num1)
result3 = multi_func(num1, num2)

print(num1, '+', num2, '=', result)
print(num1, '-', num2, '=', result1)
print(num1, '의 제곱은', result2)
print(num1, 'x', num2, '=', result3)