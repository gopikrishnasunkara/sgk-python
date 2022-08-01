Python Inheritance:
python programming language is easy to learn and work on the procedural and object oriented programming approach. inheritance is one such concept in object oriented programming. code reusability being the forte of inheritance, it help in a lot of applications when we are working on python. Following are the concepts discussed in this article.

What is inheritance?
init funcation
Types of inheritance
  single inheritance
  multiple inheritance
  multilevel inheritance
  hierarchical inheritance
  hybrid inheritance
python super() Funcation
python method overriding

What is inheritance?
The method of inheritance the properties of parent class into the chaild class known as inheritance. It is an OOP concept. Following are the benefits of inheritance.
1. code reusability- we do not have to write the same code again and again, we can just inherit the properties we need in  a chaild class.
2. it represents a real world relationshop between parent class and chaild class.
3. It is transitive in nature. if a chaild class inherits properties from a parent class, then all other sub-classes of the child class will also inherit the properties of the parent class.

Example of inheritance in python.
class parent():
	def first(self):
		print("iam from the parent statement")
class child(parent):
	def second(self):
		print("iam from the child statement")
obj = child()
obj.second()
obj.first()
Output:
iam from the child statement
iam from the parent statement

in the above programme, you can access the parent class funcation with using chaild class object.

Waht is subclass:
calling a constructure of parent class by mentioning the parent class name in the declaration of the child class is known as sub-classing.The child class identified by parent class by sub-classing.

What is the init() function?
The __init__() Function called every time a class being used to make an object. when we add the __init__ function in the parent class, the child class will no longer be able to inherite the parent's class's __init__() function. The child class will override the parent class's __init__() function.

Example:
class Parent:
	def __init__(self , fname, fage):
		self.firstname = fname
		self.age = fage
		def view(self):
			print(self.firstname , self.age)

class Child(Parent):
	def __init__(self , fname , fage):
		Parent.__init__(self, fname, fage) # the line will override the parent class's init function.
		self.lastname = "edureka"
		self.adv = "it is easy to learn"
	def view(self):
		print("course name" , self.firstname ,"first came",  self.age , " years ago." , self.lastname, " has courses to master python", self.adv)
ob = Child("Python" , '28')
ob.view()

#Output: course name Python first came 28  years ago. edureka  has courses to master python.

Types of inheritance:
Depending upon the number of child and parent classes involved, there are four types of inheritance in python.

								Single
								multiple
				Types of inheritance ----->	multilevel
								Hierarchical

Single Inheritance():
When a child class inherits only a single parent class.

Example:
class Parent():
	def fun(self):
		print("iam from the parent class function")
class Child(Parent):
	def fun1(self):
		print("iam from the chaild class funcation")
obj = Child()
obj.fun()
obj.fun1()
Output:
iam from the parent class function
iam from the chaild class funcation

Multiple Inheritance
When a child class inherits from more than one parent class.

class Parent():
	def fun(self):
		print("iam from the parent class function")
class Parent1():
	def fun1(self):
		print("iam from the parent1 class funcation")
class Child(Parent1, Parent):
	def fun2(self):
		print("iam from the child class function")
obj = Child()
obj.fun2()
obj.fun()
obj.fun1()

Output:
iam from the child class function
iam from the parent class function
iam from the parent1 class funcation

C:\Users\ANIL\Desktop>python exception.py
iam from the child class function
iam from the parent class function
iam from the parent1 class funcation

Multilevel Inheritance
When a child class becomes a parent class for another child class.

class Parent():
	def fun(self):
		print("iam from the parent class function")
class Child(Parent):
	def fun1(self):
		print("iam from the parent1 class funcation")
class Child1(Child):
	def fun2(self):
		print("iam from the child class function")
obj = Child1()
obj.fun()
obj.fun1()
obj.fun2()
Output: 
C:\Users\ANIL\Desktop>python exception.py
iam from the child class function
iam from the parent class function
iam from the parent1 class funcation

C:\Users\ANIL\Desktop>python exception.py
iam from the parent class function
iam from the parent1 class funcation
iam from the child class function

Hierarchical Inheritance
Hierarchical inheritance involves multiple inheritance from the same base or parent class.

class Parent():
	def fun(self):
		print("iam from the parent class function")
class Child(Parent):
	def fun1(self):
		print("iam from the parent1 class funcation")
class Child1(Parent):
	def fun2(self):
		print("iam from the child class function")
obj = Child()
obj1 = Child1()
obj.fun()
obj.fun1()
obj1.fun2()
Output:
iam from the parent class function
iam from the parent1 class funcation
iam from the child class function

Hybrid Inheritance
Hybrid inheritance involves multiple inheritance taking place in a single program.

class Parent():
	def fun(self):
		print("iam from the parent class function")
class Child(Parent):
	def fun1(self):
		print("iam from the parent1 class funcation")
class Child1(Parent):
	def fun2(self):
		print("iam from the child class function")
class child3(Child,Child1):
	def fun3(self):
		print("iam from the child3 function")
obj = child3()
obj.fun()

Output:
C:\Users\ANIL\Desktop>python exception.py
iam from the parent class function

Python Super() Function
Super function allows us to call a method from the parent class.

class Parent():
	def fun(self):
		print("iam from the parent class function")
class Child(Parent):
	def fun1(self):
		super().fun()
		print("iam from the child class function")
obj = Child()
obj.fun1()

output:
iam from the parent class function
iam from the child class function
