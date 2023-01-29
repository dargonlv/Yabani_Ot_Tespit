import threading
import time 

def calistir(threadName): 
    for i in range(7):
        print(threadName ,"çalışıyor")
        time.sleep(1)
        
        
def calistir2(ss):
    while True:
        print(ss,"ikinci") 
        time.sleep(0.5)

t1 = threading.Thread(target=calistir, args = ("thread-1", ))
t2 = threading.Thread(target=calistir2, args = ("thread-2", ))

t1.start()
t2.start()