#Creating a class in python.

'''class Student():
	class_name = 'A1'
	No_of_subjects = 6
	def __init__(self, name, age, s1, s2):
		self.name = name
		self.age = age
		self.s1 = s1
		self.s2 = s2
	def std_details(self):
		print("He is belonging to class section",self.class_name)
		print("he has to study",self.No_of_subjects, "a year")
		print("Name of the student is: ", self.name)
		print("He is", self.age, "years old")
		print("he got", self.s1, "marks in the s1 subject")
		print("He got", self.s2, "marks in the s2 subject")
		
s1 = Student("vissu", 27, 99,35)
s2 = Student("swamy", 27, 99,36)
s1.std_details()
print("")
s2.std_details()
print(" ")
Student.std_details(s1)
print(" ")
Student.std_details(s2)'''


#Types of variable in oops concept:

#In this section we have discussed about below points:
#1. Global variable
#2. Class variable
#3. Instance variable
#4. locat variable

'''school = "ABC"
mandatory = "Identity card and shoes"
class Student():
	imp1 = "Pen"
	imp2 = "Books"
	def __init__(self, name, age, section):
		self.name = name
		self.age = age
		self.section = section
	def Student_details(self):

		print("He is studing in :", school)
		print(mandatory + "is mandatory for every student")
		print("student needful things are :", self.imp1, self.imp2)
		print("student name is : ", self.name)
		print("student age is : ", self.age)
		print("student are belongs to : ", self.section)
	def Student_personals(self):
		school_fee = 50000
		van_fee = 10000
		print("He is studing in :", school)
		print(mandatory +  " is mandatory for every student")
		print("student needful things are :", self.imp1, self.imp2)
		print("student name is : ", self.name)
		print("student age is : ", self.age)
		print("student are belongs to : ", self.section)
		print("student school fee is : ", school_fee)
		print("student van fee is : ", van_fee)
s1 = Student("vissu", 27, "A")
s2 = Student("swami", 27, "B")
print("we are from the G-variable section")
print("Iam from the global variable section: ", school )
print("Iam from the global variable section: ", mandatory)
print(" ")
print("we are from the C-variable section")
print("Iam from the class variable section: ", s1.imp1 + " and", s1.imp2)
print("Iam from the class variable section: ", Student.imp1 + " and", Student.imp2)

print(" ")
print("we are from the I-variable section")
print("Iam from the Instance variable section: ", s1.name + " and", s1.age , " and", s1.section)
print(s1.name, s1.age, s1.section)
print("")
print("we are from the L-variable section")
#print(s1.school_fee)
print(s1.van_fee)'''



'''
s1.Student_details()
print(" ")
s2.Student_details()
print("")
print("-------------------------------------------------------")
print(" ")
s1.Student_personals()
print(" ")
s2.Student_personals()
'''


#Types of Methods in OOPS concept:
'''In this section, We are going to discuss about the below methods:
1. class method
2. Instance method
3. Static method'''


'''class Student():
	a = 1
	b = 2
	def __init__(self, firstval, secondval):
		self.c = firstval
		self.d = secondval
	def add(self):
		print(self.a + self.b + self.c + self.d)
		self.c = 50
		Student.a = 47
	#classmethod
	def substract(cls):
		print(cls.a -cls.b - s1.c - s1.d)
	@staticmethod
	def multiply(p,q):
		print((p*q) * (s1.c * s1.d * Student.a * Student.b))

s1 = Student(5,7)
#s1.add()
#Student.add(s1)
#s1.substract()
#Student.substract(s1)
#s1.multiply(5,7)
#Student.multiply(5,7)
'''

"""#Inheritance:
class Parent():
	def __init__(self, fname, fage):
		self.firstname = fname
		self.age = fage
	def view(self):
		print(self.firstname, self.age)
class Chaild(Parent):
	def __init__(self, fname, fage):
		Parent.__init__(self, fname, fage)
		self.lastname = "Edureka"
		self.adv = "It is easy to learn"
	def view(self):
		print("course name" , self.firstname ,"first came",  self.age , " years ago." , self.lastname, " has courses to master of python.", self.adv)
ob = Chaild("python", 28)
ob.view()"""

#Single Inheritance():
'''class Parent():
	def fun(self):
		print("iam from the parent class function")
class Child(Parent):
	def fun1(self):
		print("iam from the chaild class funcation")
obj = Child()
obj.fun()
obj.fun1()

#Multiple Inheritance():
class Parent():
	def fun(self):
		print("iam from the parent class function")
class Parent1():
	def fun1(self):
		print("iam from the parent1 class function")
class Chaild(Parent, Parent1):
	def fun2(self):
		print("iam from the chaild class funcation")
obj = Chaild()
obj.fun2()
obj.fun()
obj.fun1()'''

#Multilevel Inheritance():
'''class Parent():
	def fun(self):
		print("iam from the parent class function")
class Chaild(Parent):
	def fun1(self):
		print("Iam from the chaild class function")
class Chaild1(Chaild):
	def fun2(self):
		print("Iam from the chaild1 class function")
obj = Chaild1()
obj.fun()
obj.fun1()
obj.fun2()'''

#Hierarchical Inheritance
'''class Parent():
	def fun(self):
		print("iam from the parent class function")
class Chaild(Parent):
	def fun1(self):
		print("I am from the chaild class function")
class Chaild1(Parent):
	def fun2(self):
		print("I am from the chaild1 class function")
obj = Chaild()
obj1 = Chaild1()
obj.fun()
obj.fun1()
obj1.fun()
obj1.fun2()'''

#Hybrid Inheritance
'''class Parent():
	def fun(self):
		print("iam from the parent class function")
class Child(Parent):
	def fun1(self):
		print("iam from the chaild class funcation")
class Child1(Parent):
	def fun2(self):
		print("iam from the chaild1 class function")
class Chaild3(Child,Child1):
	def fun3(self):
		print("iam from the chaild3 function")

obj = Chaild3()
obj.fun3()
obj.fun2()
obj.fun1()
obj.fun()'''

#Super()
class Parent():
	def fun(self):
		print("iam from the parent class funcation")
class Chaild(Parent):
	def fun1(self):
		super().fun()
		print("iam from the chaild class funcation")
obj = Chaild()
obj.fun1()
















