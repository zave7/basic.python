# 문자열 (immutable 자료형)

## 만들기
make_1 = "Hello python double quotation"
make_2 = 'Hello pyton single quotations'
make_3 = """Hello python triple double quotation"""
make_4 = '''Hello python triple single quotation'''

## 쿼테이션 중첩
overlap_quo_1 = "Hello Python's World"
overlap_quo_2 = 'Hello "Python"'
backslash_1 = 'Python\'s world'
backslash_2 = "Python\" world"

## 문자열 변수 대입
assign_1 = "Hello\npython"
assign_2 = """
    Multiline
"""
assign_3 = '''
    Multiline
'''

## 문자열 연산
hello = "Hello"
python = "python"
connect_1 = hello + python
multiplication = "=" * 5
print(multiplication) # >>> '====='

## 문자열 길이
print(len("1234")) # >>> 4

## 인덱싱과 슬라이싱
index = "123456789"
print(index[0]) # >>> '1'
print(index[-1]) # >>> '9'
print(index[0:4]) # >>> '1234'
print(index[0:]) # >>> '123456789'
print(index[:4]) # >>> '1234'
print(index[:]) # >>> '123456789'
print(index[:-3]) # >>> '123456'

## 문자열 포매팅

### 문자열 포맷 코드
print("Hello Number(%d)" % 3) # >>> 'Hello Number(3)', '%d' 문자열 포맷 코드
print("Hello %s" % "python") # >>> 'Hello python'
print("Hello %s" % 1) # >>> 'Hello 1', %s 에는 모든 타입이 올 수 있다. (문자열 자동 변환)
print("Hello %s (%d)" % ("Double", 2)) # >>> 'Hello Double (2)'
print("%%test %d" % 3) # >>> '%test 3', 문자열 포맷 코드와 %가 같이 나타날 경우에는 '%%'로 치환해야 된다.
print("%10s." % "hi") # >>> '        hi.'
print("%-10s." % "hi") # >>> 'hi        .'
print("%0.4f" % 3.12345) # >>> '3.1235', 반올림 되어 출력된다.
print("%.4f" % 3.12345) # >>> '3.1235'
print("%10.4f" % 3.12345) # >>> '    3.1235', 공백이 채워진다.
print("%-10.4f" % 3.12345) # >>> '3.1235    ', 공백이 채워진다.
### format
print("Was I sad {}".format("🥺")) # >>> 'Was I sad 🥺'
print("Was I sad {0}".format("🥺")) # >>> 'Was I sad 🥺'
print("My favorite number is {}".format(1)) # >>> 'My favorite number is 1'
print("Put more than one value {0} {1}".format("one", 2)) # >>> 'Put more than one value one 2'
print("Put in by name {name}".format(name = "!!")) # >>> 'Put in by name !!'
print("Mix index({0}) and name({name})".format(1, name = "chan")) # >>> 'Mix index(1) and name(chan)'
print("Left Alignment ({0:<10})".format("hi")) # >>> 'Left Alignment (hi        )'
print("Right Alignment ({0:>10})".format("hi")) # >>> 'Right Alignment (        hi)'
print("Center Alignment ({name:^10})".format(name = "hi")) # >>> 'Center Alignment (    hi    )'
print("Fill out the space ({:=^10})".format("hi")) # >>> 'Fill out the space (====hi====)'
print("Expressing decimal points ({:.4f})".format(3.12345)) # >>> 'Expressing decimal points (3.1235)'
print("Expressing decimal points ({:10.4f})".format(3.12345)) # >>> 'Expressing decimal points (    3.1235)'
print("Brace Expressing }}{}{{".format(1)) # >>> 'Brace Expressing }1{'
name = "찬"
age = "26"
print(f"제 이름은 {name * 2}이고 나이는 {age}세 입니다.") # >>> '제 이름은 찬찬이고 나이는 26세 입니다.', python 3.6 버전부터 문자열 인터폴레이션을 지원한다.

## 문자열 관련 함수

### count
print("hobby".count('b')) # >>> '2'
### find 
print("Hello python".find('o')) # >>> '4'
print("Hello python".find('z')) # >>> '-1'
### index
print("Hello python".index('o')) # >>> '4'
#print("Hello python".index('z')) # >>> ValueError: substring not found
### join
print(",".join(['a', 'b', 'c'])) # >>> 'a,b,c'
### upper
print("hi".upper()) # >>> 'HI'
### lower
print("HI".lower()) # >>> 'hi'
### 공백 지우기
print(" left ".lstrip()) # >>> 'left '
print(" right ".rstrip()) # >>> ' right'
print(" both side".strip()) # >>> 'both side'
### replace
print("Hi python".replace("python", "rust")) # >>> 'hi rust'
### split
print("Are you busy now?".split()) # >>> '['Are', 'you', 'busy', 'now?']', 인자값을 넘겨주지 않으면 공백으로 나눈다.
print("Are,you,busy,now?".split(",")) # >>> '['Are', 'you', 'busy', 'now?']'
