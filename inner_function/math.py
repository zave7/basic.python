# --- abs
## 숫자의 절댓값 반환
abs(1) # 1
abs(-1) # 1

# --- divmod
## 2개의 숫자를 입력받아 나눈 몫과 나머지를 튜플로 반환
divmod(5, 3) # (1,2)

# --- oct
## 정수를 입력받아 8진수 문자열로 반환
oct(8) # 0o10

# --- hex
## 정수를 입력받아 16진수 문자열로 반환
hex(16) # '0x10'

# --- int
## 문자열 타입이나 숫자 타입을 정수로 반환, 소수점의 경우 내림
## 진수 표현 문자열을 10진수로 변환하여 반환
int("3") # 3
int(3.4) # 3
int("1100", 2) # 12
int("010", 8) # 8
int("0x10", 16) # 16

# --- max
## 반복 가능한 값을 입력받아 최댓값을 반환
## 원소가 없는 값은 ValueError
max([1, 2, 3, 4, 5]) # 5

# --- min
## 반복 가능한 값을 입력받아 최솟값을 반환
## 원소가 없는 값은 ValueError
min([1, 2, 3, 4, 5]) # 1

# --- pow
## x를 y제곱한 결괏값을 반환
pow(2, 3) # 8

# --- round
## 숫자를 입력받아 반올림하여 반환
round(4.6) # 5
round(5.123, 2) # 5.12 