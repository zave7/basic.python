# --- shutil : 파일을 복사하거나 이동할 때 사용하는 모듈
import shutil

## copy : 파일 복사
shutil.copy("./file/test1.txt", "./file/test2.txt")

## move : 이동
shutil.move("./file/test1.txt", "./file/test3.txt")

# --- glob : 디렉토리에 있는 파일 이름을 모두 조회할 때 사용하는 모듈
import glob
file_path_list: list[str] = glob.glob("./file/*") # ['./file/test2.txt', './file/test3.txt']

# --- pickle : 직렬화
import pickle

data = {
    "key": "value"
}

## dump : 직렬화
with open("./file/test1.txt", "wb") as file_pickle:
    pickle.dump(data, file_pickle)

## load : 역직렬화
with open("./file/test1.txt", "rb") as file_pickle_read:
    data = pickle.load(file_pickle_read) # {'key': 'value'}

# --- os
import os

## environ : 시스템 환경 변수 반환
os.environ # dictionary
os.environ["PATH"]

## path.expanduser('~) 홈디렉토리
home_path = os.path.expanduser('~')


## chdir : 디렉토리 위치 변경하기
os.chdir(f"{home_path}/Private/dev/learning/python/")

## getcwd : 현재 디렉토리 위치 반환
print(os.getcwd())

## system : 시스템 명령어 호출하기
## 시스템 자체의 프로그램이나 기타 명령어를 파이썬에서 호출할 수 있다.
## `os.system("명령어")`
os.system("ls")
os.system("ls -al")

## popen : 시스템 명령어를 실행한 결과값을 읽기 모드 형태의 파일 객체로 반환
file_ls = os.popen("ls")

## mkdir : 디렉토리 생성
os.mkdir("디렉토리경로")

## rmdir : 디렉토리 삭제
os.rmdir("디렉토리경로")

## remove : 파일 삭제
os.remove("파일경로")

## rename : 파일명 변경
os.rename("소스 파일", "타겟 파일")

# --- zipfile : 여러개의 파일을 zip 형식으로 합치거나 해제할 때 사용하는 모듈
import zipfile

## 묶기
with zipfile.ZipFile("./file/filename.zip", 'w') as zip:
    zip.write('./file/test1.txt')
    zip.write('./file/test2.txt')
    zip.write('./file/test3.txt')

## 해제
with zipfile.ZipFile("./file/filename.zip") as zip:
    zip.extractall("./file/compact/")

## 특정 파일만 해제
# with zipfile.ZipFile("./file/filename.zip") as zip:
#     zip.extract("test1.txt")

## 압축 묶기
with zipfile.ZipFile("./file/filename.zip", 'w', compression=zipfile.ZIP_LZMA, compresslevel=9) as zip:
    pass
### ZIP_STORED : 압축하지 않고 파일을 zip으로만 묶는다. 속도가 빠르다.
### ZIP_DEFLATED : 일반적인 zip 압축ㅇ로 속도가 빠르고 압축률은 낮다(호환성이 좋음).
### ZIP_BZIP2 : bzip2 압축으로 압축률이 높고 속도가 느리다.
### ZIP_LZMA : lzma 압축으로 압축률이 높고 속도가 느리다(7zip과 동일한 알고리즘으로 알려져있다).

### compressionlevel 은 압축 수준을 의미하는 숫자값으로, 1~9를 사용한다. 1은 속도가 가장 빠르지만 압축률이 낮고, 9는 속도가 가장 느리지만 압축률이 높다.

# --- tempfile : 파일을 임시로 만들어서 사용할 수 있는 모듈
import tempfile

## mkstemp : 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 반환
filename = tempfile.mkstemp()

# TemporaryFile : 임시 저장 공간으로 사용할 파일 객체를 반환
## 이 파일은 기본적으로 바이너리 쓰기 모드를 갖는다.
## close 가 호출되면 이 파일은 자동으로 삭제된다.
with tempfile.TemporaryFile('r+b') as file_temp:
    pickle.dump({"a": 1}, file_temp) # 바이너리를 저장하면서 커서가 파일의 맨 뒤로 이동
    file_temp.seek(0) # EOFError: Ran out of input, 끝에 있기 때문에 커서를 파일의 맨 앞으로 이동
    pickle.load(file_temp)


    
