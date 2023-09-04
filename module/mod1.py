def add(a: int, b: int):
    return a + b
def sub(a: int, b: int):
    return a - b

## '__name__' 의 의미
## 내부적으로 사용하는 특별한 변수
## 직업 파일을 실행할 경우 '__name__' 변수에는 '__main__' 값이 저장된다.
## 하지만 파이썬 쉘이나 다른 모듈에서 import할 경우에는 '__name__' 변수에 모듈 이름이 저장된다.
if __name__ == "__main__":
    print(add(1, 2))
    print(sub(1, 2))