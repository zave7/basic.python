# --- dir
## 객체가 지닌 변수나 함수를 보여주는 함수
dir((1,2)) # 튜플이가진 변수와 함수명 반환

# --- id
## 객체를 입력받아 객체의 고유 주솟값을 반환
id(1) # 4344964328

# --- isinstance
## 객체와 클래스를 입력받아 객체가 클래스 타입인지 여부 반환
class Target():
    pass
isinstance(1, Target) # False
isinstance(Target(), Target) # True

# --- type
## 입력값의 자료형이 무엇인지 알려주는 함수
type(1==1) # bool