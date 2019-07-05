from threading import *;
import time;

def job():
    for i in range(10):
        print("Job Doing : "+str(i));
        time.sleep(2);

t1=Thread(target=job);
t1.setDaemon(True);
t1.start();
time.sleep(5);
print("End of Main");

#when-ever all last non-daemon thread terminates automatically all daemon threads will be terminated automatically.
#if we remove setDaemon(True) then even after main Thread is terminated t1 will keep on running.
#if we set setDaemon(True) then just after main(non-daemon) terminates t1 automatically terminates.

# t1=Thread(target=job,daemon=True);
#another way to create a daemon thread.