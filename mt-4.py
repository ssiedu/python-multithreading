import time;
from threading import Thread;

class SquareCalc(Thread):
    
    def __init__(self,numbers):
        Thread.__init__(self);
        self.numbers=numbers;

    def run(self):
        self.square();

    def square(self):
        for n in self.numbers:
            time.sleep(0.2);
            print("SQUARE  : ",n*n);

class CubeCalc(Thread):
        def __init__(self,numbers):
            Thread.__init__(self);
            self.numbers=numbers;
            
        def cube(self):
            for n in self.numbers:
                time.sleep(0.2);
                print("CUBE  : ",n*n*n);

print("CALCULATION BEGINS  : ");

data=[2,3,4,5,6,7];

ob1=SquareCalc(data);
ob2=CubeCalc(data);

t1=time.time();
ob1.start();
ob2.start();
ob1.join();
ob2.join();
t2=time.time();
print("DONE  IN  : ",t2-t1, "SECONDS");