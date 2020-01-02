'''
division : 나누기
dividend : 피제수, 분자를 가리킴
divisor : 제수, 분모를 가리킴
quotient : 몫 (differential quotient 미분계수)
remainder : 나머지

fraction : 분수
numerator : 분자
denominator : 분모

'''


## 13-1
a = int(input('number: '))
b = int(input('number: '))
c, d =divmod(a, b)
print('몫: ', c, '나머지: ', d)


## 13-2
a = input('4 자리 정수를 입력하세요: ')
while len(a) != 4:
    a = input('4 자리 정수를 입력하세요: ')
    if len(a) ==4:
        break
result = int(a[0]) + int(a[1]) + int(a[2]) + int(a[3])
print(result)
number = int(input('네자리 정수를 입력하세요'))


















