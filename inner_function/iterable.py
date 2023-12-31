# --- enumerate
## 순서가 있는 데이터(list, tuple, string)를 입력으로 받아 인덱스 값을 포함하는 enumerate 객체 반환
enumerate(["a", "b"]) # {index, value} list 반환
# 0 a
# 1 b

# --- filter
## 함수와 반복가능한 값을 입력받아 함수에 값을 인수로 호출하고 반환값이 참인것만 리스트로 묶어서 반환
filtered = filter(lambda n: n > 0, [-2, -1, 0, 1, 2])
for n in filtered:
    print(n, end=",") # 1,2

# --- len
## 입력값의 길이를 반환
len("123") # 3
len([1, 2, 3]) # 3

# --- list
## 반복 가능한 값을 입력받아 리스트로 변환하여 반환
list((1,2)) # [1, 2]

# --- map
## 함수와 반복 가능한 값을 입력받아 함수를 적용한 결과를 반환
map(lambda n: str(n), [1, 2, 3]) # ["1", "2", "3"]

# --- range
## 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 반환
range(5) # 인수가 하나일 경우 (0)~(n미만) [0, 1, 2, 3, 4]
range(5, 10) # 인수가 두개일 경우 (a)~(b미만) [5, 6, 7, 8, 9]
range(5, 10, 2) # 인수가 세개일 경우 (step) [5, 7, 9]

# --- sorted
## 입력 데이터를 정렬한 후 그 결과로 리스트 반환
## 리스트 자료형의 sort 함수는 객체를 정렬하기만 하고 반환하지 않음
sorted([3, 2, 1]) # [1, 2, 3]
sorted(["c", "d", "a"]) # ["a", "c", "d"]

# --- sum
## 입력 데이터의 합을 반환
sum([1, 2, 3]) # 6
sum([]) # 0

# --- tuple
## 반복 가능한 값을 튜플로 바꾸어 반환
print(tuple("abcd")) # ('a', 'b', 'c', 'd')
print([1, 2, 3]) # (1, 2, 3)

# --- zip
## 동일한 개수로 이루어진 데이터(iterable)들을 묶어서 반환하는 함수
zip([1, 3, 5, 7], [2, 4, 6, 8]) # [(1,2), (3,4), (5,6), (7,8)]
zip("abc", "abc") # [("a", "a"), ("b", "b"), ("c", "c")]