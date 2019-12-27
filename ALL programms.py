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

totalsales = int(raw_input("Please Enter The Sales Value : "))
givecountry = raw_input("Please Enter The Country Name in ISO Standard : ")

if givecountry == "IN":
    if totalsales <= 50:
        print "The Total Shipping Cost is  : 50INR"
elif totalsales <= 100:
        print "The Total Shipping Cost is : 25INR"
elif totalsales <= 150:
	    print "The Total Shipping Cost is : 5INR"
else:
        print "The Shipping is Done FREE of Cost"

if givecountry == "US": 
	  if totalsales <= 50:
	    print "The Shipping Cost is :  100USD"
else:
	    "The Shipping is Done FREE of Cost"

Programme35
import os
os.system("clear")

print "Program To Print a Sequence of Numbers"
loopcounter = 1
while (loopcounter <= 10):
   print "The Line Number is : ", loopcounter
   loopcounter = loopcounter + 1

Programme36
import os
os.system("clear")

print "Program To Print a Sequence of Numbers"
loopcounter = 1
while (loopcounter <= 10):
   print "The Line Number is : ", loopcounter
   loopcounter = loopcounter + 1

print "We Are Out of The Loop"
print "Operating in The Main Block of The Program"

Programme37
import os
os.system("clear")

print "Program To Print a Sequence of Numbers"
endpoint = int(raw_input("Please Enter The Termination Point : "))
loopcounter = 1
while (loopcounter <= endpoint):
   print "The Line Number is : ", loopcounter
   loopcounter = loopcounter + 1

Programme38
import os
os.system("clear")

print "Program To Print a Sequence of Numbers"
startpoint = int(raw_input("Please Enter The Starting Point : "))
while (startpoint <= 10):
   print "The Line Number is : ", startpoint
   startpoint = startpoint + 1

Programme39
import os
os.system("clear")

print "Program To Print a Sequence of Numbers"
startpoint = int(raw_input("Please Enter The Starting Point : "))
if (startpoint <= 0 or startpoint > 10):
   print "Sorry! Index is Out of The Boundary...Cannot Proceed"
else:
   while (startpoint <= 10):
     print "The Line Number is : ", startpoint
     startpoint = startpoint + 1
Programme40
import os
os.system("clear")

print "Program To Print a Sequence of Numbers"
startpoint = int(raw_input("Please Enter The Starting Point : "))
endpoint = int(raw_input("Please Enter The Ending Point : "))
if (startpoint <= 0 or endpoint > 10):
   print "Sorry! Index is Out of The Boundary...Cannot Proceed"
else:
   while (startpoint <= endpoint):
     print "The Line Number is : ", startpoint
     startpoint = startpoint + 1
Programme41
import os
os.system("clear")

print "Program To Add Natural Numbers..."
datainput = int(raw_input("Please Enter The Number of Values : "))

finalsum = 0
loopindex = 1

while loopindex <= datainput:
    finalsum = finalsum + loopindex
    loopindex = loopindex + 1

print "The Sum of ", datainput, " Natural Numbers is : ", finalsum

Programme42
import os
os.system("clear")

print "Program To Add Natural Numbers..."
datainput = int(raw_input("Please Enter The Number of Values : "))

finalsum = 0
loopindex = 1

while loopindex <= datainput:
    finalsum = finalsum + loopindex
    print "The Current Sum is : ", finalsum
    loopindex = loopindex + 1

print "The Sum of ", datainput, " Natural Numbers is : ", finalsum

Programme43
import os
os.system("clear")

loopcounter = 0

while loopcounter < 3:
    print("Curently Working Inside The Loop")
    loopcounter = loopcounter + 1
else:
    print("Now Working in The \"else\" Part of The Loop 01")

print("Now Working Totally Outside The Loop Control 01")
print("Now Working Totally Outside The Loop Control 02")
Programme44
import os
os.system("clear")

mypassword = ""
while mypassword != "Personal":
    mypassword = raw_input("Please Enter Your Password : ")
    if mypassword == "Personal":
        print("Congratulations Your Password Matches, You Are Privileged To Enter")
    else:
        print("Sorry! Your Password Doesnot Matches, We Cannot Allow You")
Programme45
import os
os.system("clear")

invalidvalue = True
while invalidvalue:
    inputvalue = int(input("Please Input a Number Within 10 And 20 : "))
    if inputvalue >= 10 and inputvalue <= 20:
        invalidvalue = False
    else:
        print("Sorry! Number Should Be in Between 10 And 20 Only")
        print("Please Re-Enter The Value...")
print("Finally You Entered The Correct Value...")
print("Terminating The Process As Valid Input is Found...")
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
        if yourguess > valueguessed:
            print("The Guessed Number Too Big")
        elif yourguess < valueguessed:
            print("The Guessed Number is Too Small")
    else:
        print("Sorry! You Decided To Leave The Game...")
        break
else:
    print("That's The Spirit, Finally You Guessed Correctly")
Programme47
import os
os.system("clear")

for loopindex in 'ABC':     
   print 'The Character in Index is : ', loopindex
Programme48
import os
os.system("clear")

mystring = raw_input("Please Enter Any String : ")
for loopindex in mystring:     
   print 'The Character in Index is : ', loopindex
Programme49
import os
os.system("clear")

favsports = ['Cricket', 'Foot Ball',  'Shuttle', 'Table Tennis', 'Volley Ball']
for sportsindex in favsports: 
   print 'The Identified Sport is : ', sportsindex

print "All The Sports List is Completed"
Programme50
import os
os.system("clear")

favsports = ['Cricket', 'Foot Ball',  'Shuttle', 'Table Tennis', 'Volley Ball']
for sportsindex in range(len(favsports)): 
   print 'The Identified Sport is : ', favsports[sportsindex]

print "All The Sports List is Completed"
Programme51
for loopindex in range(5):
    print "The Current Value is : ", loopindex
Programme52
for loopindex in range(0, 10):
    print "The Current Value is : ", loopindex
Programme53
import os
os.system("clear")

for loopindex in range(0, 10, 2):
    print "The Current Value is : ", loopindex

Programme54
import os
os.system("clear")

for loopindex in range(5, 10):
    print "The Current Value is : ", loopindex
Programme55
import os
os.system("clear")

for loopindex in xrange(3):
    print "The Range Value is : ", loopindex
else:
    print 'Final loopindex Value is : %d' % (loopindex)
Programme56
import os
os.system("clear")

import math

print "The Ceiled Value of -26.32 is : ", math.ceil(-26.32)
print "The Ceiled Value of 125.45 is : ", math.ceil(125.45)
print "The Ceiled Value of 243L is : ", math.ceil(243L)
print "The Ceiled Value of \"pi\" is : ", math.ceil(math.pi)
Programme57
mybreakval = int(raw_input("Please Provide A Value For Break : "))
myvalue = 10
while myvalue > 0:              
   print 'Current Value in The Process is : ', myvalue
   myvalue = myvalue - 1
   if myvalue == mybreakval:
      break
Programme58
for mycharacter in 'ABC':
   if mycharacter == 'h':
      continue
   print 'The Current Letter in The Index is :', mycharacter
Programme59
import os
os.system("clear")

print "The Absolute Value of -25 is : ", abs(-25)
print "The Absolute Value of 25 is : ", abs(25)
print "The Absolute Value of -25.35 is : ", abs(-25.35)
print "The Absolute Value of 25.35 is : ", abs(25.35)
print "The Absolute Value of 235L is : ", abs(235L)
Programme60
import os
os.system("clear")

import math

print "The Ceiled Value of -26.32 is : ", math.ceil(-26.32)
print "The Ceiled Value of 125.45 is : ", math.ceil(125.45)
print "The Ceiled Value of 243L is : ", math.ceil(243L)
print "The Ceiled Value of \"pi\" is : ", math.ceil(math.pi)
Programme61
import os
os.system("clear")

import math

print "The Floored Value of -26.32 is : ", math.floor(-26.32)
print "The Floored Value of 125.45 is : ", math.floor(125.45)
print "The Floored Value of 243L is : ", math.floor(243L)
print "The Floored Value of \"pi\" is : ", math.floor(math.pi)
Programme62
import os
os.system("clear")

print "The Comparision of 35 And 45 : ", cmp(35, 45)
print "The Comparision of 45 And 35 : ", cmp(45, 35)
print "The Comparision of -35 And 45 : ", cmp(-35, 45)
print "The Comparision of 35 And -45 : ", cmp(35, -45)
Programme63
import os
os.system("clear")

import math

print "The Exponentiation Value of -25.63 is : ", math.exp(-25.63)
print "The Exponentiation Value of 235.42 is : ", math.exp(235.42)
print "The Exponentiation Value of 200.23 is : ", math.exp(200.23)
print "The Exponentiation Value of 341L is : ", math.exp(341L)
print "The Exponentiation Value of \"pi\" is : ", math.exp(math.pi)

Programme64
import os
os.system("clear")

import math

print "The Absolute Value of -25 is : ", math.fabs(-25)
print "The Absolute Value of 25 is : ", math.fabs(25)
print "The Absolute Value of -25.35 is : ", math.fabs(-25.35)
print "The Absolute Value of 25.35 is : ", math.fabs(25.35)
print "The Absolute Value of 235L is : ", math.fabs(235L)
Programme65
import os
os.system("clear")

import math

print "The Natural Logarithmic Value of 235.45 is : ", math.log(235.45)
print "The Natural Logarithmic Value of 142.45 is : ", math.log(142.45)
print "The Natural Logarithmic Value of 435L is : ", math.log(435L)
print "The Natural Logarithmic Value of \"pi\" is : ", math.log(math.pi)
Programme66
aimport os
os.system("clear")

import math

print "The Base 10 Logarithmic Value of 235.45 is : ", math.log10(235.45)
print "The Base 10 Logarithmic Value of 142.45 is : ", math.log10(142.45)
print "The Base 10 Logarithmic Value of 435L is : ", math.log10(435L)
print "The Base 10 Logarithmic Value of \"pi\" is : ", math.log10(math.pi)
Programme67
import os
os.system("clear")

print "Maximum Value in The List of (125, 253, 45) : ", max(125, 253, 45)
print "Maximum Value in The List of (-125, 53, 73) : ", max(-125, 53, 73)

Programme68
import os
os.system("clear")

print "Minimum Value in The List of (125, 253, 45) : ", min(125, 253, 45)
print "Minimum Value in The List of (-125, 53, 73) : ", min(-125, 53, 73)

Programme69
import os
os.system("clear")

import math

print "The Modf of 235.45 is : ", math.modf(235.45)
print "The Modf of 452L is : ", math.modf(452L)
print "The Modf of \"pi\" is : ", math.modf(math.pi)
Programme70
import os
os.system("clear")

import math

print "The Power of 52 And 3 is : ", math.pow(52, 3)
print "The Power of 52 And -3 is : ", math.pow(52, -3)
print "The Power of 52.45 And 3.25 is : ", math.pow(52.45, 3.25)
print "The Power of 52 And 0 is : ", math.pow(52, 0)
Programme71
import os
os.system("clear")

print "The Round Value of 1254.54647 is : ", round(1254.54647, 4)
print "The Round Value of 1254.54647 is : ", round(1254.54647, 3)
print "The Round Value of 1254.54647 is : ", round(1254.54647, 2)
Programme72
import os
os.system("clear")

import math

print "The Square Root of 625 : ", math.sqrt(625)
print "The Square Root of 119 : ", math.sqrt(119)
print "The Square Root of \"pi\" : ", math.sqrt(math.pi)
Programme73
import os
os.system("clear")

import random

print "The Random Choice of [15, 32, 54, 61, 12] : ", random.choice([15, 32, 54, 61, 12])
print "The Random Choice of The String 'ABC' is : ", random.choice('ABC')
Programme74
import os
os.system("clear")

import random

print "The Random Range in 300 To 900 With Step of 2 is : ", random.randrange(300, 900, 2)

Programme75
import os
os.system("clear")

import random

print "The Generated Random Number is : ", random.random()

Programme76
import os
os.system("clear")

import random

random.seed( 53 )
print "The Generated Random Number With Seed 53 is : ", random.random()
Programme77
import os
os.system("clear")

import random

mylist = [15, 5, 35, 67, 4, 23, 84];
random.shuffle(mylist)
print "The Reshuffled List of [15, 5, 35, 67, 4, 23, 84] Values Are : ",  mylist
Programme78
import os
os.system("clear")

import random

print "The Random Float of 15 And 25 is : ",  random.uniform(15, 25)

Programme79
import os
os.system("clear")

mystring = 'Python is A Trending Laguage'
print "The Given String in Single Quotes is : ", mystring

mystring = "SkyEss Techo Solutions Deals With BigData Training"
print "The Given String in Double Quotes is : ", mystring

mystring = '''BigData Deals With Real Time Analytics, Which is The Future Trend'''
print "The Given String in Triple Quotes is : ", mystring

mystring = """ABC GHI Deals With Bigdata Analytics
			Covering Hadoop Stack, HDFS Architecture, MapReduce With Java, Pig, Hive, HBase, Spark And Scala"""
print "The Given String in Triple Quotes With Multi Line Input is : ", mystring
Programme80
import os
os.system("clear")

mystring = 'GHI'
print "The Given String is : ", mystring

print "The First Character in The Given String \"",mystring, "\" is : ", mystring[0]
print "The Second Character in The Given String \"",mystring, "\" is : ", mystring[1]
print "The Third Character in The Given String \"",mystring, "\" is : ", mystring[2]
print "The Fourth Character in The Given String \"",mystring, "\" is : ", mystring[3]
print "The Fifth Character in The Given String \"",mystring, "\" is : ", mystring[4]
print "The Sixth Character in The Given String \"",mystring, "\" is : ", mystring[5]
print "The Seventh Character in The Given String \"",mystring, "\" is : ", mystring[6]
print "The Eighth Character in The Given String \"",mystring, "\" is : ", mystring[7]
Programme81
import os
os.system("clear")

mystring = 'GHI'
print "The Given String is : ", mystring

print "The First Last Character in The Given String \"",mystring, "\" is : ", mystring[-1]
print "The Second Last Character in The Given String \"",mystring, "\" is : ", mystring[-2]
print "The Third Last Character in The Given String \"",mystring, "\" is : ", mystring[-3]
print "The Fourth Last Character in The Given String \"",mystring, "\" is : ", mystring[-4]
print "The Fifth Last Character in The Given String \"",mystring, "\" is : ", mystring[-5]
print "The Sixth Last Character in The Given String \"",mystring, "\" is : ", mystring[-6]
print "The Seventh Last Character in The Given String \"",mystring, "\" is : ", mystring[-7]
print "The Eighth Last Character in The Given String \"",mystring, "\" is : ", mystring[-8]
Programme82
import os
os.system("clear")

mystring = 'GHI'
print "The Given String is : ", mystring

print "Slicing The Data From 1st To 4th Character From The Given String \"",mystring, "\" is : ", mystring[0:4]
print "Slicing The Data From 2st To 4th Character From The Given String \"",mystring, "\" is : ", mystring[1:6]
print "Slicing The Data From 1st To 4th Character From The Given String \"",mystring, "\" is : ", mystring[3:6]
Programme83
import os
os.system("clear")

mystring = 'GHI'
print "The Given String is : ", mystring

print "Slicing in Reverse Direction mystring[0:-1] : ", mystring[0:-1]
print "Slicing in Reverse Direction mystring[0:-2] : ", mystring[0:-2]
print "Slicing in Reverse Direction mystring[0:-3] : ", mystring[0:-3]
print "Slicing in Reverse Direction mystring[0:-4] : ", mystring[0:-4]
print "Slicing in Reverse Direction mystring[0:-5] : ", mystring[0:-5]

Programme84
import os
os.system("clear")

firstname = "ABC"
middlename = "DEF"
lastname = "GHI"
print "The Given First Name is : ", firstname
print "The Given Middle Name is : ", middlename
print "The Given Last Name is : ", lastname
print "Your Full Name is : ", firstname + middlename + lastname
Programme85
import os
os.system("clear")

firstname = "ABC"
middlename = "DEF"
lastname = "GHI"
print "The Given First Name is : ", firstname
print "The Given Middle Name is : ", middlename
print "The Given Last Name is : ", lastname
print "Your Full Name is : ", firstname + " " + middlename + " " + lastname
Programme86
import os
os.system("clear")

firstname = "ABC"
print "The Given First Name is : ", firstname * 3
Programme87
import os
os.system("clear")

print "Printing Strings With Path Character"
print "Using The Escape Sequence Method For Implementation"
print 'This is My Oracles Path : C:\\Oracle\\app\\skyess\\product"'
Programme88
import os
os.system("clear")

print "Printing Strings With Multiple Lines"
print "Using The Escape Sequence Method For Implementation"
print 'ABC\nDEF\nGHI'

Programme89
import os
os.system("clear")

print "Printing Strings With Hexa Decimal Values"
print "Using The Escape Sequence Method For Implementation"
print 'print "This is \x35\x75\x65 representation"'
Programme90
import os
os.system("clear")

print "Your Name is \x61 \nABC DEF GHI"
Programme91
import os
os.system("clear")

print R"Your Name is \x61 \nABC DEF GHI"
Programme92
import os
os.system("clear")

mystring = "skyess techno solutions";
print "The String in Capital Letters : ", mystring.capitalize()
Programme93
import os
os.system("clear")

mystring = "skyess techno solutions";
print "The String in Center : ", mystring.center(40, 'x')
Programme94
import os
os.system("clear")

mystring = "skyess";
print "The String in Center : ", mystring.center(16)


Programme95
import os
os.system("clear")

mystring = "skyess techno solutions";
print "The Length of The String is : ", len(mystring)

Programme96
import os
os.system("clear")

mystring = "SKYESS TECHNO SOLUTIONS";
print "The String in Lower Case : ", mystring.lower()
Programme97
import os
os.system("clear")

mystring = "skyess techno solutions";
print "The String in Lower Case : ", mystring.title()

Programme98
import os
os.system("clear")

mystring = "skyess techno solutions";
print "The String in Lower Case : ", mystring.upper()

Programme99
import os
os.system("clear")

mydelim = ","
mystrseq = ("Sathsih", "DEF", "GHI");
print "The Final String is : ", mydelim.join(mystrseq)
Programme100
import os
os.system("clear")

mysting = "                   SkyEss Techno Solutions";
print "The Given String is : ", mysting.lstrip()
Programme101
import os
os.system("clear")

mysting = "****************SkyEss Techno Solutions";
print "The Given String is : ", mysting
Programme102
import os
os.system("clear")

mysting = "****************SkyEss Techno Solutions";
print "The Given String is : ", mysting.lstrip('*')
Programme103
import os
os.system("clear")

mysting = "SkyEss Techno Solutions                   ";
print "The Given String is : ", mysting.rstrip()
Programme104
import os
os.system("clear")

mysting = "SkyEss Techno Solutions***************";
print "The Given String is : ", mysting.rstrip('*')
Programme105
import os
os.system("clear")

mystring = "SkyEss";
print "The Maximum Value in The String : ", max(mystring)
print "The Minimum Value in The String : ", min(mystring)
Programme106
import os
os.system("clear")

mystring = "SkyEss";
print "The String With Zero Fills : ", mystring.zfill(10)
