# 딕셔너리

## 생성
dic = {
    "name": "chan",
    "name": "chan2", # 중복 키 값은 나중에 선언된 키-밸류로 덮어 씌워진다.
    'phone': "010-1111-1111",
    (1,) : 1 # 딕셔너리의 키에는 unhashable type 이 올 수 없다. 따라서 immutable 타입만이 키로 정의될 수 있다.
}
print(dic) # >>>'{'name': 'chan2', 'phone': '010-1111-1111', (1,): 1}'

## 추가, 삭제
add = {}
add["add"] = 1
print(add) # >>> '{'add': 1}'

del add["add"]
print(add) # >>> '{}'

pop = {
    "pop": 1
}
print(pop.pop("pop")) # >>> '1'
print(pop) # >>> '{}'
print(pop.pop("pop")) # KeyError: 'pop', 해당하는 키가 없을 경우 오류 발생.

## 사용 방법
use = {
    "김연아": "피겨스케이팅",
    "류현진": "야구", 
    "손흥민": "축구",
    "귀도": "파이썬"
}
print(use["김연아"]) # >>> '피겨스케이팅'
print(use["김연아1"]) # KeyError: '김연아1', 존재하지 않는 키인 경우 오류 발생
print(use.get("김연아")) # >>> '피겨스케이팅'
print(use.get("김연아1")) # >>> 'None', 존재하지 않는 키인 경우 None 반환.
print(use.get("김연아1", "default")) # >>> 'default', 존재하지 않는 키인 경우 디폴트 값을 반환하도록 할 수 있다.

## 함수
data = {
    1: "one",
    2: "two",
    3: "three"
}
### keys
print(data.keys()) # >>> 'dict_keys([1, 2, 3])', 딕셔너리 키 객체가 반환된다.
print(list(data.keys())) # >>> '[1, 2, 3]', 키 요소들을 리스트로 변환할 수 있다.
### values
print(data.values()) # >>> 'dict_values(['one', 'two', 'three'])', 딕셔너리 밸류 객체가 반환된다.
### items
print(data.items()) # >>> 'dict_items([(1, 'one'), (2, 'two'), (3, 'three')])', 딕셔너리 키-밸류 객체가 반환된다.
### in
print(1 in data) # >>> 'True', 키가 존재하는지 확인하고 boolean 값을 반환한다.
print(10 in data) # >>> 'False'
### clear
data.clear()
print(data) # >>> '{}', 딕셔너리의 모든 요소를 제거한다.