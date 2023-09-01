# 함수

## 파이썬 함수의 구조
# def 함수_이름(매개변수):
def add(a, b): 
    return a + b
print(add(1,2)) # >>> '3'

## 매개변수와 인수
def minus(a, b): # a, b : 매개변수
    return a - b
print(minus(2, 1)) # 2, 1 : 인수

## 입력값과 리턴값에 따른 함수의 형태
# 일반적인 함수
def general(input):
    result = str(input)
    return result
# 입력값이 없는 함수
def say():
    return "Hi"
# 리턴값이 없는 함수
def no_return():
    print("no return")
print(no_return()) # >>> 'None'

## 매개변수를 지정하여 호출
def sub(a, b):
    return a - b
print(sub(a=1, b=2)) # >>> '-1'

## 입력값의 가변
### 가변 매개변수
def variable(*agrs):
    return len(agrs)
print(variable(1,2,3,4)) # >>> '4'
print(variable(1,2,3,4,5)) # >>> '5'
### 키워드 매개변수 - 매개변수는 딕셔너리가 된다.
def print_kwagrs(**kwagrs):
    print(kwagrs)
print_kwagrs(a=1, b="2", c={}) # >>> '{'a': 1, 'b': '2', 'c': {}}'

## 함수의 리턴값은 언제나 하나
def add_and_mul(a, b): 
    return a+b, a*b
print(add_and_mul(1,2)) # >>> '(3, 2)'

def double_return(): 
    return 1
    return 2
print(double_return()) # >>> '1'

## 매개변수에 초깃값 미리 설정하기
def set_default_value(name, age, man=True):
    print(f"이름:{name}, 나이{age}, 남자 : {man}")
set_default_value("찬", 26) # >>> '이름:찬, 나이26, 남자 : True'
set_default_value("찬", 26, False) # >>> '이름:찬, 나이26, 남자 : False'

## 함수 안에서 선언한 변수의 효력 범위
a = 1
def var_test_1(a):
    a = a + 1
print(a) # >>> '1'

def var_test_2(b):
    b = b + 1
print(b) # NameError: name 'b' is not defined

## 함수 안에서 함수 밖의 변수를 변경하는 방법
a = 1
def global_fun():
    global a
    a = 2
global_fun()
print(a) # >>> '2'

## lambda 예약어
# 함수_이름 = lambda 매개변수1, 매개변수2... : 
lambda_test = lambda a, b: a + b
print(lambda_test(1,2)) # >>> '3'