# --- json : json 데이터 처리 모듈
import json

## load : json 파일을 읽고 dictionary 로 변환하여 반환
import tempfile

with tempfile.TemporaryFile("r+") as file_json:
    file_json.write('{ "test": 1 }')
    file_json.seek(0)
    json_data = json.load(file_json)
    type(json_data) # <class 'dict'>

## dumps : dictionary 자료형을 json 문자열로 변환
dict = { "a": 1 }
json_str = json.dumps(dict)
print(json_str)

## dump : dictionary 자료형을 json 파일로 생성
with tempfile.TemporaryFile("r+") as file_json:
    dict = { "한글": "ㄱㄴㄷㄹ" }
    json.dump(dict, file_json) # 유니코드로 변환
    file_json.seek(0)
    file_json.read() # {"\ud55c\uae00": "\u3131\u3134\u3137\u3139"}
    
    file_json.truncate(0) # 파일 크기를 0byte로 조정, 파일 크기를 지정하지 않으면 현재 위치의 크기로 지정된다.
    json.dump(dict, file_json, ensure_ascii=False) # 유니코드(아스키) 변환 X
    file_json.seek(0)
    file_json.read() # {"한글": "ㄱㄴㄷㄹ"}

list_json = json.dumps([1, 2, 3]) # '[1, 2, 3]'
tuple_json = json.dumps((1, 2, 3)) # '[1, 2, 3]'