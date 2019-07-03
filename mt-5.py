import time
import multiprocessing

def processSalary(eno,basic):
    print("Basic of ",eno, " is ",basic);
    if(eno==112):
        v=input("enter your last basic");
    print("HRA of ",eno, " is ",(basic*.20));
    print("DA of ",eno, " is ",(basic*.15));
    
    
processSalary(111,10000);
processSalary(112,20000);
processSalary(113,30000);