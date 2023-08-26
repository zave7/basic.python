# 불

a = True
b = False
print(f"{a} and {b}") # >>> 'True and False'
print(1 == 1) # >>> 'True'

## 자료형의 bool
### String
print(bool("bool")) # >>> 'True'
print(bool("")) # >>> 'False'
### List
print(bool([1,2,3])) # >>> 'True'
print(bool([])) # >>> 'False'
### Tuple
print(bool((1,2))) # >>> 'True'
print(bool(tuple())) # >>> 'False'
### Dictionary
print(bool({ "b" : True })) # >>> 'True'
print(bool({})) # >>> 'False'
### Number
print(bool(1)) # >>> 'True'
print(bool(0.1)) # >>> 'True'
print(bool(-1)) # >>> 'True'
print(bool(0)) # >>> 'False'
### None
print(bool(None)) # >>> 'False'
