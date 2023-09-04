# --- FileNotFoundError

# file = open("test", "r") # FileNotFoundError

try:
    file1 = open("test", "r")
except Exception as e:
    print(e) # >>> '[Errno 2] No such file or directory: 'test''

# --- ZeroDivisionError

# val = 1 / 0 # ZeroDivisionError: division by zero
try:
    val = 1 / 0
except:
    print("0으로 나눌 수 없습니다.") # >>> '0으로 나눌 수 없습니다.'

# --- Multiple catch, finally

try:
    file = open("file.py", "r")
    for line in file:
        print(line)
except FileNotFoundError as e:
    print("FileNotFoundError")
except Exception as e:
    print("Unknown Error")
finally:
    file.close()

# --- Once catch

try:
    file = open("file.py", "r")
    for line in file:
        print(line)
except (FileNotFoundError, Exception):
    print("Error")

# --- try-else

try: 
    print(2/2)
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
else:
    print("Exception이 발생하지 않았습니다.")

# --- Exception avoidance

try: 
    print(2/2)
except ZeroDivisionError:
    pass

# --- raise exception

try:
    raise Exception
except:
    print("Exception 발생")

# --- custom exception

class CustomException(Exception):
    pass
try:
    raise CustomException
except: 
    print("CustomException 발생")

# --- custom exception with str

class StringException(Exception):
    def __str__(self) -> str:
        return "String Exception 발생"
try:
    raise StringException
except Exception as e: 
    print(e)