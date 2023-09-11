'''
Functions
1)Introduction : Simple example
2)Header
3)Body
4)Calling
5)Naming
6)Example : complex example
7)Variable : Scope
8)Functions with multiple arguments
9)Functions with no arguments
'''

import math

#1)Introduction : Simple
'''
Functions helps to organize code,
Block of code designed to perform specific task,
Perform calculations without duplications.
'''
#Functions contains head and body
#def->tell we are about to define function in python
#add_three->name of function
#(input_var)-> function's argument-'name of variable the function will use
#return->keyword that tell we are about to exit the function
#output_var-> value that is returned when function is exited
def add_three(input_var):#header-specifies name of function and its arguments
    output_var = input_var + 3
    return output_var

#2)Header
'''
Defines name of function and its argument/s
begins with def
then name
then argument
function can also have no arguments or have multiple args
followed by :
def function_name (args/no args) :
'''

#3)Body
'''
Specifies the work that the function does
four spaces indentation in body
works from top to bottom
this does not run the func
example of body
    output_var = input_var + 3
    return output_var
'''

#4)Calling
'''
Running function == calling
In general independent of any programming language functions are 
written as func_name()->just differentiate functions from variables
even if there are args we don't write them while documentioing
'''
var = add_three(6)#run function
#set value of this variable var to the output we get when we run the function with 6 as input
print(var)#check that the value is 9 as expected

#5)Naming
'''
Must start with _ or alphabet
can only have numbers , alphabet and _
generally-> lowercase_other_words_sep_by_underscore()
'''

#6)Example : complex
'''
Function to calculate salary based on number of hours worked,
her tax is 12% and $15/hr is base salary
get full time pay & part time pay
'''
def get_pay(num_hours):
    pay_pertax = num_hours*15
    pay_aftertax = pay_pertax*(1-0.12)
    return pay_aftertax
Net_Pay = get_pay(40)
Part_Pay = get_pay(30)
print(Part_Pay)
print(Net_Pay)

#7)Variable : Scope
'''
Variable Scope is the part of code where its accessible
Variable declared inside the function are accessible only inside the function local
Variables declared outside the function are accessible globaly
'''
def sample_func(x):
    y = 3*x
    print('Returning val of y :',end=" ")
    return y
z = sample_func(6)
print(z)
#print(x) this statement will produce error as we are accessing the local variable outside its scope

#8)Functions with multiple arguments
'''
To define function with multiple arguments we just need to add more args
seperated by comma inside function head!
'''
def multi_imput(l,b,h):
    vol = l*b*h
    return vol
vol = multi_imput(3,6,9)#this is global vol
print(vol)#here multi_input() will store local vol value in global vol

#9)Functions with no arguments
'''
Such functions have no return statement
'''
def print_greetings():
    print("Hello Sir!")
    print("Good Evening!")

print_greetings()

#We can include one function inside another
def round_division(num1,num2):
    print("Without rounding off num1/num2 =",num1/num2)
    print("With rounding off num1/num2 =",math.ceil(num1/num2))#using mat.ceil() rounding off function inside another function
    
round_division(5,2)
print(round(2.6))

'''
When coding we should aim to write as little as possible,
coz each line increases the probability of getting errors!
'''
