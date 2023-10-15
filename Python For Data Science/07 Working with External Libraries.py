'''
Working with External Libraries
1)Imports
2)Other import syntax
3)Submodules
4)Objects
5)3 tools for understanding strange objects : type(), dir(), help()
6)Operator overloading
7)Why 1+1 != 2 ?
'''

# 1)Imports
'''
vast number of libraries can be added accessed using import
A module is just a collection of variables (a namespace, if you like) defined by someone else. 
We can see all the names in module using the built-in function dir().
We can access these variables using dot syntax.
'''
import math
print("It's math! It has type {}".format(type(math)))#math is a module
print(dir(math))
print("pi to 4 significant digits = {:.4}".format(math.pi))
print('log(32,2) =',math.log(32,2))
'''
hlep()
log(...)
log(x, [base=math.e])
Return the logarithm of x to the given base.
'''

# 2)Other import syntax
'''
we'll be using functions in math frequently we can import it under a shorter alias to save some typing 
(though in this case "math" is already pretty short)
import math as mt
or
import math
mt = math
print(mt.pi)

what if we could refer to all the variables in the math modul by themselves?
i.e just pi instead of math.pi or mt.pi
We can do that by :

from math import *
print(pi,log(32, 2))

import * makes all the module's variables directly accessible!
without dotted prefix

from math import *
from numpy import *
print(pi, log(32,2)) -> gives error as both math and numpy have log function with different semantics.

we can resolve above error by importing specific libraries
from math import log, pi
from numpy import asarray
'''

# 3)Submodules
'''
Modules contain variables which can refer to functions or values
They can also have variables referring to other modules.
'''
import numpy
print("numpy.random is a",type(numpy.random))
print("it contaings names such as ...","dir(numpy.random)[-15:]")
rolls = numpy.random.randint(low=1, high=6, size=10)
print(rolls)

# 4)Objects
'''
libraries also define their own types which we'll learn to work with.
'''

# 5)3 tools for understanding strange objects : type(), dir(), help()
'''
type()->what's this thing?
dir()->what can I do with it?
help()->tell me more
'''
print(type(rolls))
print(dir(rolls))
print(rolls.mean())#average of roll
print(rolls.tolist())#turn the array into a list
#help(rolls.ravel)

# 6)Operator overloading
'''
a single operator performs different operation!
print([1,2,3,4,5,6]+10)->gives an error
the list does not support the + with integer
while the numpy array supports the + with integer
print(rolls+10)
'''
print(rolls+10)
print(rolls<=3)
xlist = [[1,2,3],[2,3,6]]
x = numpy.asarray(xlist)
print("xlist = {}\nx =\n{}".format(xlist, x))
print(x[1,-1])
#print(xlist[1,-1])-> gives an error

# 7)Why 1+1 != 2 ?
'''
tensorflow is a Python Library popularly used for deep learning
makes extensive use of operator overloading!
'''
import tensorflow as tf
num1 = tf.constant(1)
num2 = tf.constant(1)
print(num1 + num2)
'''
num1 + num2 is not equal to 2
It does not hold the values of that operation's output, 
but instead provides a means of computing those values in a TensorFlow tf.Session.

When Python programmers want to define how operators behave on their types, they do so by implementing methods 
with special names beginning and ending with 2 underscores such as __lt__, __setattr__, or __contains__. Generally, 
names that follow this double-underscore format have a special meaning to Python.
So, for example, the expression x in [1, 2, 3] is actually calling the list method __contains__ behind-the-scenes.
It's equivalent to (the much uglier) [1, 2, 3].__contains__(x)

'''
