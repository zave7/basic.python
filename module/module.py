# module
import mod1 # 모듈단위 
from mod2 import div
import mod_class

print(mod1.add(1,1)) # >>> '2'
print(div(4,2)) # >>> '2.0'
print(__name__) # >>> '__main__'
print(mod1.__name__) # >>> 'mod1'
print(type(mod_class.ModuleClass()))

## 다른 디렉토리에 있는 모듈 불러오기
import sys
print(sys.path) # 파이썬 라이브러리가 설치되어있는 디렉토리 확인
sys.path.append("/Users/zave/Private/dev/learning/python/module") # 파이썬 패스에 모듈 경로 추가

## PYTHONPATH 환경변수 설정하기
# export PYTHONPATH="/Users/zave/Private/dev/learning/python/module"