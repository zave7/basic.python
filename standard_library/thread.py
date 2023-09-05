# --- thread 
import threading
import time

def long_task(): 
    for i in range(5):
        print(f"working {i}")
        time.sleep(1)

print("Start")
threads = []
for i in range(5): 
    thread = threading.Thread(target=long_task)
    threads.append(thread)

for t in threads:
    t.start()

for t in threads:
    t.join()
print("End")