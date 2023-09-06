# --- traceback : 프로그램 실행 중 발생한 오류 추적 모듈
import traceback

def a():
    a = 1 / 0
def b():
    a()
def c():
    b()

try:
    c()
except:
    print(traceback.format_exc())
# Traceback (most recent call last):
#   File "/Users/zave/Private/dev/learning/python/standard_library/exception.py", line 12, in <module>
#     c()
#   File "/Users/zave/Private/dev/learning/python/standard_library/exception.py", line 9, in c
#     b()
#   File "/Users/zave/Private/dev/learning/python/standard_library/exception.py", line 7, in b
#     a()
#   File "/Users/zave/Private/dev/learning/python/standard_library/exception.py", line 5, in a
#     a = 1 / 0
#         ~~^~~
# ZeroDivisionError: division by zero