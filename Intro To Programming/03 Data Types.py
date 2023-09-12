'''
Data Types
1)Introduction
2)Integers
3)Floats
4)Booleans
5)Strings
6)Some intersting operations on diff data types
''' 

#1)Introduction
'''
Whenever we create a variable in Python it has
a value with a corresponding data type.
Different types of data types : integers,floats,booleans,strings,
dictionaries,sets,lists,tuples etc.
Data types are important because they determine what kind of actions we can do with them.
For example we can divide int with float but cannot divide int with strings.
To avoid such errors we need to make sure actions match data types.
'''
a = 10         #int
b = -10.1      #float
c = True       #booleans
d = 'stringsss'#strings

#2)Integers
'''
Numbers without any fractional part 
can be positive or negative
(...-1,0,1...)
'''
print(f"Value of variable a is : {a}")
print(f"Data type of vriable a is : {type(a)}")

#3)Floats
'''
Numbers with fractional part are floats
they can have many numbers after decimal
example : 3.12442523480985 , -0.3234 , etc.
Can convert float to int and int to float
'''
o = -10.45
p = 11.9
print(f"Value of o after converting to int is rounded to : {int(o)}")
print(f"Value of p after converting to int is rounded to : {int(p)}")
print(f"Value of variable b is : {b}")
print(f"Data type of vriable b is : {type(b)}")
print(round(b))
#with help of round function we can round these float data types.
#round(value)
#numbers like 1. , 1.0 , 1.00 will be recognized as a float (even though these don't have actually any fractional part)

#4)Booleans
'''
Booleans represent only one of two values : True or Flase
They are also used to represent the truth value of an expression.
Like a<b a==c etc.
Switch values of booleans using not
not True is False 
not False is True
'''
e = b>c
f = not c
print(f"Value of variable c is : {c}")
print(f"Data type of vriable c is : {type(c)}")
print(f"Value of variable e is : {e}")
print(f"Data type of vriable e = (b>a) is : {type(e)}")
print(f"Value of variable f is : {f}")
print(f"Data type of vriable f = not c is : {type(f)}")

#5)Strings
'''
String is a collection of characters like alphabet letters,
punctuation, numerical digits, etc.
commonly used represent text.
we can get length of a string using len()
len() calculates all characters including spaces,symbols,etc
special type of string is empty string which has len zero
'String' '2039.2343'
"String" "aojdflja123r"
We can add two strings-> string concatenation
We can multiply sttring with integer
We can divide and substract string
we cannot multiply strings with float
'''
g = len(d)
h = ""
i = len(h)
j = '121'
l = int(j)
k = float(j)
x = 'yoyo'
m = d + x
n = d * 3
print(f"Value of variable d is : {d}")
print(f"Data type of vriable d is : {type(d)}")
print(f"Value of variable g is : {g}")
print(f"Data type of vriable g = len(d) is : {type(g)}")
print(f"Value of variable h is : {h}")
print(f"Data type of vriable h is : {type(h)}")
print(f"Value of variable i is : {i}")
print(f"Data type of vriable i = len(h) is : {type(i)}")
print(f"Data type of j converted to int : {type(l)}")
print(f"Data type of j converted to float : {type(k)}")
print(f"Value of m = d + x is : {m}")
print(f"Value of n = d * 3 is : {n}")

#6)Some intersting operations on diff data types
print(9*True)#9*1 here True is conv to its int form i.e 9
print(-9.01*False)#-9.01*0 here Flase is conv to its int form i.e 0 
print("yoyo"*False,type("yoyo"*False),len("yoyo"*False))#returns empty string and <class 'str'>
print(True+False) #arithmetic operation on booleans
print(True+True)
print(False+False)
