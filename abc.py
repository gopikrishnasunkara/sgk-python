wheels = 4						#wheels and steeing are two are global variables
steering = "power steering"
class car():
	sitting = 5					#sitting and doors are class variables
	doors = 5
	def __init__ (self, color, engtype):		#constructor is created with two arguments
		self.colour = color			#self.colour and self.engtypes are two instance variables
		self.engtype = engtype
	def suzuki(self):
		mil = "8KMS"				# mil is the local variable
		print(self.colour, self.engtype)	#printing the instance variable inside of the suzuki method with using instance(self)(i.e, object)
		print(self.sitting, self.doors)		#printing the class variable inside of the suzuki method with using instance(i.e, object) or using the class name, it was not a good practice.
		print(wheels, steering)			#printing the global variable inside the suzuki methods, we no need to mentioned any instance name or class name, we call directly
		print(mil)				#printing the local variable mil inside of the suzuki method
	def honda(self): 
		mil = "5kms"				# mil is the local variable
		print(self.colour, self.engtype)	#printing the instance variable inside of the honda method with using instance(i.e, object)
		print(self.sitting, self.doors)		#printing the class variable inside of the Honda method with using instance(i.e, object) or using the class name, it was not a good practice.
		print(wheels, steering)			#printing the global variable inside the honda methods, we no need to mentioned any instance name or class name, we call directly
		print(mil)				#printing the local variable mil inside of the honda method
	def hundai(self):
		print(mil)				#gives an error like, mil is not defined, local variable we can use within the method where we defined
abc  = car("white", "diesel")				#creation an object of the class with values white and diesel.
abc.suzuki()						#calling an suzuki method
abc.honda()						#calling an honda method
#abc.hundai()						#calling an hundai method
print(wheels, steering)					#global variable we can call directly, we no need to class name or instance name
print(abc.colour, abc.engtype)				#class variable we can call with either class name or instance object name
print(car.sitting, car.doors)				#class variable we can call with either class name or instance object name
#print(mil)						#it gives us an error, bcz local variable we cannot call out side of the class or method
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
school = "abc"
mandatory = "identity card"
class student():
	imp1 = "pen"
	imp2 = "books"
	def __init__ (self, name, age, section):
		self.name = name
		self.age  = age
		self.section = section
	def details(self):
		mandate = "shoes"
		print("He is studing in", school, "school")
		print("student should properly wear", mandatory)
		print("student must have", self.imp1)
		print("student must have ", self.imp2)
		print("student should come with", mandate)
	def information(self):
		print(mandate)
s1 = student("vissu", 25, "A")
s1.details()
s1.information()
print(school, mandatory)
print(s1.name, s1.age, s1.section)
print(mandate)