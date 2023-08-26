from copy import copy

# 숫자형
## 정수
integer_p = 123
integer_n = -432
integer_z = 0
## 실수
float_p = 123.45
float_n = -1234.5
float_e1 = 1.456e10
float_e2 = 1.456E10
## 8진수
octal = 0o12
## 16진수 
hex = 0x12f

## 메모리
memory_1 = 1
memory_2 = memory_1
print(id(memory_1)) # >>> '4319783352'
print(id(memory_2)) # >>> '4319783352'
print(memory_1 is memory_2) # >>> 'True'

list_1 = [1]
list_2 = list_1
print(list_1 is list_2) # >>> 'True'
print(list_1 is list_1[:]) # >>> 'False'
print(list_1 is copy(list_1)) # >>> 'False'

## 대입
tuple_1, tuple_2 = (1,2)
print(f"{tuple_1} {tuple_2}") # >>> '1 2'
(tuple_3, tuple_4) = 3,4
print(f"{tuple_3} {tuple_4}") # >>> '3 4'
array = [a, b] = 1,2
print(array) # >>> '(1, 2)'
print(f"{a} {b}") # >>> '1 2'
c, d = [1,2,3] # ValueError: too many values to unpack (expected 2), 모든 요소를 다 할당해야한다.