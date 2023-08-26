# If

## 비교연산자, 논리연산자
num = 1
if num == 1 or num == 2:
    print(num) # >>> '1'
elif num == 0 and -1:
    print("zero")
else:
    print(not num)

### in
if "a" in ["a", "b", "c"]:
    print("contains") # >>> 'contains'
else:
    print("not contiains")

### not in
if {} not in [{}]:
    print("not in")
else:
    print("in") # >>> 'in'

### in string
if "c" in "car":
    print("in str") # >>> 'in str'
else:
    print("not in str")

### pass
if 1 == 1:
    pass
else:
    print("not pass")

### conditional expression
print("참" if 1 == 1 else "거짓") # >>> '참'