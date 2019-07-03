import time
import threading;

def processSalary(eno,basic):
    print("Basic of ",eno, " is ",basic);
    if(eno==112):
        v=input("enter your last basic");
        print("YOUR INPUT ",v);
    print("HRA of ",eno, " is ",(basic*.20));
    print("DA of ",eno, " is ",(basic*.15));
    print("COMPLETED FOR : ",eno);
t1=threading.Thread(target=processSalary,args=(111,12000));
t2=threading.Thread(target=processSalary,args=(112,24000));
t3=threading.Thread(target=processSalary,args=(113,36000));
t1.start();
t2.start();
t3.start();
t1.join();
t2.join();
t3.join();
print("END-OF-PROFCESS");