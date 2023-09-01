import sys

# 파이썬에서는 sys모듈을 사용하여 프로그램에 인수를 전달할 수 있다.

args = sys.argv[1:]
for i in args:
    print(i)

# python3 sys.py test1 test2 test3
# 출력
# test1
# test2
# test3