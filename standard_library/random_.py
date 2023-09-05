# --- random : 난수를 발생시키는 모듈
import random

## random
random_val_1 = random.random() # 0.0 ~ 1.0 사이의 실수 중 난수 값을 반환, 0.023461997948057034
rand_int = random.randint(1, 2) # a 이상 b 이하 값 중 난수 값을 반환
choice = random.choice((1,2,3)) # iterable 타입 값을 입력받아 그 값들 중 임의의 값을 반환
sample = random.sample([1,2,3,4,5], 3) # iterable 타입 값과 길이 값을 입력받아 섞어서 길이에 맞춰 반환
