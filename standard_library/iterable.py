# --- itertools
import itertools

## zip_longest : 같은 갯수의 자료형을 묶는 파이썬 내장 함수인 zip 함수와 동일하게 동작한다.
## 하지만 반복 가능한 객체의 길이가 다를 경우 긴 객체의 길이에 맞춰 fillvalue에 설정한 값을 짧은 객체에 채울 수 있다.
students = ['권영찬', '이진혁', '박찬혁', '한예진']
drink = ['사이다', '콜라']
zip_result = zip(students, drink) # [ ('권영찬', '사이다'), ('이진혁', '콜라') ]
zip_longest_result = itertools.zip_longest(students, drink, fillvalue='fill') # [ ('권영찬', '사이다'), ('이진혁', '콜라'), ('박찬혁', 'fill'), ('한예진', 'fill') ]

## permutation : 반복 가능한 객체 중에서 r개를 선택한 순열을 iterator로 반환하는 함수
permutation = itertools.permutations([1, 2, 3], 2) # [ (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2) ]

## combinations : 반복 가능한 객체 중에서 순서에 상관없이 r개의 조합을 반환하는 함수
combination = itertools.combinations([1, 2, 3], 2) # [ (1, 2), (1, 3), (2, 3) ]

## combinations_with_replacement : combinations에서 데이터의 중복을 허용하는 조합을 반환하는 함수
combinations_with_replacement = itertools.combinations_with_replacement([1, 2, 3], 2) # [ (1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3) ]

# --- functools
import functools

## reduce : iterable 요소 값들을 누적 계산하여 최종 계산된 1개의 값을 반환
reduce = functools.reduce(lambda a, b: a + b, [1, 2, 3]) # 6

# --- operator
from operator import itemgetter, attrgetter

## itemgetter : 정렬 함수 key 매개변수에 적용하여 정렬할 수 있도록 도와주는 모듈(클래스)
students_tuple = [
    ("a", 1), ("b", 3), ("c", 2),
]
sorted_student_tuple = sorted(students_tuple, key=itemgetter(1)) # [('a', 1), ('c', 2), ('b', 3)]

students_dic = [
    { "name": "a", "age": 1 },
    { "name": "b", "age": 3 },
    { "name": "c", "age": 2 }
]

sorted_students_dic = sorted(students_dic, key=itemgetter("age")) # [{'name': 'a', 'age': 1}, {'name': 'c', 'age': 2}, {'name': 'b', 'age': 3}]

## attrgetter : 정렬 함수 key 매개변수에 적용하여 정렬할 수 있도록 도와주는 모듈(클래스)
class Student:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
students_class = [
    Student('a', 1),
    Student('b', 3),
    Student('c', 2)
]
sorted_students_class = sorted(students_class, key=attrgetter('age')) # a, b, c 순 정렬
