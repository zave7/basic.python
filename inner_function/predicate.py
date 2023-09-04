# --- all
## 반복가능한 데이터를 입력값으로 받아 모두 참일 경우 True 반환 
all([True, { "a": 1 }, " ", 1]) # True
all([False, {}, "", 0]) # False

# --- any
## 반복가능한 데이터를 입력값으로 받아 하나라도 경우 True 반환
all(False, False, False, False, True) # True
all(False, False, False, False, False) # False