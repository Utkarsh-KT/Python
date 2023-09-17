'''
Conditions & Conditional Statements
1)Introduction
2)Conditions
3)Conditional Statements
4)if
5)if...else
6)if...elif...else
7)Example - Calculations
8)Example - Multiple elif statements
'''

#1)Introduction
'''
Sometimes we need to add few conditions when to perform a certain task
example: add_one_or_two()
consider the function which add one if input is odd or add two is input is even
'''
def add_one_or_two(var):
    if(var%2==0):#check if var is even
        return var+2
    if(var%2!=0):#check if var is odd
        return var+1
print(add_one_or_two(3))
print(add_one_or_two(4))

#2)Conditions
'''
In programming conditions are statements that are eiter True or False
Many ways to write conditions in python most common one is to compare values
We can also compare variables.
List of symbols used for comparisions:
== equals
!= does not equals
< less than
<= less than or equals to
> greater than
>= greater than or equal to

imp note-> difference between = and ==
= sets val of lhs as rhs
== checks val of lhs and rhs
'''
print(1>2,1<2)
var1 = 1
var2 = 2
print(var1>=1)
print(var2<var1)
'''
Conditions are boolean statements (statements involving comparision operators)
Conditional statements are conditions to modify how your function runs.
'''

#3)Conditional Statements
'''
Conditional statements that run certain block if condition is True
or does not run certain block if condition is False
'''

#4)if
'''
Here if temperature is greater than 38 C then it updates value of msg
or else it won't update value of msg
Here ther are two different levels of indentation 
first->for statements inside the function 
Second->for statements inside if statement
if return statement is inside if statement then it would return msg only if is True
'''
def check_fever(temp):
    msg = 'Normal Temperature. :)'
    if(temp>38):
        msg = 'Fever! `_`'
    return msg
print(check_fever(37.9))
print(check_fever(38.01))

#5)if...else
'''
To run True statements we use if statements
To run False statements we use else statements
Here statements inside else statements are also indented!
'''
def check_fever_else(temp):
    if temp>38:
        msg = 'Fever! `_`'
    else :
        msg = 'Normal Temperature. :)'
    return msg
print(check_fever_else(37.9))
print(check_fever_else(38.01))

#6)if...elif...else
'''
elif (else if) - used to check multiple if conditions
'''
def check_fever_elif(temp):
    if temp>38 :
        msg = 'Fever! `_`'
    elif temp>35 :
        msg = 'Normal Temperature. :)'
    else :
        msg = 'Low Temperature. :|'
    return msg
print(check_fever_elif(37.9))
print(check_fever_elif(38.01))
print(check_fever_elif(34))

#7)Example - Calculations
'''
Conditional statements are not only used to set values to variables but also,
used for calculations!
Example - calculate tax if income less than 12000 has 25% and above 12000 have 30%
'''
def taxes(earn):
    if earn<12000 :
        tax = earn*0.25
    else :
        tax = earn*0.30
    return tax
print("Tax on person A with income 9000 is :",taxes(9000))
print("Tax on person B with income 15000 is :",taxes(15000))
       
#8)Example - Multiple elif statements
'''
There is no limit to use elif statements consider following example:
marks obtained to pointer (only for examples purpose not accurate)
'''
def get_pointer(perc):
    if perc > 90 :
        pntr = 10 
    elif perc > 85 :
        pntr = 9 
    elif perc > 75 :
        pntr = 8 
    elif perc > 65 :
        pntr = 7
    elif perc > 55 :
        pntr = 6
    elif perc > 45 :
        pntr = 5 
    else :
        pntr = 0
    return pntr
print(f"86% is equivalent to {get_pointer(86)} pointer")
print("91% is eauivalend to {} pointer!".format(get_pointer(91)))

'''
We not always have to review every single line of code before interacting it (in built functions)
For example while studying ML we might use package 'skit-learn'
which is collection of code that we will learn without reviewing all of the codein detail
In short we might often be running code that other people have written , this is common practice for adv programmers!
'''
