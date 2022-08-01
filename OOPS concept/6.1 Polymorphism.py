class ABC():
	def capital(self):
		print("iam a first method in ABC class")
	def language(self):
		print("iam a second method in ABC class")
	def type(self):
		print("iam a third method in ABC class")
class DEF():
	def capital(self):
		print("iam a first method in DEF class")
	def language(self):
		print("iam a second method in DEF class")
	def type(self):
		print("iam a third method in DEF class")

obj_abc = ABC()
obj_def = DEF()
for a in (obj_abc, obj_def):
	a.capital()
	a.language()
	a.type() '''


# class Deck():
# 	def talk(self):
# 		print("Quack... Quack")
# class Dog():
# 	def talk(self):
# 		print("Bow... Bow")
# class cat():
# 	def talk(self):
# 		print("Meow.. Meow")
# class Goat():
# 	def talk(self):
# 		print("Myaah.. Myaah")
# def f1(obj):
# 	obj.talk()
# l1 = [Deck(), Dog(), cat(), Goat()]
# for i in l1:
# 	f1(i)



# class Deck():
# 	def talk(self):
# 		print("Quack... Quack")
# class Dog():
# 	def bark(self):
# 		print("Bow... Bow")
# def f1(obj):
# 	obj.talk()
# d = Deck()
# f1(d)
# d = Dog()
# f1(d)


# class Deck():
# 	def talk(self):
# 		print("Quack... Quack")
# class Human():
# 	def talk(self):
# 		print("Hello..HI")
# class Dog():
# 	def bark(self):
# 		print("Bow... Bow")
# def f1(obj):
# 	if hasattr(obj, 'talk'):
# 		obj.talk()
# 	else:
# 		obj.bark()
# d = Deck()
# f1(d)
# h = Human()
# f1(h)
# d = Dog()
# f1(d)

# class Book():
# 	def __init__(self, pages):
# 		self.pages = pages
# 	def __add__(self, other):
# 		print(other.pages)
# 		return self.pages + other.pages
# b1 = Book(100)
# b2 = Book(200)
# print("total nof : ", b1 + b2)


# class student():
# 	def __init__(self, name, marks):
# 		self.name = name
# 		self.marks = marks
# 	def __gt__(self, other):
# 		return self.marks > other.marks
# 	def __le__(self, other):
# 		return self.marks <= other.marks
# s1 = student('krishna', 100)
# s2 = student('rama', 200)
# print(s1>s2)
# print(s1<s2)
# print(s1>=s2)
# print(s1<=s2)

# class employee():
# 	def __init__(self, name, salary):
# 		self.name = name
# 		self.salary = salary
# 	def __mul__(self, other):
# 		print(self.salary)
# 		print(other.days)
# 		return self.salary * other.days
# class timesheet():
# 	def __init__(self, name, days):
# 		self.name = name
# 		self.days = days
# e = employee("shaik", 500)
# t = timesheet("shaik", 25)
# print(e*t)


# class Test():
# 	def m1(self):
# 		print("there is no arguments")
# 	def m1(self, a):
# 		print("there is one arguments")
# 	def m1(self, a, b):
# 		print("There are two arguments in this", a * b)

# t = Test()
# # t.m1()
# # t.m1(10)
# t.m1(5, 10)


# class Test():
# 	def m1(self, a = None, b = None, c = None):
# 		if a != None and b != None and c != None:
# 			print("Sum of 3 arguments", a+b+c)
# 		elif a != None and b != None:
# 			print("sum of 2 arguments", a + b)
# 		else:
# 			print("Please provide 2 or 3 arguments")
# t = Test()
# t.m1(10, 20)
# t.m1(10, 20, 30)
# t.m1(5)

# class Test():
# 	def sum(self, *a):
# 		l = 0
# 		for x in a:
# 			l = l+x
# 		print("sum of l: ", l)
# t = Test()
# t.sum(10,20)
# t.sum(10,20,30)
# t.sum(5)

# class Test():
# 	def __init__(self):
# 		print("ther is no arguments")
# 	def __init__(self, a):
# 		print("ther is one arguments")
# 	def __init__(self, a, b):
# 		print("ther is two arguments")
# # t = Test()
# # t1 = Test(5)
# t2 = Test(5, 10)

# class Test():
# 	def __init__(self,a=None,b=None,c=None):
# 		print("constructor with 0|1|2|3 number of aguments")

# t = Test()
# t1 = Test(5)
# t2 = Test(5, 10)
# t3 = Test(5, 10, 15)


class Test():
	def __init__(self, *a):
		print("constructor with number of aguments")

t = Test()
t1 = Test(5)
t2 = Test(5, 10)
t3 = Test(5, 10, 15)
t4 = Test(10,20,3040,50,60)