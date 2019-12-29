Programme1: printing the normal commands in the python.

print("My First Name is : ABC")
print("My Middle Name is : DEF")
print("My Last Name is : GHI")

output:
My First Name is : ABC
My Middle Name is : DEF
My Last Name is : GHI

Programme2: creating an variables in  the python.
firstname = "ABC"
middlename = "DEF"
lastname = "GHI"
age = 45
experience = 22.5

print(firstname)
print(middlename)
print(lastname)
print(age)
print(experience)

output:
ABC
DEF
GHI
45
22.5

Programme3: printing 3 string variables in the same line.

firstname = "ABC"
middlename = "DEF"
lastname = "GHI"
age = 45
experience = 22.5

print(firstname, middlename, lastname)
print(age)
print(experience)

Output:
ABC DEF GHI
45
22.5




Programme4: Creating an variable in the python  and include them in the print statement.

import os
os.system("clear")

firstname = "ABC"
middlename = "DEF"
lastname = "GHI"
age = 45
experience = 22.5

print("Your First Name : ", firstname)
print("Your Middle Name : ", middlename)
print("Your Last Name : ", lastname)
print("Your Given Age is : ", age)
print("Your Experience As Given is : ", experience)

Output:

'clear' is not recognized as an internal or external command,
operable program or batch file.
Your First Name :  ABC
Your Middle Name :  DEF
Your Last Name :  GHI
Your Given Age is :  45
Your Experience As Given is :  22.5

Programme5:printing the all statemtents are invidual as well including all

import os
os.system("clear")

#My Declarations Begin Here

firstname = "ABC"
middlename = "DEF"
lastname = "GHI"
age = 45
experience = 22.5

#End of Declarations

#Operational Logic Begins Here

print("Your First Name : ", firstname)
print("Your Middle Name : ", middlename)
print("Your Last Name : ", lastname)
print("Your Full Name is : ", firstname, middlename, lastname)
print("Your Given Age is : ", age, ", And Your Experience is : ", experience)

#Operational Logic Ends Here


Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
Your First Name :  ABC
Your Middle Name :  DEF
Your Last Name :  GHI
Your Full Name is :  ABC DEF GHI
Your Given Age is :  45 , And Your Experience is :  22.5

Programme6: Printing the numeric values in the python

a = 30	
#b = 75382041L 				long integer are not there in the python3
c = 35.45
d = 5.75j

print("The Given Integer Value : ", a)
#print("The Given Long Value : ", b)
print("The Given Float Value : ", c)
print("The Given Complex Value : ", d)

Output:

The Given Integer Value :  30
The Given Float Value :  35.45
The Given Complex Value :  5.75j

Programme7: Working on the string functions

mystring = 'Python Savvy'
print('Printing The Total String')
print(mystring)
print('Printing Data From Specific Index')
print(mystring[0])
print('Printing Data From Specific Index To A Specific Index')
print(mystring[4:5])
print('Printing Data From Specific Index Till Last')
print(mystring[8:])
print('Printing Data Multiple Times')
print(mystring * 2)
print('Printing Data With Concatenated String')
print(mystring + ", With Thirst")

Output:

Printing The Total String
Python Savvy
Printing Data From Specific Index
P
Printing Data From Specific Index To A Specific Index
o
Printing Data From Specific Index Till Last
avvy
Printing Data Multiple Times
Python SavvyPython Savvy
Printing Data With Concatenated String
Python Savvy, With Thirst

Programme8: working on the string indexing function in python

fruits = [ 'Apple', 'Banana', 'Mango', 'Litchi', 'Papaya' ]

print(fruits)
print(fruits[0])
print(fruits[1:3])    
print(fruits[3:])

Output:

['Apple', 'Banana', 'Mango', 'Litchi', 'Papaya']
Apple
['Banana', 'Mango']
['Litchi', 'Papaya']

Progamme9:

import os
os.system("clear")
mixedlist = [ 'ABC', 'DEF', 'GHI', 45, 22.5 ]
print("Your First Name is : ", mixedlist[0])
print("Your Middle Name is : ", mixedlist[1])       
print("Your Last Name is : ", mixedlist[2]) 
print("Mr.", mixedlist[0], mixedlist[1], mixedlist[2], "Your Age is : ", mixedlist[3], "Years And Proffessional Experience is : ", mixedlist[4])

Output:

'clear' is not recognized as an internal or external command,
operable program or batch file.
Your First Name is :  ABC
Your Middle Name is :  DEF
Your Last Name is :  GHI
Mr. ABC DEF GHI Your Age is :  45 Years And Proffessional Experience is :  22.5

Programme 10: Working on the dictonary's in python.

mydictionary = {'FirstName': 'ABC', 'MiddleName': 'DEF', 'LastName': 'GHI', 'Age': 45, 'Experience': 22}
print("First Name : ", mydictionary['FirstName'])
print("Middle Name : ", mydictionary['MiddleName'])
print("Last Name : ", mydictionary['LastName'])
print("Mr.", mydictionary['FirstName'], mydictionary['MiddleName'], mydictionary['LastName'], "Your Age is : ", mydictionary['Age'], "Years And Proffessional Experience is : ", mydictionary['Experience'])

Output:

First Name :  ABC
Middle Name :  DEF
Last Name :  GHI
Mr. ABC DEF GHI Your Age is :  45 Years And Proffessional Experience is :  22

Programme 11: Adding the two variables

var01 = 5
var02 = 2
result = var01 + var02
print("The Sum of ", v1, " and  ", v2, " is : ", result)

output:

The Sum of  5  and   2  is :  7

Programme12: Adding the two variables with user inputs in python

var01 = input("Please Enter The First Value : ")
var02 = input("Please Enter The Second Value : ")
result = int(var01) + int(var02)
print("The Sum of ", var01, " and  ", var02, " is : ", result)
#waitforainput = raw_input("Please Press Any Key To Terminate...") raw input function has been removed from the python3

Output:

Please Enter The First Value : 5
Please Enter The Second Value : 7
The Sum of  5  and   7  is :  12

Programme13: Substracting the two variables with user inputs in python

var01 = input("Please Enter The First Value : ")
var02 = input("Please Enter The Second Value : ")
result = 0
result = int(var01) - int(var02)
print("The Difference of ", var01, " and  ", var02, " is : ", result)
#waitforinput = raw_input("Please Press Any Key To Terminate...")

output:
Please Enter The First Value : 5
Please Enter The Second Value : 7
The Sum of  5  and   7  is :  -2

Programme14: adding the two number with assignment operator

var01 = input("Please Enter Any Numeric Value : ")
result = 10
result += int(var01)
print("The Final Result is : ", result)
waitforinput = input("Please Press Any Key To Terminate...")

Output:
Please Enter Any Numeric Value : 5
The Final Result is :  15
Please Press Any Key To Terminate...k

C:\Users\Nemmadi Gopi\Desktop>

Programme15: substracting the two number with assignment operator

var01 = input("Please Enter Any Numeric Value : ")
result = 10
result -= int(var01)
print("The Final Result is : ", result)
waitforinput = input("Please Press Any Key To Terminate...")

Output:
Please Enter Any Numeric Value : 5
The Final Result is :  5
Please Press Any Key To Terminate...ll

C:\Users\Nemmadi Gopi\Desktop>

Programme16: printing the string values in python

var01 = input("Enter any Integer Value : ")#if i have given int infrone ofthe input, it should take only numeric values, not string
if var01:
	print("The Variable Has A Value, We Are Working in TRUE State")
	print("The Value is : ", var01)
	print(type(var01))

output:

Enter any Integer Value : 5
The Variable Has A Value, We Are Working in TRUE State
The Value is :  5
<class 'String'>

Programme17: Printing the int values in python

var01 = int(input("Enter any Integer Value : ")) #if i have given int infrone ofthe input, it should take only numeric values, not string
if var01:
	print("The Variable Has A Value, We Are Working in TRUE State")
	print("The Value is : ", var01)
	print(type(var01))
Output:

Enter any Integer Value : 5
The Variable Has A Value, We Are Working in TRUE State
The Value is :  5
<class 'String'>

Programme18
var01 = 25
if var01:
	print("The Variable Has A Value, We Are Working in TRUE State")
	print("The Value is : ", var01)
print("This is Main Part of The Execution After if Has Terminated")
output:
The Variable Has A Value, We Are Working in TRUE State
The Value is :  25
This is Main Part of The Execution After if Has Terminated

Programme19:

var01 = 0

if var01:
	print("The Variable Has A Value, We Are Working in TRUE State")
	print("The Value is : ", var01)
print("This is Main Part of The Execution After if Has Terminated")
output: if the values is zero or null values are fale, programme should not be executed.

Programme20: declaring the valrible and priting the statements with using if condition.

var01 = 0 
if var01:
	print("The Variable Has A Value, We Are Working in TRUE State")
	print("The Value is : ", var01)
output: if the values is zero or null values are fale, programme should not be executed.

Programme21: Getting the values from the user and printing the value.

var01 = input("Enter any Integer Value : ")
if var01:
   print("The Variable Has A Value, We Are Working in TRUE State")
   print("The Value is : ", var01)

Output:
Enter any Integer Value : k
The Variable Has A Value, We Are Working in TRUE State
The Value is :  k

Enter any Integer Value : 5
The Variable Has A Value, We Are Working in TRUE State
The Value is :  5

Enter any Integer Value : 0
The Variable Has A Value, We Are Working in TRUE State
The Value is :  0

Programme22:

var01 = int(input("Enter any Integer Value : "))
if var01:
	print("The Variable Has A Value, We Are Working in TRUE State")
	print("The Value is : ", var01)
output: if the values is zero or null values are fale, programme should not be executed.
Output: if the values are non-zero or non - null values are true and programme will executed.
Enter any Integer Value : k
Traceback (most recent call last):
  File "com.py", line 1, in <module>
    var01 = int(input("Enter any Integer Value : "))
ValueError: invalid literal for int() with base 10: 'k'

Enter any Integer Value : 5
The Variable Has A Value, We Are Working in TRUE State
The Value is :  5

Enter any Integer Value : 0

Programme23:

var01 = int(input("Enter any Integer Value : "))
if var01:
	print("The Variable Has A Value, We Are Working in TRUE State")
	print("The Value is : ", var01)
print("I Am Outof The if Construct")

Output:
Enter any Integer Value : 5
The Variable Has A Value, We Are Working in TRUE State
The Value is :  5
I Am Outof The if Construct

Programme24:

var03 = int(input("Enter any Integer Value : "))
if ( var03  == 30 ): print("The Condition Evaluated To TRUE, We Are Working in TRUE State")
print("My Job is Done...Leaving To The Prompt...")
Output:
Enter any Integer Value : 5
My Job is Done...Leaving To The Prompt...

Enter any Integer Value : 30
The Condition Evaluated To TRUE, We Are Working in TRUE State
My Job is Done...Leaving To The Prompt...

Programme25:

var01 = 0
if var01:
	print("The Variable Has A Value, We Are Working in TRUE State")
	print("The Value is : ", var01)
else:
	print("The Variable Has No Value, We Are Working in FALSE State")
	print("The Value is : ", var01)
Output:
The Variable Has No Value, We Are Working in FALSE State
The Value is :  0

Programme26:

var01 = int(input("Enter any Integer Value : "))
if (var01 > 10):
	print("The Given Value is Greater Than 10")
	print("The Given Value is : ", var01)
else:
	print("The Given Value is Less Than 10")
	print("The Given Value is : ", var01)

Output:
Enter any Integer Value : 5
The Given Value is Less Than 10
The Given Value is :  5

C:\Users\Nemmadi Gopi\Desktop>python com.py
Enter any Integer Value : 11
The Given Value is Greater Than 10
The Given Value is :  11

Programme27

var01 = int(input("Enter any Integer Value : "))
result = var01 % 2
if (result == 0):
	print("The Given Number is an Even Number")
	print("The Given Value is : ", var01)
else:
	print("The Given Number is an Odd Number")
	print("The Given Value is : ", var01)

output:
C:\Users\Nemmadi Gopi\Desktop>python com.py
Enter any Integer Value : 5
The Given Number is an Odd Number
The Given Value is :  5

C:\Users\Nemmadi Gopi\Desktop>python com.py
Enter any Integer Value : 10
The Given Number is an Even Number
The Given Value is :  10

Programme28:

var01 = int(input("Enter any Integer Value : "))
if (var01 % 2 == 0):
	print("The Given Number is an Even Number")
	print("The Given Value is : ", var01)
else:
	print("The Given Number is an Odd Number")
	print("The Given Value is : ", var01)
Output:
C:\Users\Nemmadi Gopi\Desktop>python com.py
Enter any Integer Value : 5
The Given Number is an Odd Number
The Given Value is :  5

C:\Users\Nemmadi Gopi\Desktop>python com.py
Enter any Integer Value : 10
The Given Number is an Even Number
The Given Value is :  10

Programme29:

var02 = 50
if(var02 == 20):
	print("Evaluated To TRUE State")
	print("The Value is : ", var02)
elif(var02 == 30):
	print("Evaluated To TRUE State")
	print("The Value is : ", var02)
elif(var02 == 40):
	print("Evaluated To TRUE State")
	print("The Value is : ", var02)
elif(var02 == 50):
	print("Evaluated To TRUE State")
	print("The Value is : ", var02)
else:
	print("None of The Values Were Matching, Hence Terminating")
	print("The Value is : ", var02)
output:
Evaluated To TRUE State
The Value is :  50

Programme30:

import os
os.system("clear")
var02 = int(input("Please Enter Any Number of Your Choice : "))
if(var02 == 20):
	print("Evaluated To TRUE State")
	print("The Value is : ", var02)
elif(var02 == 30):
	print("Evaluated To TRUE State")
	print("The Value is : ", var02)
elif(var02 == 40):
	print("Evaluated To TRUE State")
	print("The Value is : ", var02)
elif(var02 == 50):
	print("Evaluated To TRUE State")
	print("The Value is : ", var02)
else:
	print("None of The Values Were Matching, Hence Terminating")
	print("The Value is : ", var02)
waitforinput = input("Please Press Any Key To Terminate...")

Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
Please Enter Any Number of Your Choice : 35
None of The Values Were Matching, Hence Terminating
The Value is :  35

C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
Please Enter Any Number of Your Choice : 50
Evaluated To TRUE State
The Value is :  50

Programme31
import os
os.system("clear")
var01 = int(input("Enter First Integer Value : "))
var02 = int(input("Enter Second Integer Value : "))
if (var01 < var02):
	print("First Value is Less Than The Second Value")
	print("First Value :", var01, "Second Value :", var02)
elif (var01 > var02):
	print("First Value is Greater Than The Second Value")
	print("First Value :", var01, "Second Value :", var02)
elif (var01 == var02):
	print("First Value is Equal To The Second Value")
	print("First Value :", var01, "Second Value :", var02)
else:
	print("Sorry Unable To Analyze!")
waitforinput = input("Please Press Any Key To Terminate...")

Output: C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
Please Enter Any Number of Your Choice : 50
Evaluated To TRUE State
The Value is :  50
Please Press Any Key To Terminate...5

C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
Enter First Integer Value : 50
Enter Second Integer Value : 20
First Value is Greater Than The Second Value
First Value : 50 Second Value : 20
Please Press Any Key To Terminate...k

C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
Enter First Integer Value : 50
Enter Second Integer Value : 50
First Value is Equal To The Second Value
First Value : 50 Second Value : 50
Please Press Any Key To Terminate...50


C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
Enter First Integer Value : 20
Enter Second Integer Value : 50
First Value is Less Than The Second Value
First Value : 20 Second Value : 50
Please Press Any Key To Terminate...l

Programme32:

import os
os.system("clear")

givenmarks = int(input("Please Enter Your Marks : "))

if(givenmarks >= 90):
	print("Excellent You Achieved Grade A")
elif(givenmarks >=80):
	print("Congratulations You Achieved Grade B")
elif(givenmarks >=70):
	print("It is OK You Achieved Grade C")
elif(givenmarks >= 65):
	print("You Achieved Grade D")
else:
	print("Sorry! You Failed in This Semester")
waitforinput = input("Please Press Any Key To Terminate...")

Output:
C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
Please Enter Your Marks : 95
Excellent You Achieved Grade A
Please Press Any Key To Terminate...k

C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
Please Enter Your Marks : 35
Sorry! You Failed in This Semester
Please Press Any Key To Terminate...

Programme33:
import os
os.system("clear")
givenyear = int(input("Please Enter Any Year in 4 Digits : "))
if (givenyear % 4) == 0:
	if (givenyear % 100) == 0:
		if (givenyear % 400) == 0:
			print(givenyear, " is A Leap Year")
		else:
			print(givenyear, " is Not A Leap Year")
	else:
		print(givenyear, " is A Leap Year")
else:
	print(givenyear, "is Not A Leap Year")

Output:
C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
Please Enter Any Year in 4 Digits : 2019
2019 is Not A Leap Year

C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
Please Enter Any Year in 4 Digits : 2014
2014 is Not A Leap Year

C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
Please Enter Any Year in 4 Digits : 2012
2012  is A Leap Year

Programme34:
import os
os.system("clear")

totalsales = int(input("Please Enter The Sales Value : "))
givecountry = input("Please Enter The Country Name in ISO Standard : ")

if givecountry == "IN":
	if totalsales <= 50:
		print("The Total Shipping Cost is  : 50INR")
	elif totalsales <= 100:
		print("The Total Shipping Cost is : 25INR")
	elif totalsales <= 150:
		print("The Total Shipping Cost is : 5INR")
	else:
		print("The Shipping is Done FREE of Cost")
if givecountry == "US":
	if totalsales <= 50:
		print("The Shipping Cost is :  100USD")
	else:
		print("The Shipping is Done FREE of Cost")
Output:
C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
Please Enter The Sales Value : 100
Please Enter The Country Name in ISO Standard : US
The Shipping is Done FREE of Cost

C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
Please Enter The Sales Value : 150
Please Enter The Country Name in ISO Standard : IN
The Total Shipping Cost is : 5INR

Programme35
import os
os.system("clear")

print("Program To Print a Sequence of Numbers")
loopcounter = 1
while (loopcounter <= 10):
	print("The Line Number is : ", loopcounter)
	loopcounter = loopcounter + 1
output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
Program To Print a Sequence of Numbers
The Line Number is :  1
The Line Number is :  2
The Line Number is :  3
The Line Number is :  4
The Line Number is :  5
The Line Number is :  6
The Line Number is :  7
The Line Number is :  8
The Line Number is :  9
The Line Number is :  10


Programme36
import os
os.system("clear")

print("Program To Print a Sequence of Numbers")
loopcounter = 1
while (loopcounter <= 10):
	print("The Line Number is : ", loopcounter)
	loopcounter = loopcounter + 1

print("We Are Out of The Loop")
print("Operating in The Main Block of The Program")
output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
Program To Print a Sequence of Numbers
The Line Number is :  1
The Line Number is :  2
The Line Number is :  3
The Line Number is :  4
The Line Number is :  5
The Line Number is :  6
The Line Number is :  7
The Line Number is :  8
The Line Number is :  9
The Line Number is :  10
We Are Out of The Loop
Operating in The Main Block of The Program


Programme37
import os
os.system("clear")

print("Program To Print a Sequence of Numbers")
endpoint = int(input("Please Enter The Termination Point : "))
loopcounter = 1
while (loopcounter <= endpoint):
	print("The Line Number is : ", loopcounter)
	loopcounter = loopcounter + 1
Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
Program To Print a Sequence of Numbers
Please Enter The Termination Point : 5
The Line Number is :  1
The Line Number is :  2
The Line Number is :  3
The Line Number is :  4
The Line Number is :  5

Programme38
import os
os.system("clear")

print("Program To Print a Sequence of Numbers")
startpoint = int(input("Please Enter The Starting Point : "))
while (startpoint <= 10):
	print("The Line Number is : ", startpoint)
	startpoint = startpoint + 1
output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
Program To Print a Sequence of Numbers
Please Enter The Starting Point : 2
The Line Number is :  2
The Line Number is :  3
The Line Number is :  4
The Line Number is :  5
The Line Number is :  6
The Line Number is :  7
The Line Number is :  8
The Line Number is :  9
The Line Number is :  10

Programme39
import os
os.system("clear")

print("Program To Print a Sequence of Numbers")
startpoint = int(input("Please Enter The Starting Point : "))
if (startpoint <= 0 or startpoint > 10):
	print("Sorry! Index is Out of The Boundary...Cannot Proceed")
else:
	while(startpoint <= 10):
		print("The Line Number is : ", startpoint)
		startpoint = startpoint + 1

Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
Program To Print a Sequence of Numbers
Please Enter The Starting Point : 15
Sorry! Index is Out of The Boundary...Cannot Proceed

C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
Program To Print a Sequence of Numbers
Please Enter The Starting Point : 9
The Line Number is :  9
The Line Number is :  10

C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
Program To Print a Sequence of Numbers
Please Enter The Starting Point : 0
Sorry! Index is Out of The Boundary...Cannot Proceed

Programme40
import os
os.system("clear")

print("Program To Print a Sequence of Numbers")
startpoint = int(input("Please Enter The Starting Point : "))
endpoint = int(input("Please Enter The Ending Point : "))
if (startpoint <= 0 or endpoint > 10):
	print("Sorry! Index is Out of The Boundary...Cannot Proceed")
else:
	while (startpoint <= endpoint):
		print("The Line Number is : ", startpoint)
		startpoint = startpoint + 1
Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
Program To Print a Sequence of Numbers
Please Enter The Starting Point : 0
Please Enter The Ending Point : 9
Sorry! Index is Out of The Boundary...Cannot Proceed

C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
Program To Print a Sequence of Numbers
Please Enter The Starting Point : 0
Please Enter The Ending Point : 8
Sorry! Index is Out of The Boundary...Cannot Proceed

C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
Program To Print a Sequence of Numbers
Please Enter The Starting Point : 1
Please Enter The Ending Point : 5
The Line Number is :  1
The Line Number is :  2
The Line Number is :  3
The Line Number is :  4
The Line Number is :  5

Programme41
import os
os.system("clear")
print("Program To Add Natural Numbers...")
datainput = int(input("Please Enter The Number of Values : "))
finalsum = 0
loopindex = 1
while(loopindex <= datainput):
    finalsum = finalsum + loopindex
    loopindex = loopindex + 1

print("The Sum of ", datainput, " Natural Numbers is : ", finalsum)

Output:
C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
Program To Add Natural Numbers...
Please Enter The Number of Values : 5
The Sum of  5  Natural Numbers is :  15

C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
Program To Add Natural Numbers...
Please Enter The Number of Values : 1
The Sum of  1  Natural Numbers is :  1

Programme42
import os
os.system("clear")
print("Program To Add Natural Numbers...")
datainput = int(input("Please Enter The Number of Values : "))
finalsum = 0
loopindex = 1
while(loopindex <= datainput):
    finalsum = finalsum + loopindex
    print("The Current Sum is : ", finalsum)
    loopindex = loopindex + 1

print("The Sum of ", datainput, " Natural Numbers is : ", finalsum)
Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
Program To Add Natural Numbers...
Please Enter The Number of Values : 5
The Current Sum is :  1
The Current Sum is :  3
The Current Sum is :  6
The Current Sum is :  10
The Current Sum is :  15
The Sum of  5  Natural Numbers is :  15

Programme43
import os
os.system("clear")
loopcounter = 0
while loopcounter < 3:
    print("Curently Working Inside The Loop", loopcounter)
    loopcounter = loopcounter + 1
else:
    print("Now Working in The \"else\" Part of The Loop 01")

print("Now Working Totally Outside The Loop Control 01")
print("Now Working Totally Outside The Loop Control 02")
Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
Curently Working Inside The Loop 0
Curently Working Inside The Loop 1
Curently Working Inside The Loop 2
Now Working in The "else" Part of The Loop 01
Now Working Totally Outside The Loop Control 01
Now Working Totally Outside The Loop Control 02

Programme44
import os
os.system("clear")
mypassword = ""
while(mypassword != "Personal"):
	mypassword = input("Please Enter Your Password : ")
	if(mypassword == "Personal"):
		print("Congratulations Your Password Matches, You Are Privileged To Enter")
	else:
		print("Sorry! Your Password Doesnot Matches, We Cannot Allow You")

Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
Please Enter Your Password : personal
Sorry! Your Password Doesnot Matches, We Cannot Allow You
Please Enter Your Password : "Personal"
Sorry! Your Password Doesnot Matches, We Cannot Allow You
Please Enter Your Password : "Personal"
Sorry! Your Password Doesnot Matches, We Cannot Allow You
Please Enter Your Password : Personal
Congratulations Your Password Matches, You Are Privileged To Enter

Programme45
import os
os.system("clear")
invalidvalue = True
while(invalidvalue):
	inputvalue = int(input("Please Input a Number Within 10 And 20 : "))
	if(inputvalue >= 10 and inputvalue <= 20):
		invalidvalue = False
	else:
		print("Sorry! Number Should Be in Between 10 And 20 Only")
		print("Please Re-Enter The Value...")
print("Finally You Entered The Correct Value...")
print("Terminating The Process As Valid Input is Found...")

Output:

'clear' is not recognized as an internal or external command,
operable program or batch file.
Please Input a Number Within 10 And 20 : 15
Finally You Entered The Correct Value...
Terminating The Process As Valid Input is Found...

C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
Please Input a Number Within 10 And 20 : 10
Finally You Entered The Correct Value...
Terminating The Process As Valid Input is Found...

C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
Please Input a Number Within 10 And 20 : 15
Finally You Entered The Correct Value...
Terminating The Process As Valid Input is Found...

C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
Please Input a Number Within 10 And 20 : 30
Sorry! Number Should Be in Between 10 And 20 Only
Please Re-Enter The Value...
Please Input a Number Within 10 And 20 : 35
Sorry! Number Should Be in Between 10 And 20 Only
Please Re-Enter The Value...
Please Input a Number Within 10 And 20 :

Programme46
import os
os.system("clear")
import random
samplevalue = 20
valueguessed = int(samplevalue * random.random()) + 1
yourguess = 0
while yourguess != valueguessed:
	yourguess = int(input("Please Enter Your Guessed Number : "))
	if yourguess > 0:
		print(valueguessed)
		if yourguess > valueguessed:
			print("The Guessed Number Too Big")
		elif yourguess < valueguessed:
			print("The Guessed Number is Too Small")
	else:
		print("Sorry! You Decided To Leave The Game...")
		break
else:
    print("That's The Spirit, Finally You Guessed Correctly")

output:

'clear' is not recognized as an internal or external command,
operable program or batch file.
Please Enter Your Guessed Number : 8
4
The Guessed Number Too Big
Please Enter Your Guessed Number : 4
4
That's The Spirit, Finally You Guessed Correctly

C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
Please Enter Your Guessed Number : 5
15
The Guessed Number is Too Small
Please Enter Your Guessed Number : 15
15
That's The Spirit, Finally You Guessed Correctly

Programme47
import os
os.system("clear")
for loopindex in 'ABC':     
   print('The Character in Index is : ', loopindex)
Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Character in Index is :  A
The Character in Index is :  B
The Character in Index is :  C

Programme48
import os
os.system("clear")
mystring = input("Please Enter Any String : ")
for loopindex in mystring:     
   print('The Character in Index is : ', loopindex)
Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
Please Enter Any String : hello
The Character in Index is :  h
The Character in Index is :  e
The Character in Index is :  l
The Character in Index is :  l
The Character in Index is :  o

Programme49
import os
os.system("clear")

favsports = ['Cricket', 'Foot Ball',  'Shuttle', 'Table Tennis', 'Volley Ball']
for sportsindex in favsports: 
   print('The Identified Sport is : ', sportsindex)

print("All The Sports List is Completed")

Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Identified Sport is :  Cricket
The Identified Sport is :  Foot Ball
The Identified Sport is :  Shuttle
The Identified Sport is :  Table Tennis
The Identified Sport is :  Volley Ball
All The Sports List is Completed

Programme50
import os
os.system("clear")

favsports = ['Cricket', 'Foot Ball',  'Shuttle', 'Table Tennis', 'Volley Ball']
for sportsindex in range(len(favsports)):
	print('The Identified Sport is : ', favsports[sportsindex])
print "All The Sports List is Completed"
Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Identified Sport is :  Cricket
The Identified Sport is :  Foot Ball
The Identified Sport is :  Shuttle
The Identified Sport is :  Table Tennis
The Identified Sport is :  Volley Ball
All The Sports List is Completed

Programme51
for loopindex in range(5):
    print("The Current Value is : ", loopindex)
Output:
The Current Value is :  0
The Current Value is :  1
The Current Value is :  2
The Current Value is :  3
The Current Value is :  4

Programme52
for loopindex in range(0, 10):
    print("The Current Value is : ", loopindex)
Output:
The Current Value is :  0
The Current Value is :  1
The Current Value is :  2
The Current Value is :  3
The Current Value is :  4
The Current Value is :  5
The Current Value is :  6
The Current Value is :  7
The Current Value is :  8
The Current Value is :  9

Programme53
import os
os.system("clear")

for loopindex in range(0, 10, 2):
    print("The Current Value is : ", loopindex)
""" Output:
The Current Value is :  0
The Current Value is :  2
The Current Value is :  4
The Current Value is :  6
The Current Value is :  8
"""

Programme54
import os
os.system("clear")

for loopindex in range(5, 10):
    print("The Current Value is : ", loopindex)
""" Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Current Value is :  5
The Current Value is :  6
The Current Value is :  7
The Current Value is :  8
The Current Value is :  9
"""

Programme55
import os
os.system("clear")

for loopindex in range(3): #xrange funcation has been removed
    print("The Range Value is : ", loopindex)
else:
    print('Final loopindex Value is : %d' % (loopindex))

output: 'clear' is not recognized as an internal or external command,
operable program or batch file.
The Range Value is :  0
The Range Value is :  1
The Range Value is :  2
Final loopindex Value is : 2

import os
os.system("clear")

for loopindex in range(3): #xrange funcation has been removed
    print("The Range Value is : ", loopindex)
else:
    print('Final loopindex Value is : %d', (loopindex))

C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Range Value is :  0
The Range Value is :  1
The Range Value is :  2
Final loopindex Value is : %d 2

Programme56
import os
os.system("clear")

import math

print("The Ceiled Value of -26.32 is : ", math.ceil(-26.52))
print("The Ceiled Value of 125.45 is : ", math.ceil(125.45))
print("The Ceiled Value of 243L is : ", math.ceil(243))
print("The Ceiled Value of \"pi\" is : ", math.ceil(math.pi))
output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Ceiled Value of -26.32 is :  27
The Ceiled Value of 125.45 is :  126
The Ceiled Value of 243L is :  243
The Ceiled Value of "pi" is :  4

Programme57
mybreakval = int(input("Please Provide A Value For Break : "))
myvalue = 10
while myvalue > 0:              
	print('Current Value in The Process is : ', myvalue)
	myvalue = myvalue - 1
	if myvalue == mybreakval:
		break
Output:
Please Provide A Value For Break : 5
Current Value in The Process is :  10
Current Value in The Process is :  9
Current Value in The Process is :  8
Current Value in The Process is :  7
Current Value in The Process is :  6

Programme58
for mycharacter in 'ABC':
	if mycharacter == 'A':
 		continue
	print('The Current Letter in The Index is :', mycharacter)
Output;
The Current Letter in The Index is : B
The Current Letter in The Index is : C
Or:
for mycharacter in 'ABC':
	if mycharacter == 'H':
 		continue
	print('The Current Letter in The Index is :', mycharacter)
Output:
The Current Letter in The Index is : A
The Current Letter in The Index is : B
The Current Letter in The Index is : C

Programme59
import os
os.system("clear")

print("The Absolute Value of -25 is : ", abs(-25))
print("The Absolute Value of 25 is : ", abs(25))
print("The Absolute Value of -25.35 is : ", abs(-25.35))
print("The Absolute Value of 25.35 is : ", abs(25.35))
print("The Absolute Value of 235L is : ", abs(235))
Output;
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Absolute Value of -25 is :  25
The Absolute Value of 25 is :  25
The Absolute Value of -25.35 is :  25.35
The Absolute Value of 25.35 is :  25.35
The Absolute Value of 235L is :  235

Programme60
import os
os.system("clear")

import math

print("The Ceiled Value of -26.32 is : ", math.ceil(-26.99))
print("The Ceiled Value of 125.45 is : ", math.ceil(125.45))
#print("The Ceiled Value of 243L is : ", math.ceil(243L)) long - int has been removed from the python 3
print("The Ceiled Value of \"pi\" is : ", math.ceil(math.pi))

Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Ceiled Value of -26.32 is :  -26
The Ceiled Value of 125.45 is :  126
The Ceiled Value of "pi" is :  4

Programme61
import os
os.system("clear")

import math

print("The Floored Value of -26.32 is : ", math.floor(-26.32))
print("The Floored Value of 125.45 is : ", math.floor(125.45))
#print("The Floored Value of 243L is : ", math.floor(243L))
print("The Floored Value of \"pi\" is : ", math.floor(math.pi))

Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Floored Value of -26.32 is :  -27
The Floored Value of 125.45 is :  125
The Floored Value of "pi" is :  3

Programme62
import os
os.system("clear")

# print("The Comparision of 35 And 45 : ", cmp(35, 45)) comparision funcation has been removed in python 3
# print("The Comparision of 45 And 35 : ", cmp(45, 35))
# print("The Comparision of -35 And 45 : ", cmp(-35, 45))
# print("The Comparision of 35 And -45 : ", cmp(35, -45))

Programme63
import os
os.system("clear")

import math

print("The Exponentiation Value of -25.63 is : ", math.exp(-25.63))
print("The Exponentiation Value of 235.42 is : ", math.exp(235.42))
print("The Exponentiation Value of 200.23 is : ", math.exp(200.23))
#print("The Exponentiation Value of 341L is : ", math.exp(341L)
print("The Exponentiation Value of \"pi\" is : ", math.exp(math.pi))

Output: e^0 = 1
	E^1 = 2.718
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Exponentiation Value of -25.63 is :  7.396605035323884e-12
The Exponentiation Value of 235.42 is :  1.7442427627207943e+102
The Exponentiation Value of 200.23 is :  9.094610656313121e+86
The Exponentiation Value of "pi" is :  23.140692632779267


Programme64
import os
os.system("clear")

import math
#the fabs funcation will accept any interger or float values and giving return value with floating point. we have to use math module before writing the body.
#the abs method will also accept any interger or float values and giving only the exact values and we no need to import math module
print("The Absolute Value of -25 is : ", math.fabs(-25))
print("The Absolute Value of 25 is : ", math.fabs(25))
print("The Absolute Value of -25.35 is : ", math.fabs(-25.35))
print("The Absolute Value of 25.35 is : ", math.fabs(25.35))
#print("The Absolute Value of 235L is : ", math.fabs(235L))
#abs() method is a standard built-in method, for this, there is no need to import a module. But, the fabs() method is defined in the math module, for this we need to import the math module first.
#abs() method returns either an integer value or a float value based on given number type. But, fabs() method returns only float value, no matter given number is an integer type or a float type
Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Absolute Value of -25 is :  25.0
The Absolute Value of 25 is :  25.0
The Absolute Value of -25.35 is :  25.35
The Absolute Value of 25.35 is :  25.35

Programme65
import os
os.system("clear")
import math
print("The Natural Logarithmic Value of 235.45 is : ", math.log(235.45))
print("The Natural Logarithmic Value of 142.45 is : ", math.log(142.45))
#print("The Natural Logarithmic Value of 435L is : ", math.log(435L))
print("The Natural Logarithmic Value of \"pi\" is : ", math.log(math.pi))
Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Natural Logarithmic Value of 235.45 is :  5.461498576689563
The Natural Logarithmic Value of 142.45 is :  4.958991060943918
The Natural Logarithmic Value of "pi" is :  1.1447298858494002

Programme66
import os
os.system("clear")

import math

print("The Base 10 Logarithmic Value of 235.45 is : ", math.log10(235.45))
print("The Base 10 Logarithmic Value of 142.45 is : ", math.log10(142.45))
#print("The Base 10 Logarithmic Value of 435L is : ", math.log10(435L))
print("The Base 10 Logarithmic Value of \"pi\" is : ", math.log10(math.pi))

Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Base 10 Logarithmic Value of 235.45 is :  2.371898694778741
The Base 10 Logarithmic Value of 142.45 is :  2.1536624535754956
The Base 10 Logarithmic Value of "pi" is :  0.49714987269413385

Programme67
import os
os.system("clear")
print("Maximum Value in The List of (125, 253, 45) : ", max(125, 253, 45))
print("Maximum Value in The List of (-125, 53, 73) : ", min(-125, 53, 73))

Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
Maximum Value in The List of (125, 253, 45) :  253
Maximum Value in The List of (-125, 53, 73) :  -125
Syntax2: 
print("Maximum Value in The List of (125, 253, 45) : ", max(125, 253, 45))
print("Maximum Value in The List of (-125, 53, 73) : ", min(-125, 53, 73))

C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
Maximum Value in The List of (125, 253, 45) :  253
Maximum Value in The List of (-125, 53, 73) :  73

Programme68
import os
os.system("clear")
print("Maximum Value in The List of (125, 253, 45) : ", max(125, 253, 45))
print("Maximum Value in The List of (-125, 53, 73) : ", min(-125, 53, 73))

Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
Maximum Value in The List of (125, 253, 45) :  253
Maximum Value in The List of (-125, 53, 73) :  -125
programme2:

print("Maximum Value in The List of (125, 253, 45) : ", min(125, 253, 45))
print("Maximum Value in The List of (-125, 53, 73) : ", min(-125, 53, 73))

Output:

Maximum Value in The List of (125, 253, 45) :  45
Maximum Value in The List of (-125, 53, 73) :  -125

Programme69
import os
os.system("clear")

import math
#modf funcation will divide the interger and fraction. For example 235.99 will manipulated as(0.99(as fraction point), 235.0(as integer))
print("The Modf of 235.45 is : ", math.modf(235.45))
#print("The Modf of 452L is : ", math.modf(452L))
print("The Modf of \"pi\" is : ", math.modf(math.pi))

Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Modf of 235.45 is :  (0.44999999999998863, 235.0)
The Modf of "pi" is :  (0.14159265358979312, 3.0)

Programme70
import os
os.system("clear")

import math

print("The Power of 52 And 3 is : ", math.pow(52, 3))
print("The Power of 52 And -3 is : ", math.pow(52, -3))
print("The Power of 52.45 And 3.25 is : ", math.pow(52.45, 3.25))
print("The Power of 52 And 0 is : ", math.pow(52, 0))

Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Power of 52 And 3 is :  140608.0
The Power of 52 And -3 is :  7.111970869367319e-06
The Power of 52.45 And 3.25 is :  388304.8819393262
The Power of 52 And 0 is :  1.0

Programme71
import os
os.system("clear")
#the round funcation rounding the values, means x = 15.111111 and y= 3 and the final output would be as 15.111. The y value should be decide thefloating point limits. 
print("The Round Value of 1254.54647 is : ", round(1254.54647, 4))
print("The Round Value of 1254.54647 is : ", round(1254.54647, 3))
print("The Round Value of 1254.54647 is : ", round(1254.54647, 2))

Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Round Value of 1254.54647 is :  1254.5465
The Round Value of 1254.54647 is :  1254.546
The Round Value of 1254.54647 is :  1254.55


Programme72
import os
os.system("clear")

import math

print("The Square Root of 625 : ", math.sqrt(625))
print("The Square Root of 119 : ", math.sqrt(119))
print("The Square Root of \"pi\" : ", math.sqrt(math.pi))

output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Square Root of 625 :  25.0
The Square Root of 119 :  10.908712114635714
The Square Root of "pi" :  1.7724538509055159

Programme73
import os
os.system("clear")

import random
print("The Random Choice of [15, 32, 54, 61, 12] : ", random.choice([15, 32, 54, 61, 12]))
print("The Random Choice of The String 'ABC' is : ", random.choice('ABC'))

Output:
C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Random Choice of [15, 32, 54, 61, 12] :  12
The Random Choice of The String 'ABC' is :  A

C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Random Choice of [15, 32, 54, 61, 12] :  32
The Random Choice of The String 'ABC' is :  A

C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Random Choice of [15, 32, 54, 61, 12] :  15
The Random Choice of The String 'ABC' is :  C

Programme74
import os
os.system("clear")
import random
print("The Random Range in 300 To 900 With Step of 2 is : ", random.randrange(300, 900, 2))

Output;
C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Random Range in 300 To 900 With Step of 2 is :  828

C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Random Range in 300 To 900 With Step of 2 is :  738

Programme75
import os
os.system("clear")

import random

print("The Generated Random Number is : ", random.random())

Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Generated Random Number is :  0.6115312644883316

C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Generated Random Number is :  0.0728593802862636

C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Generated Random Number is :  0.20909000071217587

Programme76
import os
os.system("clear")

import random

random.seed( 5 )
print("The Generated Random Number With Seed 53 is : ", random.random())

Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Generated Random Number With Seed 53 is :  0.6229016948897019

Programme77
import os
os.system("clear")

import random

mylist = [15, 5, 35, 67, 4, 23, 84];
random.shuffle(mylist)
print(mylist)
print("The Reshuffled List of [15, 5, 35, 67, 4, 23, 84] Values Are : ",  mylist)

Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Reshuffled List of [15, 5, 35, 67, 4, 23, 84] Values Are :  [35, 67, 84, 5, 23, 4, 15]

C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
[4, 35, 67, 84, 5, 15, 23]
The Reshuffled List of [15, 5, 35, 67, 4, 23, 84] Values Are :  [4, 35, 67, 84, 5, 15, 23]

C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
[15, 67, 4, 23, 84, 5, 35]
The Reshuffled List of [15, 5, 35, 67, 4, 23, 84] Values Are :  [15, 67, 4, 23, 84, 5, 35]

C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
[5, 4, 35, 15, 84, 67, 23]
The Reshuffled List of [15, 5, 35, 67, 4, 23, 84] Values Are :  [5, 4, 35, 15, 84, 67, 23]

C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
[15, 35, 67, 5, 4, 84, 23]
The Reshuffled List of [15, 5, 35, 67, 4, 23, 84] Values Are :  [15, 35, 67, 5, 4, 84, 23]

Programme78
import os
os.system("clear")

import random

print("The Random Float of 15 And 25 is : ",  random.uniform(15, 25))

Output:
C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
[15, 35, 67, 5, 4, 84, 23]
The Reshuffled List of [15, 5, 35, 67, 4, 23, 84] Values Are :  [15, 35, 67, 5, 4, 84, 23]

C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Random Float of 15 And 25 is :  16.170957282188382

C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Random Float of 15 And 25 is :  22.08140175060147

Programme79
import os
os.system("clear")

mystring = 'Python is A Trending Laguage'
print("The Given String in Single Quotes is : ", mystring)

mystring = "SkyEss Techo Solutions Deals With BigData Training"
print("The Given String in Double Quotes is : ", mystring)

mystring = '''BigData Deals With Real Time Analytics, Which is The Future Trend'''
print("The Given String in Triple Quotes is : ", mystring)

mystring = """ABC GHI Deals With Bigdata Analytics
			Covering Hadoop Stack, HDFS Architecture, MapReduce With Java, Pig, Hive, HBase, Spark And Scala"""
print("The Given String in Triple Quotes With Multi Line Input is : ", mystring)
Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Given String in Single Quotes is :  Python is A Trending Laguage
The Given String in Double Quotes is :  SkyEss Techo Solutions Deals With BigData Training
The Given String in Triple Quotes is :  BigData Deals With Real Time Analytics, Which is The Future Trend
The Given String in Triple Quotes With Multi Line Input is :  ABC GHI Deals With Bigdata Analytics
                        Covering Hadoop Stack, HDFS Architecture, MapReduce With Java, Pig, Hive, HBase, Spark And Scala

Programme80
import os
os.system("clear")

mystring = 'GHI'
print("The Given String is : ", mystring)
#Here we have defined only 3 character of string, so output would be generated only for 3 characterstics.
print("The First Character in The Given String \"",mystring, "\" is : ", mystring[0])
print("The Second Character in The Given String \"",mystring, "\" is : ", mystring[1])
print("The Third Character in The Given String \"",mystring, "\" is : ", mystring[2])
print("The Fourth Character in The Given String \"",mystring, "\" is : ", mystring[3])
print("The Fifth Character in The Given String \"",mystring, "\" is : ", mystring[4])
print("The Sixth Character in The Given String \"",mystring, "\" is : ", mystring[5])
print("The Seventh Character in The Given String \"",mystring, "\" is : ", mystring[6])
print("The Eighth Character in The Given String \"",mystring, "\" is : ", mystring[7])

Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Given String is :  GHI
The First Character in The Given String " GHI " is :  G
The Second Character in The Given String " GHI " is :  H
The Third Character in The Given String " GHI " is :  I
Traceback (most recent call last):
  File "com.py", line 10, in <module>
    print("The Fourth Character in The Given String \"",mystring, "\" is : ", mystring[3])
IndexError: string index out of range

Programme81
import os
os.system("clear")

mystring = 'GHI'
print("The Given String is : ", mystring)
#Here we have defined only 3 character of string, so output would be generated only for 3 characterstics.
print("The First Character in The Given String \"",mystring, "\" is : ", mystring[0])
print("The Second Character in The Given String \"",mystring, "\" is : ", mystring[-1])
print("The Third Character in The Given String \"",mystring, "\" is : ", mystring[-2])
print("The Fourth Character in The Given String \"",mystring, "\" is : ", mystring[-3])
print("The Fifth Character in The Given String \"",mystring, "\" is : ", mystring[-4])
print("The Sixth Character in The Given String \"",mystring, "\" is : ", mystring[-5])
print("The Seventh Character in The Given String \"",mystring, "\" is : ", mystring[-6])
print("The Eighth Character in The Given String \"",mystring, "\" is : ", mystring[-7])

Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Given String is :  GHI
The First Character in The Given String " GHI " is :  G
The Second Character in The Given String " GHI " is :  I
The Third Character in The Given String " GHI " is :  H
The Fourth Character in The Given String " GHI " is :  G
Traceback (most recent call last):
  File "com.py", line 11, in <module>
    print("The Fifth Character in The Given String \"",mystring, "\" is : ", mystring[-4])
IndexError: string index out of range

Programme82
import os
os.system("clear")

mystring = 'GHI'
for i in range(len(mystring)):
	print(mystring[i])
print("The Given String is : ", mystring)

print("Slicing The Data From 1st To 4th Character From The Given String \"",mystring, "\" is : ",mystring[0:4])
print("Slicing The Data From 2st To 4th Character From The Given String \"",mystring, "\" is : ",mystring[1:6])
print("Slicing The Data From 1st To 4th Character From The Given String \"",mystring, "\" is : ",mystring[3:6])

Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
G
H
I
The Given String is :  GHI
Slicing The Data From 1st To 4th Character From The Given String " GHI " is :  GHI
Slicing The Data From 2st To 4th Character From The Given String " GHI " is :  H
Slicing The Data From 1st To 4th Character From The Given String " GHI " is :

C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
G
H
I
The Given String is :  GHI
Slicing The Data From 1st To 4th Character From The Given String " GHI " is :  GHI
Slicing The Data From 2st To 4th Character From The Given String " GHI " is :  HI
Slicing The Data From 1st To 4th Character From The Given String " GHI " is :

Programme83
import os
os.system("clear")

mystring = 'GHIjk'
print("The Given String is : ", mystring)

print("Slicing in Reverse Direction mystring[0:-1] : ", mystring[0:-1])
print("Slicing in Reverse Direction mystring[0:-2] : ", mystring[0:-2])
print("Slicing in Reverse Direction mystring[0:-3] : ", mystring[0:-3])
print("Slicing in Reverse Direction mystring[0:-4] : ", mystring[0:-4])
print("Slicing in Reverse Direction mystring[0:-5] : ", mystring[0:-5])

Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Given String is :  GHI
Slicing in Reverse Direction mystring[0:-1] :  GH
Slicing in Reverse Direction mystring[0:-2] :  G
Slicing in Reverse Direction mystring[0:-3] :
Slicing in Reverse Direction mystring[0:-4] :
Slicing in Reverse Direction mystring[0:-5] :

C:\Users\Nemmadi Gopi\Desktop>python com.py
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Given String is :  GHIjk
Slicing in Reverse Direction mystring[0:-1] :  GHIj
Slicing in Reverse Direction mystring[0:-2] :  GHI
Slicing in Reverse Direction mystring[0:-3] :  GH
Slicing in Reverse Direction mystring[0:-4] :  G
Slicing in Reverse Direction mystring[0:-5] :

Programme84
import os
os.system("clear")

firstname = "ABC"
middlename = "DEF"
lastname = "GHI"
print("The Given First Name is : ", firstname)
print("The Given Middle Name is : ", middlename)
print("The Given Last Name is : ", lastname)
print("Your Full Name is : ", firstname +" ", middlename +" " , lastname)
output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Given First Name is :  ABC
The Given Middle Name is :  DEF
The Given Last Name is :  GHI
Your Full Name is :  ABC  DEF  GHI

Programme85
import os
os.system("clear")

firstname = "ABC"
middlename = "DEF"
lastname = "GHI"
print("The Given First Name is : ", firstname)
print("The Given Middle Name is : ", middlename)
print("The Given Last Name is : ", lastname)
print("Your Full Name is : ", firstname + middlename +lastname)

Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Given First Name is :  ABC
The Given Middle Name is :  DEF
The Given Last Name is :  GHI
Your Full Name is :  ABCDEFGHI

programme2:
import os
os.system("clear")

firstname = "ABC"
middlename = "DEF"
lastname = "GHI"
print("The Given First Name is : ", firstname)
print("The Given Middle Name is : ", middlename)
print("The Given Last Name is : ", lastname)
print("Your Full Name is : ", firstname +" " + middlename+" "+lastname)
Output;
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Given First Name is :  ABC
The Given Middle Name is :  DEF
The Given Last Name is :  GHI
Your Full Name is :  ABC DEF GHI

Programme86
import os
os.system("clear")

firstname = "ABC"
print("The Given First Name is : ", firstname * 3)
Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Given First Name is :  ABCABCABC

Programme87
import os
os.system("clear")

print("Printing Strings With Path Character")
print("Using The Escape Sequence Method For Implementation")
print('This is My Oracles Path : C:\\Oracle\\app\\skyess\\product')
Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
Printing Strings With Path Character
Using The Escape Sequence Method For Implementation
This is My Oracles Path : C:\Oracle\app\skyess\product

Programme88
import os
os.system("clear")

print("Printing Strings With Multiple Lines")
print("Using The Escape Sequence Method For Implementation")
print('ABC\nDEF\nGHI')

output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
Printing Strings With Multiple Lines
Using The Escape Sequence Method For Implementation
ABC
DEF
GHI

Programme89
import os
os.system("clear")

print("Printing Strings With Hexa Decimal Values")
print("Using The Escape Sequence Method For Implementation")
print('print("This is \x35\x75\x65 representation"')

Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
Printing Strings With Hexa Decimal Values
Using The Escape Sequence Method For Implementation
print("This is 5ue representation"

Programme90
import os
os.system("clear")

print("Your Name is \x61 \nABC DEF GHI") #\x formate will be a hexadecimal values

Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
Your Name is a
ABC DEF GHI


Programme91
import os
os.system("clear")

print(R"Your Name is \x61 \nABC DEF GHI") #we have meantioned R infront of string, so output would of the string will be same as inpt string.

Output:

'clear' is not recognized as an internal or external command,
operable program or batch file.
Your Name is \x61 \nABC DEF GHI

Programme92
import os
os.system("clear")

mystring = "skyess techno solutions"
print("The String in Capital Letters : ", mystring.capitalize()) # capitalize() would print first letter of string should as capital letter.

Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The String in Capital Letters :  Skyess techno solutions

Programme93
import os
os.system("clear")

mystring = "skyess techno solutions"
print("The String in Center : ", mystring.center(40, 'x')) #mystring.center() will center the string along with mentioned symbol "x". 

Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The String in Center :  xxxxxxxxskyess techno solutionsxxxxxxxxx

Programme94
import os
os.system("clear")

mystring = "skyess"
print("The String in Center:",mystring.center(10),"hi")


Output;
'clear' is not recognized as an internal or external command,
operable program or batch file.
The String in Center :       skyess

'clear' is not recognized as an internal or external command,
operable program or batch file.
The String in Center:      skyess      hi

Programme95
import os
os.system("clear")

mystring = "skyess techno solutions"
print("The Length of The String is : ", len(mystring))


Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Length of The String is :  23

Programme2:
import os
os.system("clear")

mystring = "solutions"
print("The Length of The String is : ", len(mystring))

Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Length of The String is :  9


Programme96
import os
os.system("clear")

mystring = "skyess techno solutions"
print("The String in Lower Case : ", mystring.lower())

Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The String in Lower Case :  skyess techno solutions

Programme97
import os
os.system("clear")
#Title function in python is the Python String Method which is used to convert the first character in each word to Uppercase and remaining characters to Lowercase in string and returns new string.
mystring = "skyess techno solutions"
print("The String in Lower Case : ", mystring.title())

Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The String in Lower Case :  Skyess Techno Solutions

Programme98
import os
os.system("clear")

mystring = "skyess techno solutions";
print("The String in Lower Case : ", mystring.upper())

Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The String in Lower Case :  SKYESS TECHNO SOLUTIONS

Programme99
import os
os.system("clear")

mydelim = ","
mystrseq = ("ABC", "DEF", "GHI")
print("The Final String is : ", mydelim.join(mystrseq))

Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Final String is :  ABC,DEF,GHI

Programme100
import os
os.system("clear")

mysting = "                   SkyEss Techno Solutions" #it will remove the left space from the string(as mysting)
print("The Given String is : ", mysting.lstrip())

output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Given String is :  SkyEss Techno Solutions

Programme101
import os
os.system("clear")

mysting = "****************SkyEss Techno Solutions"
print("The Given String is : ", mysting)

Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Given String is :  ****************SkyEss Techno Solutions

Programme102
import os
os.system("clear")

mysting = "****************SkyEss Techno Solutions"
print("The Given String is : ", mysting.lstrip('*'))

output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Given String is :  SkyEss Techno Solutions

Programme103
import os
os.system("clear")

mysting = "SkyEss Techno Solutions                   "
print("The Given String is : ", mysting.rstrip())

Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Given String is :  SkyEss Techno Solutions

Programme104
import os
os.system("clear")

mysting = "SkyEss Techno Solutions***************";
print("The Given String is : ", mysting.rstrip('*'))

Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Given String is :  SkyEss Techno Solutions

Programme105
import os
os.system("clear")

mystring = "SkyEssaz"
print("The Maximum Value in The String : ", max(mystring))
print("The Minimum Value in The String : ", min(mystring))

Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Maximum Value in The String :  z
The Minimum Value in The String :  E

programme2:
import os
os.system("clear")

mystring = "SkyEssaz"
print("The Maximum Value in The String : ", max(mystring))
print("The Minimum Value in The String : ", min(mystring))

Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The Maximum Value in The String :  z
The Minimum Value in The String :  A

Programme106
import os
os.system("clear")

mystring = "SkyEss"
print("The String With Zero Fills : ", mystring.zfill(10))#Zfill() will Returns a copy of the string with '0' characters   
padded to the leftside of the given string.


Output:
'clear' is not recognized as an internal or external command,
operable program or batch file.
The String With Zero Fills :  0000SkyEss