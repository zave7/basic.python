# 튜플
# 튜플은 immutable list 이다.
# 따라서 요소을 변경시키는 것 이외에는 동일한 동작을 한다.

make_mistake = (1)
print(make_mistake) # >>> '1', 요소가 한개인 튜플을 만들기 위해서는 반드시 마지막에 ','를 붙여야 한다.
make_correct = (1,)
print(make_correct) # >>> (1,)

del (1,)[0] # TypeError: 'tuple' object doesn't support item deletion
# 요소는 변경될 수 없다.