# --- time
import time

## time : UTC를 사용하여 현재 시간을 실수 형태로 반환
print(time.time()) # 1693876905.844053

## localtime : time이 반환한 실수값을 사용해서 연,월,일,시,분,초의 형태로 변환
## 인수 없이 호출 시 현재 시각을 기준으로 반환
struct_time = time.localtime(time.time()) # struct_time
# (tm_year=2023, tm_mon=9, tm_mday=5, tm_hour=10, tm_min=30, tm_sec=51, tm_wday=1, tm_yday=248, tm_isdst=0)

## asctime : localtime가 반환된 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 반환
## 인수 없이 호출 시 현재 시각을 기준으로 반환
asc_time: str = time.asctime(struct_time) # Tue Sep  5 10:34:08 2023

## ctime : time.asctime(time.localtime(time.time())) 을 간단하게 현재시간만을 반환
ctime: str = time.ctime() # Tue Sep  5 10:35:58 2023

## strftime : 시간게 관계된 것을 세밀하게 표현하는 여러 가지 포맷 코드를 제공하는 함수
## 인수 없이 호출 시 현재 시각을 기준으로 반환
## format code : https://wikidocs.net/33#timestrftime
strf_day: str = time.strftime('%d', time.localtime(time.time()))

## sleep : 일정한 시간 간격을 지연시키는 함수
## 초단위로 실수 형태로 입력값을 받는다
for i in range(10):
    print(i)
    time.sleep(1)

