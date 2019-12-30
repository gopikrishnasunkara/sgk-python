Python enumerate():
The enumerate() method add a counter to an iterable and returns it(the enumerate object).

The syntax of enumerate() is:
enumerate(iterable, start=0)

Enumerate() Parameters:
The enumerate() method takes two parameters:
iterable() - a squence, an iterator, or objects that supports iteration.
start(optional) - enumerate() starts counting from this number. if start is omitted, o is taken as start.

Return Value from enumerate()
The enumerate() method adds counter to an iterable and returns it. The returned object is a enumerate object.

You can convert enumerate objects to list and tuple using list() and tuple() method respectively.

Example 1: How enumerate() works in Python?
a = [10,20,30,40]
 for i,b in enumerate(a):
...     print(i, ":", b)
...
Output:

0 : 10
1 : 20
2 : 30
3 : 40

Example2:
c = ["apple", "bat", "cat"]
>>> obj = enumerate(c)
>>> print(list(enumerate(c)))
output:
[(0, 'apple'), (1, 'bat'), (2, 'cat')]

Example3:
a=[10, 20, 30, 40]
>>> for i, c in enumerate(a, 10):
...     print(i,":",c)
Output:
10 : 10
11 : 20
12 : 30
13 : 40
Example4:
>>> grocery = ['bread', 'milk', 'butter']
>>> for item in enumerate(grocery):
...     print(item)

Output:

(0, 'bread')
(1, 'milk')
(2, 'butter')