# --- math
import math

## gcd : 최대공약수를 구하는 함수 (python 3.5 버전부터 존재)
gcd_val = math.gcd(77, 99, 11) # 11

## lcm : 최소 공배수를 구하는 함수 (python 3.9 버전부터 존재)
lcm_val = math.lcm(3, 9, 18) # 18

# --- fractions : 유리수를 표현할 때 사용하는 표준 라이브러리
from fractions import Fraction
## Fraction
Fraction(1, 5) # 5분의 1
Fraction('1/3') # 3분의 1