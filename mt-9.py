import threading;

def disp():
    print("welcome");
    
def show():
    print("hello");
    t2=threading.Thread(target=disp);
    print("T2 Daemon "+str(t2.isDaemon()));
    

t1=threading.Thread(target=show);
print(t1.isDaemon());
t1.setDaemon(True);
print(t1.isDaemon());
t1.start();
mainthr=threading.current_thread();
print(mainthr.isDaemon());
mainthr.setDaemon(True);