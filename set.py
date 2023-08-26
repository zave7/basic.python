# 집합 / 중복이 없고 순서가 없다
set_num = set([1,2,3,3])
print(set_num) # >>> '{1, 2, 3}'
set_str = set("test")
print(set_str) # >>> '{'s', 'e', 't'}'
set_str2 = set(["test"])
print(set_str2) # >>> '{'test'}'

## 변환
to_list = list(set_num)
print(to_list) # >>> '[1, 2, 3]'
to_tuple = tuple(set_num)
print(to_tuple) # >>> '(1, 2, 3)'

set_1 = set([1,2,3])
set_2 = set([3,4,5])

## 교집합
print(set_1 & set_2) # >>> '{3}'
print(set_1.intersection(set_2)) # >>> '{3}'

## 합집합
print(set_1 | set_2) # >>> '{1, 2, 3, 4, 5}'
print(set_1.union(set_2)) # >>> '{1, 2, 3, 4, 5}'

## 차집합
print(set_1 - set_2) # >>> '{1, 2}'
print(set_1.difference(set_2)) # >>> '{1, 2}'

## 함수
set_funtion = set([1])
### add
set_funtion.add(2)
print(set_funtion) # >>> '{1, 2}'
### update
set_funtion.update([3,4])
print(set_funtion) # >>> '{1, 2, 3, 4}'
### remove
set_funtion.remove(2)
set_funtion.remove(3)
set_funtion.remove(4)
print(set_funtion) # >>> '{1}'