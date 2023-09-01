# iterate

## while

count = 5
while count:
    print("while", end = ',') # >>> 'while,while,'
    count-=1
    if(count == 1): 
        print()
        break
    else:
        count = 2
        continue

## for
for i in [1,2,3]:
    print(i, end = ',')
print()
for (a, b) in [(1,2), (3,4)]:
    print(f"{a} {b}")
for i in range(0, 5):
    print(i) # >>> 0~4

### List Comprehension
list = [
    i*j 
    for i in range(0, 10) if i%2 == 0 if 0<i<5 # if 문 중첩 가능
    for j in range(1, 10) # for 문 중첨가능
]
print(list)
# >>> [2, 4, 6, 8, 10, 12, 14, 16, 18, 4, 8, 12, 16, 20, 24, 28, 32, 36]

### Dictionary Comprehension
students = [("승운", 10), ("예진", 0), ("현성", 100)]
dic = {
    name: (score, "통과" if score >= 90 else "낙제")
    for (name, score) in students if score >= 10
}
print(dic) # >>> '{'승운': (10, '낙제'), '현성': (100, '통과')}'

### Set Comprehension
names = set(["승운", "예진", "현성"])
set = { name for name in names if name != "현성" }
print(set) # >>> {'승운', '예진'}