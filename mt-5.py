import time;
import threading;

def square(numbers):
    indsq=threading.current_thread().ident;
    print("Square Indent : "+str(indsq));
    name=threading.currentThread().getName();
    for n in numbers:
        time.sleep(.10);
        print("SQUARE By - "+name+" : "+str(n*n));
        
def cube(numbers):
    indcb=threading.current_thread().ident;
    print("Cube Indent : "+str(indcb));
    name=threading.currentThread().getName();
    for n in numbers:
        time.sleep(.10);
        print("CUBE By - "+name+"  : "+str(n*n*n));

print("CALCULATION BEGINS  : ");

data=[2,3,4,5,6,7];
t1=time.time();
thread1=threading.Thread(target=square,args=(data,));
thread2=threading.Thread(target=cube,args=(data,));
#thread1.setName("Th-Sq");
#thread2.setName("Th-Cb");
thread1.start();
thread2.start();
#square(data);
#cube(data);
print("ACTIVE COUNT  : ",threading.activeCount());
thread1.join();
thread2.join();
t2=time.time();
ct=threading.current_thread();
print(ct.getName());
print(ct.ident);
print("DONE  IN  : ",t2-t1, "SECONDS");     