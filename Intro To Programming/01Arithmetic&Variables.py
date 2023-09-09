'''
01 Arithmetic & Variables
1)Printing
2)Arithmetic
3)Comments
4)Variables
5)Debugging
'''
#1)Printing
print('Hello, World!')
print(3*6)

#2)Arithmetic
#
print("1 + 2 =",1+2)#Addition
print("2 - 1 =",2-1)#Substarction
print("2 * 3 =",2*3)#Multiplication
print("3 / 2 =",3/2)#Division
print("3**2 =",3**2)#Exponentiation

#3)Comments
'''Single line '''
"""Single line"""
'''
Multi
line
'''
"""
Multi
line
"""

#4)Variables
test_var = 4 + 5 #creating var
print('test_var =',test_var)
my_var = 3 #manupilation of variables
print('my_var =',my_var)
my_var = 100
print('my_var =',my_var)
my_var = my_var + 3
print('my_var =',my_var)
dys = 30 #using multiple variables
hrs = 24
minu = 60
sec = 60
total_secs = dys*hrs*minu*sec
print('total_secs = dys*hrs*minu*sec =',total_secs)
dys = 31
total_secs = dys*hrs*minu*sec
print('total_secs = dys*hrs*minu*sec =',total_secs)
'''
For calculating huge eqn if we use multiple variables then
its more readable hence its more effcient for debugging
'''

#5)Debugging
#logical errors
print("Addition :",2-1)
print("Addition :",2+1)

