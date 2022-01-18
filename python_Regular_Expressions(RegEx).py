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