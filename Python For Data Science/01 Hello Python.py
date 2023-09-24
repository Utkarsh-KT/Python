'''
Hello Python
1) Introduction
2) Hello Python!
3) Variable Assignments & Reassignments
4) Function calls
5) Comments, Conditions & Strings
6) Numbers & Arithmetic in Python
7) Order of operations
8) Built-in Functions for working with numbers
'''

# 1)Introduction
'''
Python was named for the British comedy troupe Monty Python.
Python was developed by Guido van Rossum in the year 1991.
Following are few key features of Python:
Easy to Learn, powerful & versatile, free & open-source,
large community of users & developers, interpreted language(does not need to be compiled before run),
Dynamically typed language(donot need to declare the type of variable), oop language,
large standard library.
'''

# 2) Hello Python!
'''
There are a lot of concepts in the code below which will covered in individual topics below!
'''
msg = 'But I am a beginner!'
exp = 0 
print(exp ,msg)
exp = exp + 4
if exp > 0  :
    msg = "But I am not a beginner!"
    print(exp,msg)

popup = 'Exp'*exp
print(popup)

# 3) Variable Assignments & Reassignments
'''
variable_name = value
= is assignment operator
Unlike other languages in python we don't do following :
declare before assigning
refer data type while assigning
Example : 
exp = 0
assignment operators works from RHS to LHS
variable name can begin with alphabet or _ and later contain numbers only
'''
var1 = 36 #var1 is assign with 36
print(f'var1 = {var1}')
var1 = var1 + 36
print('Updated value of var1 = {}'.format(var1))

# 4) Function calls
'''
Function call is statement in which the function is been revoked!
Usually function call involves function name with parameters inside parentheses
example : print()
'''
var2 = 63
print('var2 = {}'.format(var2))#calling function named print

# 5) Comments, Conditions & Strings
#single line
'''single line'''
"""Single line"""
'''Multi 
line
'''
"""Multi
Line
"""
'''
Conditional statements only execute if condition is satisfied
if exp > 0 :
here statement inside if block will execute only if exp is > 0 is True
'''
if var2>60:# : Indicates new code block
    print("Condition Satisfied!")
print("Outiside if code block!")# this is outside 
#strings declared inside ' ' or " "
#char declared inside ' ' 
laugh = "Heee"*3 #multiplying a str with num repeats the str num times
print(laugh)
greet = 'Hii! ' + laugh
print(greet)
#* & + can be used for other purpose rather than multiplication or addition this is operator overloading

# 6) Numbers & Arithmetic in Python
'''
Data types like int & floats comes under the category of numbers
'''
var3 = 9
print(f"var3 = {var3} , data type of var3 is {type(var3)}")
var4 = -9.36
print(f"var4 = {var4} , data type of var4 is {type(var4)}")
'''
Python has following arithmetic operators:
+,-,*,/,//,%,**,-var
'''
print(f'3+6 = {3+6}')#addition
print(f'3-6 = {3-6}')#substraction
print(f'3*6 = {3*6}')#multiplication
print(f'3/6 = {3/6}')#division
print(f'3//6 = {3//6}')#floor division
print(f'3%6 = {3%6}')#modulas
print(f'3**6 = {3**6}')#exponentiation
print(f'-9+3*6 = {-9+3*6}')#negation

# 7) Order of operations
'''
PEMDAS - Parentheses, Exponents, Multiplication/Division, Addition/Substraction
Python follow this rules which give order for operations.
'''
print('6-3+9 =',6-3+9)#either add or substract does not matter
print('-3+6*9 =',-3+6*9)#implements first multiplication then add in -3
print('(-3+6)*9 =',(-3+6)*9)#implements first parentheses then multiplies
# 8) Built-in Functions for working with numbers
'''
Functions which are defined already we only have to call them to use.
example : min(), max(), abs(), float(), int(), print()
'''
print('min(6,3,-9) =',min(6,3,-9))
print('max(-6,-1,-3) =',max(-6,-1,-3))
print('abs(369) =',abs(369))
print('abs(-369) =',abs(-369))
print('float(-9) =',float(-9))
print('int(3.69) =',int(3.69))
print('int(\'36\')+9 =',int('36')+9)
