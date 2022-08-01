AGENDA:
What is Multitasking in python?
Types of Multitasking
What is a thread?
How to achieve Multithreading in python?
How to create Threads in python?
 . Without creating a class
 . By extending Thread class
 .Without extending Thread class
Advantages of Multithreading?

# What is the Mutlitasking in python?

#Multitasking in general capable of performing multiple task's simultaneous.
#Multitasking refers to ability of an operating system to perform different task's at the same time.

Example: we are downloading something in the PC and listing something in the PC and concurred paying game all of these performed by same OS. this is nothing but Multitasking.

Types of Multitasking?

There are two types of Multitasking in an OS.
1. Process Based
2. Thread Based

1. Process Based():
   Process based is nothing but 2 (or) more processors functions concurrently running on the same OS.
   The smallest unit of process based multitasking is called processed based.
   Multiple threads running on the same OS simultaneously.
   Example: Downloading, listening to songs and playing a game.

2. Thread Based().
   Multithread came into picture, when single processor has to perform multiple task's to be achieved, all these task's are independent or part of same process.

What is the Thread?
 Smallest unit of multithreading is thread.
 Basically independent flow of execution single processor can consists of multiple threads, each thread in programming ca perform particular task.

Multithread:
In order to create a thread in python, you have to import threading module.

Syntax:
       import threading
       from threading import *

When to use Multithread?
Multithreading is very useful and saving time and improving performance, but it cannot be applied anywhere.
1. Multiple tasks need to achieved
2. Tasks do not have interdependency.

How to create a Threads in Python?
There are 3 ways to create a Thread in python.

1. Without creating a class
2. By extending Thread class
3. Without extending Thread class

Among 3 methods, 2nd method is most standard way of creating threads in python.

1. Without creating a class?

Code:

def new():
    for x in range(6):
        print("chaild execution...")
t1 = Thread(target = new)
t1.start()
print("bye")

Output:
chaild execution...bye

chaild execution...
chaild execution...
chaild execution...
chaild execution...
chaild execution...

Another Example:
def new():
    for x in range(6):
        print("chaild execution...")
t1 = Thread(target = new)
t1.start()
t1.join()
print("bye")

Output: 
chaild execution...
chaild execution...
chaild execution...
chaild execution...
chaild execution...
chaild execution...
bye

Example - 3
def new():
    for x in range(6):
        print("chaild execution...", current_thread().getName())
t1 = Thread(target = new)
t1.start()
t1.join()
print("bye", current_thread().getName())

Output:
chaild execution... Thread-13
chaild execution... Thread-13
chaild execution... Thread-13
chaild execution... Thread-13
chaild execution... Thread-13
chaild execution... Thread-13
bye MainThread

Example - 3:
def new():
    for x in range(6):
        print("chaild execution...", current_thread().getName())
t1 = Thread(target = new)
print( current_thread().getName())
t1.start()
t1.join()
print("bye", current_thread().getName())

Output:
MainThread
chaild execution... Thread-14
chaild execution... Thread-14
chaild execution... Thread-14
chaild execution... Thread-14
chaild execution... Thread-14
chaild execution... Thread-14
bye MainThread

2. By Extending the Thread class():

Code:
import threading
class A(threading.Thread):
    def run(self):
        for i in range(7):
            print("chaild = ", current_thread().getName())
obj = A()
obj.start()
obj.join()
print("control return to ", current_thread().getName())

Output:
chaild =  Thread-35
chaild =  Thread-35
chaild =  Thread-35
chaild =  Thread-35
chaild =  Thread-35
chaild =  Thread-35
chaild =  Thread-35
control return to  MainThread

3. Without Extending the thread class:
code:
class ex:
    def B(self):
        lst = [2,1,'w', 8.7, "abcd"]
        for i in lst:
            print("chaild printing ", i)
myobj = ex()
t1 = Thread(target = myobj.B)
t1.start()
t1.join()
print("done")

output:
chaild printing  2
chaild printing  1
chaild printing  w
chaild printing  8.7
chaild printing  abcd
done

Advantages of Multithreading:
1. Enhanced performance by decreased development time
2. Simplified and streamlined program coding
3. Simultaneous and parallelized occurence of tasks
4. Better use of CPU resource

code:
import time
def d2(n):
    for i in n:
        time.sleep(1)
        print(i%2)
def d3(n):
    for i in n:
        time.sleep(1)
        print(i%3)
n = [2,4,3,5,6,7,8,9]
s = time.time()
d2(n)
d3(n)
e = time.time()
print(e-s)

output:
0
0
1
1
0
1
0
1
2
1
0
2
0
1
2
0
16.1211678981781

Another example: with using Thread function.
import time
def d2(n):
    for i in n:
        time.sleep(1)
        print(i%2)
def d3(n):
    for i in n:
        time.sleep(1)
        print(i%3)
n = [2,4,3,5,6,7,8,9]
s = time.time()
t1 = Thread(target = d2, args = (n,))
t2 = Thread(target = d3, args = (n,))
t1.start()
t2.start()
t1.join()
t2.join()
e = time.time()
print(e-s)

Output:

02

01

01

12

00

11

02

10

8.088833570480347

