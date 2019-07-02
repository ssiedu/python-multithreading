import time;


def square(numbers):
    for n in numbers:
        time.sleep(0.2);
        print("SQUARE  : ",n*n);
        
def cube(numbers):
    for n in numbers:
        time.sleep(0.2);
        print("CUBE  : ",n*n*n);

print("CALCULATION BEGINS  : ");

data=[2,3,4,5,6,7];
t1=time.time();
square(data);
cube(data);
t2=time.time();
print(t1);
print(t2);
print("DONE  IN  : ",t2-t1, "SECONDS");