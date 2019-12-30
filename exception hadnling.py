Exception handling:
Mainly we have to discuss about two things, 
1. Error
2. exceptions

1.Error: The error is an action which is inaccurate or incorrect funcationlity and errors cann't be handled at runtime.
2. Exceptions: The exceptions are process of handling the error means that, we have write some code which is correct, but still system saying that it error. but error can be handled at runtime.
we have following keyword which is very oftenly used in the exception handling function.
1.try
2.except
3.Except(superclass)
4. finally(it will executed always even with exceptio or without exception)

example: for error.
class excepdemo():
	def __init__(self, a, b):
		self.x = a
		self.y = b
	def addit(self):
		return self.x + self.y + self.z
obj = excepdemo(5, 7)
print(obj.addit())

Output:
C:\Users\ANIL\Desktop>python exception.py
Traceback (most recent call last):
  File "exception.py", line 8, in <module>
    print(obj.addit())
  File "exception.py", line 6, in addit
    return self.x + self.y + self.z
AttributeError: 'excepdemo' object has no attribute 'z'

exceptions:
class fileread():
	def __init__(self, path):
		self.path = path
	def readfile(self):
		f = open(self.path, 'r')
		data = f.read()
		return data
obj = fileread(r'C:\Users\ANIL\Desktop\exception1.py')
print(obj.readfile())

Output:
class fileread():
        def __init__(self, path):
                self.path = path
        def readfile(self):
                f = open(self.path, 'r')
                data = f.read()
                return data
obj = fileread(r'C:\Users\ANIL\Desktop\exception.py')
print(obj.readfile())

programme2:Giving an incorrect file path location while calling the function.
class fileread():
	def __init__(self, path):
		self.path = path
	def readfile(self):
		f = open(self.path, 'r')
		data = f.read()
		return data
obj = fileread(r'C:\Users\ANIL\Desktop\exception1.py')
print(obj.readfile())

Output:
Traceback (most recent call last):
  File "exception.py", line 9, in <module>
    print(obj.readfile())
  File "exception.py", line 5, in readfile
    f = open(self.path, 'r')
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\ANIL\\Desktop\\exception1.py'

programme3:
class fileread():
	def __init__(self, path):
		self.path = path
	def readfile(self):
		try:
			f = open(self.path, 'r')

			data = f.read()
		except (FileNotFoundError):
			print("file is not available")
		finally:
			print("closing the file")
			f.close()
		return data

obj = fileread(r'C:\Users\ANIL\Desktop\exception1.py')
obj.readfile()

output:
file is not available
closing the file
Traceback (most recent call last):
  File "exception.py", line 17, in <module>
    obj.readfile()
  File "exception.py", line 13, in readfile
    f.close()
UnboundLocalError: local variable 'f' referenced before assignment

Programme4:
here we have used Exception before the exptions, so Exception would print first then exception. so  exception would be super class. always priority is first Exceptions.
class fileread():
	def __init__(self, path):
		self.path = path
	def readfile(self):
		try:
			f = open(self.path, 'r')

			data = f.read()
		except(Exception):
			print("something wrong")

		except (FileNotFoundError):
			print("file is not available")
		finally:
			print("closing the file")
			f.close()
		return data

obj = fileread(r'C:\Users\ANIL\Desktop\exception1.py')
obj.readfile()

Output:
something wrong
closing the file
Traceback (most recent call last):
  File "exception.py", line 20, in <module>
    obj.readfile()
  File "exception.py", line 16, in readfile
    f.close()
UnboundLocalError: local variable 'f' referenced before assignment
 Programme4:
class fileread():
	def __init__(self, path):
		self.path = path
	def readfile(self):
		try:
			f = open(self.path, 'r')

			data = f.read()
		except (FileNotFoundError):
			print("file is not available")

		except(Exception):
			print("something wrong")

		finally:
			print("closing the file")
			f.close()
		return data

obj = fileread(r'C:\Users\ANIL\Desktop\exception1.py')
obj.readfile()
 Output:
file is not available
closing the file
Traceback (most recent call last):
  File "exception.py", line 21, in <module>
    obj.readfile()
  File "exception.py", line 17, in readfile
    f.close()
UnboundLocalError: local variable 'f' referenced before assignment

Programme5:
class sub():
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def div(self):
		try:
			res = self.x/self.y
			
		except (FileNotFoundError):
			print("file is not available")

		except(Exception):
			print("something wrong")

		finally:
			print("closing the programme")
			f.close()
		return res

obj = sub(5, 0)
obj.div()
output:
something wrong
closing the programme
Traceback (most recent call last):
  File "exception.py", line 21, in <module>
    obj.div()
  File "exception.py", line 17, in div
    f.close()
NameError: name 'f' is not defined

Programme6:
class sub():
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def div(self):
		try:
			res = self.x/self.y
			
		except (ZeroDivisionError):
			print("please enter the second value > 0")

		except(Exception):
			print("something wrong")

		finally:
			print("closing the programme")
			f.close()
		return res

obj = sub(5, 0)
obj.div()
Output:
file is not available
closing the programme
Traceback (most recent call last):
  File "exception.py", line 21, in <module>
    obj.div()
  File "exception.py", line 17, in div
    f.close()
NameError: name 'f' is not defined
programme7:
class sub():
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def div(self):
		try:
			res = self.x/self.y
			
		except (ZeroDivisionError):
			print("please enter the second value > 0")

		except(Exception):
			print("something wrong")

		finally:
			print("closing the programme")
			f.close()
		return res

obj = sub(5, 0)
obj.div()
Output:
please enter the second value > 0
closing the programme
Traceback (most recent call last):
  File "exception.py", line 21, in <module>
    obj.div()
  File "exception.py", line 17, in div
    f.close()
NameError: name 'f' is not defined

