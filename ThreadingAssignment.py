import datetime
from threading import Thread

#calculate the time needed for counting till 1000000000

thread_op = []
def counter(Thread_No,n1,n2):
    num=0
    for i in range(n1,n2):
        num+=1
    
    thread_op.append({"Thread_No":Thread_No,"Num":num})

print("start_time",datetime.datetime.today().strftime("%d-%b-%Y %H:%M:%S"))

# Create a Thread Object using the Thread class of the threading module
t1=Thread(target= counter,args=(1,1,250000001,))
t1.start()
t1.join()

# Create a Thread Object using the Thread class of the threading module
t2=Thread(target= counter,args=(1,250000001,500000001,))
t2.start()
t2.join()

# Create a Thread Object using the Thread class of the threading module
t3=Thread(target= counter,args=(1,500000001,750000001,))
t3.start()
t3.join()

# Create a Thread Object using the Thread class of the threading module
t4=Thread(target= counter,args=(1,750000001,1000000001,))
t4.start()
t4.join()

print("End_time",datetime.datetime.today().strftime("%d-%b-%Y %H:%M:%S"))
print(thread_op)
