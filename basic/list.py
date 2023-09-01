# 리스트

odd = [1,3,5,7,9] # 리스트 생성 및 초기화, 변수 = [요소1, 요소2...]
emtpy = list() # 비어있는 리스트 생성, []와 동일

## 인덱싱, 슬라이싱
### index
index = [1,2,3]
print(index[0]) # >>> '1'
print(index[0] + index[1]) # >>> '3'
print(index[-1]) # >>> '3'
index_2 = [1,2,3,['a', 'b', 'c']]
print(index_2[-1][0]) # >>> 'a'
### slice
slice = [1,2,3,4,5]
print(slice[0:2]) # >>> '[1, 2]
print(slice[:2]) # >>> '[1, 2]'
print(slice[2:]) # >>> '[3, 4, 5]'

## 연산
### 더하기
add_1 = [1,2,3]
add_2 = [4,5,6]
print(add_1 + add_2) # >>> '[1, 2, 3, 4, 5, 6]'
### 반복하기
repeat = [1,2,3]
print(repeat * 3) # >>> '[1, 2, 3, 1, 2, 3, 1, 2, 3]'
### 길이
print(len([1,2,3,4])) # >>> '4'

## 수정, 삭제
update = ['a', 'b', 'c']
update[0] = 'b'
print(update) # >>> '['b', 'b', 'c']'
delete = ['a', 'b', 'c']
del delete[0] # del 은 파이썬 자체 함수이다, (del 객체) 형식으로 사용
print(delete) # >>> '['b', 'c']'
del delete[:3] # 길이를 초과해도 상관없다
print(delete) # >>> '[]'
a = 2
del a
# print(a) # NameError: name 'a' is not defined

## 함수
### 요소추가
append = [1,2,3,4,5]
append.append(6)
print(append) # >>> '[1, 2, 3, 4, 5, 6]'
append.append([])
print(append) # >>> '[1, 2, 3, 4, 5, 6, []]'
### 정렬
sort_num = [3,4,2,5,1]
sort_num.sort()
print(sort_num) # >>> '[1, 2, 3, 4, 5]'
sort_alphabet = ['z', 'b', 's', 'a', 'y']
sort_alphabet.sort()
print(sort_alphabet) # >>> '['a', 'b', 's', 'y', 'z']'
### 리버스
reverse = [1,2,3,4,5]
reverse.reverse()
print(reverse) # >>> '[5, 4, 3, 2, 1]'
reverse_mix = [1,'b',2,'a',4,5]
reverse_mix.reverse()
print(reverse_mix) # >>> '[5, 4, 'a', 'b', 2, 1]', reverse 는 타입이 섞여도 각 타입별, 인덱스별 로 리버스해준다..
### 인덱스 반환
index_get = [1,2,3]
print(index_get.index(3)) # >>> '2'
# print(index_get.index(4)) # ValueError: 4 is not in list, 없으면 오류 발생
### 삽입
insert = [1,2,3]
insert.insert(1, 0)
print(insert) # >>> '[1, 0, 2, 3]'
insert.insert(-1, 0)
print(insert) # >>> '[1, 0, 2, 0, 3]'
### 제거
remove = [1,2,3,3]
remove.remove(3)
print(remove) # >>> '[1, 2, 3]', 첫번째로 나오는 요소 제거
# remove.remove(0) # ValueError: list.remove(x): x not in list, 없으면 오류 발생
remove_pop = [1,2,3,4,5]
print(remove_pop.pop()) # >>> '5', 맨 마지막 요소를 꺼낸 후 리스트에서 삭제
print(remove_pop) # >>> '[1, 2, 3, 4]'
### 카운트
count = [1,2,2,3,3,3]
print(count.count(3)) # >>> '3'
### 확장
extend = [1,2,3]
extend.extend(['extend'])
print(extend) # >>> '[1, 2, 3, 'extend']'
extend.extend('extend')
print(extend) # >>> '[1, 2, 3, 'extend', 'e', 'x', 't', 'e', 'n', 'd']', 문자열을 더할 경우 리스트로 평탄화된 후 확장된다.
# extend.extend(1) # TypeError: 'int' object is not iterable, iterable 타입이 아니기 때문에 오류가 발생한다.