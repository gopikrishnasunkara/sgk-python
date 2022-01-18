#Python RegEx(Regular Expression):
#A RegEX, or Regular Expression, is a sequence of characters that form a search pattern.
#RegEx can be used to check if a string contains the specified search pattern.

#RegEx Module:
#RegEx is implemented by re package. First we need to implement the re package with "Import re".
#import re Module:
#import re

#RegEx Functions:

#The re module offers a set of functions that allows us to search a string for a match:

#Function:   - 	Description:
#findall     -	Returns a list containing all matches
#search	     - 	Returns a Match object if there is a match anywhere in the string(Start(), Span(), string())
#split       -	Returns a list where the string has been split at each match
#sub         -	Replaces one or many matches with a string


#Practise():
>>> import re
>>> str = "Powerstar Pawankalayan"
>>> x = re.findall("P", str)
>>> print(x)
['P', 'P']
>>> str = "Powerstar Pawankalayan"
>>> x = re.findall("p", str)
>>> print(x)
[]
>>> import re
>>> str = "Powerstar Pawankalayan"
>>> x = re.search("P", str)
>>> print(x)
<_sre.SRE_Match object; span=(0, 1), match='P'>
>>> print(x.start())
0
>>> str = "Powerstar Pawankalayan"
>>> x = re.search("p", str)
>>> print(x)
None
>>> str = "Powerstar Pawankalayan"
>>> x = re.search("w", str)
>>> print(x.start())
2
>>> str = "Powerstar Pawankalayan"
>>> x = re.search("wer", str)
>>> print(x.start())
2
>>> x = re.search("wer", str)
>>> print(x.start())
2
>>> import re
>>> str = "Powerstar Pawankalayan"
>>> x = re.search("Pawankalayan", str)
>>> print(x.start())
10
>>> import re
>>> str = "Powerstar Pawankalayan"
>>> x = re.search("Pawankalayan", str)
>>> print(x.span())
(10, 22)
>>> str = "Powerstar Pawankalayan"
>>> x = re.search("Pawankalayan", str)
>>> print(x.string())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object is not callable
>>> print(x.string)
Powerstar Pawankalayan
>>> import re
>>> str = "Powerstar Pawankalayan"
>>> x = re.split("Pawankalayan", str)
>>> print(x)
['Powerstar ', '']
>>> x = re.split("P", str)
>>> print(x)
['', 'owerstar ', 'awankalayan']
>>> str = "Powerstar Pawankalayan"
>>> x = re.split(" ", str)
>>> print(x)
['Powerstar', 'Pawankalayan']
>>> str = "Powerstar Pawankalayan"
>>> x = re.split("",str)(Non_Empty pattern will work after version of python 3.7 or else we will get same error)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\nemma\AppData\Local\Programs\Python\Python36\lib\re.py", line 212, in split
    return _compile(pattern, flags).split(string, maxsplit)
ValueError: split() requires a non-empty pattern match.

>>> x = re.split(" ",str)
>>> print(x)
['Powerstar', 'Pawankalayan']

>>> str = "Powerstar Pawankalayan is an Actor"
>>> x = re.split("P", str)
>>> print(x)
['', 'owerstar ', 'awankalayan is an Actor']
>>> x = re.split(" ", str)
>>> print(x)
['Powerstar', 'Pawankalayan', 'is', 'an', 'Actor']
>>> x = re.sub("P","p",str)
>>> print(x)
powerstar pawankalayan is an Actor
>>> str = "Powerstar Pawankalayan is an Actor"
>>> x = re.sub("A","a",str)
>>> print(x)
Powerstar Pawankalayan is an actor

#Syntax:
import re
str = "Powerstar Pawankalayan is an Actor"
x = re.sub("P","p", str)
print(x)
Output: ['Powerstar', 'Ppawankalayan is an Actor']

#Syntax:
import re
str = "Powerstar Pawankalayan is an Actor"
x = re.sub("A","a", str)
print(x)


import re
#Metacharacters:
#1. [] - A set of characters("[a-m]"): it find the character range between metioned in findall as like below.
#str = "i love India"
#x = re.findall("[a-m,A-m]", str)
#print(x)


#2.\ - Singnals s special sequence(can also be used to escape special characters)("\d"):
#txt = "That will be 59 dollars"
#Find all digit characters:
#x = re.findall("\d", txt)
#print(x)

#output: It will find the all digits from the string or variable.

#3 . - any character(except newline character)('he..o"):

txt = "hello planet"
#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
x = re.findall("he..o", txt)
print(x)

output:['hello']


another example:
import re
txt = "hello planet"
#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
x = re.findall(".", txt)
print(x)

output:['h', 'e', 'l', 'l', 'o', ' ', 'p', 'l', 'a', 'n', 'e', 't']

4. ^ - starts with ("^hello"):
import re

txt = "hello planet"

#Check if the string starts with 'hello':

x = re.findall("^hello", txt)
print(x)

Output:['hello']


#Another example:
txt = "The hello planet"

#Check if the string starts with 'hello':

x = re.findall("^hello", txt)
print(x)
output: []

5. $ - Ends with ("planet$"):
import re

txt = "hello planet"

#Check if the string starts with 'hello':

x = re.findall("planet$", txt)
print(x)

Output:['planet']


#Another example:
txt = "The hello planet"

#Check if the string starts with 'hello':

x = re.findall("^planet$", txt)
print(x)
output: []

6. * - Zero or more occurrences("he.*o"):
txt = "helloooo planet"

#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

x = re.findall("he.*o", txt)

print(x)
txt = "helloooo planet"

#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":
x = re.findall("he.*o", txt)
print(x)
output:['helloooo']

Anthor example:
#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":
x = re.findall("he*o", txt)
print(x)

output: []

7. + - One or more occurrences("he.+o"):
txt = "hello planet"
#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":
x = re.findall("he.+o", txt)

print(x)
Output: ['hello']

another example:
txt = "hello planet"
#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":
x = re.findall("he+o", txt)

print(x)

Output: []

8. ? - Zero or one occurrences("he.?o"):
txt = "hello planet"

#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":

x = re.findall("he.?o", txt)

print(x)

#This time we got no match, because there were not zero, not one, but two characters between "he" and the "o"

Output: []

9. {} - Exactly the specified number of occurrences("he{2}o"):
txt = "hello planet"

#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

x = re.findall("he.{2}o", txt)

print(x)
output: ['hello']

Another example:

txt = "hello planet"

#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

x = re.findall("he.{3}o", txt)

print(x)
output: []

10. |- Either or("falls|stays):
txt = "The rain in Spain falls mainly in the plain!"

#Check if the string contains either "falls" or "stays":

x = re.findall("falls|stays", txt)

print(x)
output: ['falls']