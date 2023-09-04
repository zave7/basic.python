# 클래스 정의

class Calculator: 
    def __init__(self) -> None: # '->' : 화살표는 함수 리턴 값의 주석 역할을 한다.
        pass
    def add(a: int, b: int) -> int: # ': int' 매개변수에 대한 주석 역할을 한다.
        return a + b

class_type = Calculator()
print(type(class_type)) # >>> '<class '__main__.Calculator'>'

## 간단한 클래스 정의
class Pass:
    pass

class Self:
    def test(self): # 파이썬 클래스의 함수는 첫 번째 인자로 자기 자신 객체를 받는다.
                    # 클래스에서 바로 접근하면 생략해도 된다.
        print("hi")
        print(id(self))
print(type(Self())) # >>> '<class '__main__.Pass'>'

## 생성자
class Constructor:
    def __init__(self, test: int) -> None:
        self.test = test
        self._protected = test # '_' = 내부 사용 용도로 정의 (외부 접근 가능)
        self.__private = test # 외부에서 접근 불가능 (private)

## 프로퍼티 접근 제한
print(Constructor(test=1).test)
print(Constructor(test=1)._protected)
print(Constructor(test=1).__private) # AttributeError: 'Constructor' object has no attribute '__private'

