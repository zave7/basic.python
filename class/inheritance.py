# 상속

## 부모 클래스
class Parent:
    age = 3
    def __init__(self, age: int = age) -> None:
        self.age = age
    def test(self) -> None:
        pass

## 자식 클래스
class Child(Parent): # 클래스를 상속하기 위해서는 클래스 이름 뒤 괄호안에 상속할 클래스 이름을 넣어주면 된다.
    def __init__(self) -> None:
        super().__init__()
    def test(self) -> str: # 오버라이딩이 가능하지만 함수의 스펙을 바꿀 수 있다.
        return "str"

print(Child().age) # >>> '3'
print(Child().test()) # >>> 'zzz'

## 클래스변수
class Class(): 
    class_var = 1

print(Class.class_var) # >>> '1'
Class.class_var = 2
print(Class.class_var) # >>> '2', 클래스 변수는 객체와 달리 클래스로 만든 모든 객체에 공유된다는 특징이 있다.

object = Class()
object.class_var = 3
print(Class.class_var) # >>> '2', 클래스 변수에 영향을 주지 않는다.
print(object.class_var) # >>> '3', 객체에 lastname 이라는 객체 변수가 새롭게 생성된다.
