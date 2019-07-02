import time;
import threading;

def square(numbers):
    for n in numbers:
        time.sleep(10);
        print("SQUARE  : "+str(n*n));
        
def cube(numbers):
    for n in numbers:
        time.sleep(10);
        print("CUBE  : "+str(n*n*n));

print("CALCULATION BEGINS  : ");

data=[2,3,4,5,6,7];
t1=time.time();
thread1=threading.Thread(target=square,args=(data,));
thread2=threading.Thread(target=cube,args=(data,));
thread1.start();
thread2.start();
#square(data);
#cube(data);
thread1.join();
thread2.join();
t2=time.time();
print("DONE  IN  : ",t2-t1, "SECONDS");     