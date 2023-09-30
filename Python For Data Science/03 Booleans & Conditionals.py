'''
Booleans & Conditionals
1)Booleans 
2)Comparison Operations
3)Combining Boolean Values
4)Conditionals
5)Boolean Conversion
6)Something special
'''
# 1)Booleans 
'''
Data type in python which has only two possible values
True or False.
We use boolean values from boolean operators, rather putting True or False in our code directly.
'''
x = True
y = False 
print(f'x = {x}, type(x) = {type(x)}')
print(f'y = {y}, type(x) = {type(y)}')

# 2)Comparison Operations
'''
Comparison Operations : ==, !=, <, >, <=, >= 
We can combine arithmetic operators with comparison operators to represent limitless range of 
mathematical tests.
'''
def run_for_elections(age):
    return age>= 18
print('Is 19 year old Eligible : {}'.format(run_for_elections(19)))
print('Is 18 year old Eligible : {}'.format(run_for_elections(18)))
print('Is 17 year old Eligible : {}'.format(run_for_elections(17)))
print(f'3.0 == 3 is {3.0==3}')
print(f'\'3\'==3 is {"3"==3}')
def is_odd(n):
    return (n%2)==1
def is_even(n):
    return (n%2==0)
print('3 is odd :',is_odd(3))
print('2 is even :',is_even(2))

# 3)Combining Boolean Values
'''
Combining boolean values using logical operators : and, or, not
'''
def run_for_elections(age,is_citizen):
    return is_citizen and (age>=18)
print('Is 19 year old Eligible : {}'.format(run_for_elections(19,False)))
print('Is 18 year old Eligible : {}'.format(run_for_elections(18,True)))
print('Is 17 year old Eligible : {}'.format(run_for_elections(17,False)))
'''
precedence of operators : https://docs.python.org/3/reference/expressions.html#operator-precedence
consider the examples
'''
print(True or True and False)
'''
Instead of caring of precedence of operators we can simply add parentheses
consider the examples :
'''
val = (True or ((3<6)and False)or(not(True and True)))
print(val)

# 4)Conditionals
'''
Conditional statements if, else, elif 
when combined with comparison operators gives control to run over code block
'''
def pos_nev_zero(num):
    if num==0 :
        x = 'num is 0!'
    elif num>0:
        x = 'num is positive!'
    elif num<0 :
        x = 'num is negative!'
    else :
        x = 'Its not a number'
    return x
print(pos_nev_zero(3))
print(pos_nev_zero(0))
print(pos_nev_zero(-6))
'''
the conditional statements ends with :
and code block contains the indented part including tab whitespace.
the unindented line after conditional statements are excuted immediately after.
'''

# 5)Boolean Conversion
'''
just like int() converts number to int type ,float() converts number to float type,
similarly bool converts str or number to bool
'''
print(bool(1))#all non zero number are gtreated False
print(bool(0))#O is treated as False
print(bool('asf'))#all non empty strings are treated True
print(bool(''))#all empty sequences like - strings, lists, typles, dictonaries are treated as False
'''
We can use non-boolean objects in if conditions and other places where a boolean would be expected. 
Python will implicitly treat them as their corresponding boolean value
'''
if 0 :
    print(0)
elif 'YOYO' :
    print("YOYO")
else :
    print(1)
    
# 6)Something special
'''
have_umbrella or ((rain_level < 5) and have_hood) or (not (rain_level > 0 and is_workday))

have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday

T or T and T or T and T 
T or T or T
'''

''' 
def is_negative(number):
    if number < 0:
        return True
    else:
        return False

def concise_is_negative(number):
    return True if number< 0 else False
'''
