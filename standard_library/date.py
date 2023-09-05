# --- datetime
import datetime

## date : 연, 월, 일로 날짜를 표현할 때 사용하는 함수

day1 = datetime.date(2023, 3, 3) # date 타입
day2 = datetime.date(2023, 3, 4)

## timedelta
diff = day2 - day1 # timedelta 객체가 반환
diff.days # 1

## weekday : 0-월요일 ~ 6-일요일
week_day = datetime.date(2023, 9, 5).weekday() # 화요일 1

## isweekday : 1-월요일 ~ 7-일요일
iso_week_day = datetime.date(2023, 9, 5).isoweekday() # 화요일 2