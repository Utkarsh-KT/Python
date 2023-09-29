'''
Functions & Getting Help
1)Introduction & Getting help
2)Common pitfall
3)Defining Functions
4)Docstrings
5)Functions that don't return & side effects
6)Default arguments
7)Functions Applied to Functions
'''
# 1)Introduction & Getting help()
'''
Python has many built in function's like : print, abs, round, min, max, etc;
Besides this we can declare are own functions.
help()- is a built in function used to understand usecase other built in functions.

help(round)

'''
'''
help() displays two things:
1- the header of that function round(number, ndigits=None).In this case, this tells us that round() takes an argument we can describe as number.
Additionally, we can optionally give a separate argument which could be described as ndigits.
2- A brief English description of what the function does.
'''

# 2)Common pitfall while using help()
'''
Pass only the name of function & not the result/parameters
Python evaluates an expression from inside to outside hence it will calculate the output and then,
it will provide help on that output.

help(round(-3.69))

'''
'''
help() can also deal with functions with complex docstrings like print()

help(print)

'''
'''
by reading the docstrings of print() we are introduced with sep argument,
print(' ',sep=' ')
'''
print('Apple','Mango','Orange')#it will print strings only with indentation
print('Apple','Mango','Orange.',sep=', ')#it will print strings with , in between them

# 3)Defining Functions
'''
def funct_name(parameter1,parameter2,...,parametern) : ->creates a function with n arguments
there is code block after :-> this is executed only when function is called
return -> functions is exited immediately & passes the value on the rhs to calling context
You can use help(least_diff) to understand about this function

help(least_diff)

python can't give docstrings of user defined functions, we need to explicitly write descriptions
i.e docstrings for these functions.
'''
def least_diff(a,b,c):
    diff1 = abs(a-b)
    diff2 = abs(a-c)
    diff3 = abs(c-b)
    return min(diff1,diff2,diff3)
print(least_diff(3,6,9),least_diff(4,8,12),least_diff(5,10,15))

# 4)Docstrings
'''
The docstring is a triple-quoted string (which may span multiple lines) 
that comes immediately after the header of a function.
'''
def sq_num(num) :
    '''
    Returns the square of the number passed as parameter in the function.
    
    >>> sq_num(3)
    9
    '''
    return num**2
print('3^2 =',sq_num(3))
'''
help(sq_num)
calling help(sq_num) then it will show docstrings of fuction sq_num
docstrings contains example which is not executed to python.
example calls in function docstrings is universally observed and very effective at helping other
understand use case of function.
'''

# 5)Functions that don't return & side effects
'''
Python allows us to define functions that dont return anything.
The result of calling them is a special value None
'''
def add_two_num(a,b) :
    c = a + b
print(add_two_num(3,6))
'''
without return statement function is completely pointless,
but function with side effects does something uselful without returning anything.
for example print(), help(), etc does not return anything.
'''
side_effects_print = print()
print(side_effects_print)
def add_two_num_print(a,b):#we can excute function with no return statement in following way.
    c = a + b
    print(c)
    
# 6)Default arguments
'''
Function have few arguments by default,
even when we don't pass them they execute their default value
This is applicable in built in function and also in user defined function.
'''
print(3,6,9)#default value of arg sep is ' '
print(3,6,9,sep=' < ')#when we specify value of arg sep as ' < ' then it executes that value.
def greet(name='DRAKE'):
    print('Hello, ',name,'!',sep='')
greet()#executes default value of argument name
greet(name="World")#set value of argument name  as world

# 7)Functions Applied to Functions
'''
Calling a function inside another function as an argument.
Functions that operate on other functions are called "higher-order functions."
here mult_by_three() , call() are called higher-order functions
'''
def mult_by_three(arg1):
    return 3 * arg1
def call(func1,arg2):
    return func1(arg2)
def sq_of_call(func2,arg3):
    return func2(func2(arg3))
print('mult_by_three(1) = 3 * 1 =',mult_by_three(1))
print('call(mult_by_three,1) = (value of mult_by_three) * 1 = 3 * 1 =',call(mult_by_three,1))
print('sq_call(mult_by_three,1) = (value of mult_by_three) * (value of mult_by_three) * 1 = 3 * 3 * 1 =',sq_of_call(mult_by_three,1))
'''
There are higher-order functions built into Python
Consider the example :
By default, max returns the largest of its arguments. 
But if we pass in a function using the optional key argument, 
it returns the argument x that maximizes key(x) (aka the 'argmax').
'''
def modu_5(x) :
    return x%5 
print('Biggest num :',max(6,3,9))
print('Biggest num of modulo 5 :',max(6,3,9,key=modu_5))#returns 9 as remainder after dividing with 5 is largest
