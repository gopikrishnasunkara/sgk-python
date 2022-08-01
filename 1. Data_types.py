#print("jai srirama")

#List funtions()
'''l = [1,2,3,4,5,6,7,8,9,10]
print(l)
print(type(l))
print(dir(l))
 #'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove',
# 'reverse', 'sort']

l.append([5,67,8,9,10,11,12,13])
print(l)

l2 = [1,2,3,4,5,6,7,8,9,10]
l2.clear()
print(l2)

l3 = l.copy()
print(l3)

print(l.count(1))
l2.extend(l3)
print(l2)
print(l2.index(10))
print(l2[::2])
print(l2[0:10:-1])
print(l2[10:0:-1])

print(l2.pop())
print(l2)

l2.remove(10)
print(l2)

l2.reverse()
print(l2)

l4 = [10,20,30,40,9,900,80,78,600,1000]
l4.sort()
print(l4)

print(len(l4))

l5 = [[1,2,3,4],[5,6,7,8]]
l6 = []
for i in l5:
    for j in i:
        l6.append(j)
print(l6)
print(l5)
print()
print()
#Tuple funtions()

t = (1,2,3,4,5,6,7,10.5,11,100.50,"hello")
#print(t)
#print(type(t))
#print(dir(t))
#'count', 'index'
#print(t.count(1))
print(len(t))
#print(max(t))
print(t[00:10:-1])

#Set Function()

s = {1,1,2,3,4,5,6,8,7,9,7,4,10,11,22,15,16,14,14,15,16,1,61,25}
#print(s)
#print(type(s))
#print(dir(s))

# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard','intersection', 
#'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop','remove',
# 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'


s.add(55)
print("this is after add: ",s) 

s1 = {1,1,2,3,4,5,6,8,7,9,7,4,10,11,22,15,16,14,14,15,16,1,61,25}
s1.clear()
print()
print(s1)

s1 = s.copy()
print("this is after copy: ",s1)
s1.update([16,7,85])
print("this is after Update: ",s1)

s2 = {1,2,3,4,5,67, 6,7}
s3 = {6,7,8,9,10,11,6,7}
print(s2.union(s3))
print(s2.intersection(s3))

s5 = {'a','b','c','d','e'}
s6 = {'c','d','f','g','h'}

print(s5-s6)
print(s6-s5)

print(s5.difference(s6))
print(s6.difference(s5))

s7 = {'a','b','c','d','e'}
s8 = {'c','d','f','g','h'}
r = s7.difference_update(s8)
print(s7)
print(s8)
r1 = s8.difference_update(s7)
print("iam from s7: ",s7)
print("Iam from s8: ", s8)

s9 = {1,2,3,4,5,6,7,8,9,10,1500}
s9.discard(1501)
print(s9)


s10 = {'a','b','c','d','e'}
s11 = {'c','d','f','g','h'}

#print(s10.intersection(s11))
#print(s11.intersection(s10))
#r = s10.intersection_update(s11)
#print(s10)
#print(s11)
r = s11.intersection_update(s10)
print(s10)
print(s11)
# 'symmetric_difference', 'symmetric_difference_update'

s12 = {1,2,3,4,5,6,7,8,9,10,11,12,13,14}
s13 = {8,9,10,11,12,13,14}

print(s12.issuperset(s13))
print(s13.issubset(s12))

A = {2, 4, 5, 6}
B = {7, 8, 9, 10}

print(A.isdisjoint(B))
print(B.isdisjoint(A))
print(A.pop())
B.remove(10)
print(B)

s15 = {1,2,3,4,5}
s16 = {3,4,5,6,7}
#print(s15.symmetric_difference(s16))
#print(s16.symmetric_difference(s15))
#r = s15.symmetric_difference_update(s16)
r = s16.symmetric_difference_update(s15)
print(s15)
print(s16)

#Dictionary set()
mydict = {'name': "vissu", 'age': 27, "address": "Tenali"}
print(mydict)
#print(type(mydict))
#print(dir(mydict))
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault',
#'update', 'values']
mydict1 = {'name': "vissu", 'age': 27, "address": "Tenali"}
mydict1.clear()
print(mydict1)
mydict1 = mydict.copy()
print(mydict1)
mydict1 = {'name': "vissu", 'age': 27, "address": "Tenali"}
mydict1['name']
'vissu'
print(mydict1.get('qualification'))
None
mydict1['qualification'] = "B-Tech"
mydict1
{'name': 'vissu', 'age': 27, 'address': 'Tenali', 'qualification': 'B-Tech'}
mydict1['name'] = "viswanath"
mydict1
{'name': 'viswanath', 'age': 27, 'address': 'Tenali', 'qualification': 'B-Tech'}
d = {'a': 1, 'b':2}
e = {'c': 3, 'd': 4}
c = d.update(e)
print(d)
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(e)
{'c': 3, 'd': 4}
d.pop('a')
1
d
{'b': 2, 'c': 3, 'd': 4}
d.popitem()
('d', 4)
d
{'b': 2, 'c': 3}
del d
d
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'd' is not defined
mar = {}.fromkeys(['maths','phys','english'],0)
print(mar)
{'maths': 0, 'phys': 0, 'english': 0}
mydict1
{'name': 'viswanath', 'age': 27, 'address': 'Tenali', 'qualification': 'B-Tech'}
mydict1.keys()
dict_keys(['name', 'age', 'address', 'qualification'])
mydict1.values()
dict_values(['viswanath', 27, 'Tenali', 'B-Tech'])
mydict1.items()
dict_items([('name', 'viswanath'), ('age', 27), ('address', 'Tenali'), ('qualification', 'B-Tech')])

#String Funcations():

s = "hello world!"
#print(s)
#print(type(s))
#print(dir(s))

#'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find'
##, 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 
#'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper',

print(s.capitalize())
s1 = "HELLO WORLD!"
print(s1.casefold())
print(s1.center(15,"$"))
print(s1.count('L'))
print(s1.endswith('D!'))
print(s1.startswith('HE'))

str = "PYTHON!"
s2 = str.encode()
print(s2)

str = 'xyz\t12345\tabc'
print(str)
res = str.expandtabs(2)
print(res)

s2 = "I love india, i'm the part of india"
print(s2.rfind('L'))
#print(s2.rindex('L'))

print("hello {0}, your age is {1}.".format("shankar", 28))
print("hello {name}, your age is {age}.".format(name = "shankar", age = 28))

p = {'x':5, 'y': 7}
print('{x} and {y}'.format_map(p))
#print('{x} and {y} and {z}'.format_map(p))

s2 = "hello123"
print(s2.isalnum())
s
s = "hello"
print(s.isalpha())
s1 = '123456'
print(s1.isdecimal())
print(s1.isdigit())
print(s.isidentifier())

s= "hello world!"
s.lower()
print(s)
print(s.islower())
s3 = "1234567"
print(s3.isnumeric())
print(s3.isprintable())

s4 = " "
print(s4.isspace())
s5 = "Hello World!"
print(s5.istitle())

s6 = "HELLO WORLD!"
print(s6.isupper())
s7 = ['I', "Love","India"]
print(" ".join(s7))
print("@".join(s7))

s8 = "python"
print(s8.ljust(12, '@'))
print(s8.rjust(12, '@'))
s9 = "    python    "
#print(s9.strip())
print(s9.lstrip())
print(s9.rstrip())

s10 = "@@@@@python@@@@@"
print(s10.lstrip('@'))
print(s10.rstrip('@'))
print(s9.strip('@'))

# 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 
#'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 
#'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

dict = {'a': "123", "b":"456", "c":"789"}
string = "abc"
print(string.maketrans(dict))
s = "this, that, there, therefore, these"
print(s.split(',', 4))
print(s.rsplit(',', 2))

str = "python is fun"
print(str.partition("python"))
print(str.rpartition("is "))
s = "this, that, there, therefore, these"
t = "bat ball"
res = t.replace('b','c')
print(res)

t = 'a,b,a,c,d,e,e,f,g'
res = t.replace(',' ,'')
print(res)
str = "THIS SHOULD ALL BE lowercase"
print(str.swapcase())
str = "this should be a lowercase"
print(str.title())'''


a = ("john","charles", "mike")
b = ("jenny", "christy","monica")
x = zip(a, b)
print(tuple(x))

import sys
a = [10,12.15,'python','averages', 100]
b = (10,12.15,'python','averages', 100)
print(sys.getsizeof(a))
print(sys.getsizeof(b))