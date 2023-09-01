# 파일 생성
test_file_1 = open("./file/test_file.txt", 'w')
## 읽기 모드 : r
## 쓰기 모드 : w
## 추가 모드 : a
test_file_1.close() # 다만, 프로그램을 종료할 때 열려있는 파일의 객체를 자동으로 닫아준다.

# 파일 쓰기
file_write_1 = open("./file/w1.txt", 'w')
for i in range(1, 11):
    data = f"{i}번 라인\n"
    file_write_1.write(data)
file_write_1.close()

# 파일 읽기
## 첫 라인
file_function_line1 = open("./function.py", 'r')
line = file_function_line1.readline()
print(line) # >>> '# 함수'
file_function_line1.close()
## 모든 라인
file_function_all = open("./function.py", 'r')
while True: 
    line = file_function_all.readline()
    if not line: break
    print(line)
file_function_all.close()
## readLines
file_function_lines = open("./function.py", 'r')
lines = file_function_lines.readlines()
print(lines) # 모든 라인을 가지는 list 반환(줄바꿈 포함)
for line in lines: line.strip() # 라인 끝의 개행 문자를 제거
file_function_lines.close()
## read
file_function_read = open("./function.py", 'r')
data = file_function_read.read()
print(data) # function.py 의 내용 전체를 한개의 문자열로 반환
## 파일 객체를 for 문과 함께 사용
file_for = open("./function.py", 'r')
for line in file_for:
    print(line)
file_for.close()

# 파일 내용 추가
# 쓰기 모드로 파일을 열 때 이미 내용이 존재하는 파일을 열면 그 파일의 내용이 모두 덮어 씌워지게 된다.
## 파일에 새로운 내용 추가하기
file_append = open("./file/append.txt", 'a')
for i in range(10):
    file_append.write(f"{i} 번째 추가\n")
file_append.close()

# with 문과 함께 사용하기
with open("./file/append.txt", 'w') as file_with:
    file_with.write("init")
# 위와 같이 with 문을 사용하면 with 블록을 벗어나는 순간, 열린 파일 객체가 자동으로 닫힌다.
# java 의 try-with-resource 와 유사하다.
