# --- sympy : 방정식 기호를 사용하게 해주는 라이브러리

## sympy 설치
### $ pip install sympy

import sympy
from fractions import Fraction

## symbols : 'x'처럼 방정식에 사용하는 미지수를 나타내는 기호를 생성하여 반환
x = sympy.symbols("x")
y, z = sympy.symbols("y, z")

## Eq : a와 b가 같다는 방정식
f_1 = sympy.Eq(1, 2)
f_2 = sympy.Eq(x * Fraction(2, 5), 1760)

## solve : 방정식에서 미지수의 해를 구하여 반환, 방정식의 해는 여러개일 수 있으므로 리스트로 반환
result_one = sympy.solve(f_2) # [4400]
result_two = sympy.solve(sympy.Eq(x*x, 4)) # [-2, 2]

### 미지수가 2개 이상이면 딕셔너리로 반환
# 연립 방정식 (simultaneous equations)
_x, _y = sympy.symbols('_x _y')
se_f1 = sympy.Eq(_x + _y, 4)
se_f2 = sympy.Eq(_x * _y, 3)
result = sympy.solve([se_f1, se_f2]) # 연립 방정식의 경우 list 타입으로 전달
result # [{_x: 1, _y: 3}, {_x: 3, _y: 1}]
