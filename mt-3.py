import time;

class SquareCalc:
    def square(this,numbers):
        for n in numbers:
            time.sleep(0.2);
            print("SQUARE  : ",n*n);

class CubeCalc:        
        def cube(this,numbers):
            for n in numbers:
                time.sleep(0.2);
                print("CUBE  : ",n*n*n);

print("CALCULATION BEGINS  : ");

data=[2,3,4,5,6,7];

ob1=SquareCalc();
ob2=CubeCalc();

t1=time.time();
ob1.square(data);
ob2.cube(data);
t2=time.time();
print("DONE  IN  : ",t2-t1, "SECONDS");