'''
Strings & Dictionaries
1)Introductions to Strings
2)String syntax
3)Escaping
4)Strings are Sequences
5)String methods
6)Strings to lists
7)Building strings with .format()
8)Dictionaries
9)
'''

# 1)Introductions to Strings
'''
String mnipulation is key feature of python, 
python has few built in functions which support string manipulation
String is a collection of alphabets, words or other characters.
'''

# 2)String syntax
'''
Strings are defined using either single or double quotations
'''
x = 'xyz123@'
y = "xyz123@"
print(x==y)
'''
single quotes are more preferred for char.
when we use double quotes to create strings its easy to wrap single quotes in it. 
or vice versa
'''
x = 'xyz@123'
y = 'xyz@123 is "id"'
print(x,y,sep='\n')
'''
To declare multi line strings we use triple single or triple double quotes!
'''
z = '''x
y
z'''
print(z)

# 3)Escaping
'''
If we use single quotes for char in a string defined with single quotes!
then it gets confused and hence gives an error!
we need to use escape characters instead!
y = 'xyz@123 is 'id''->this will give an error
instead do as follows!
'''
y = 'xyz@123 is \'id\''#we escaped the single quotes inside the string with single quotation
print(y)
'''
following are few escape characters which are been uesd inside the strings!
\' -> '
\" -> "
\\ -> \
\n -> shift's cursor to next line
'''
print('3\\10\\23')
print("Hello\nWorld!")#print() adds and \n to line by default
print("hello",end=" ")#can manipulate default by end=' '
print("xyz")

# 4)Strings are Sequences
'''
Strings can be thought of as sequences of characters. 
Almost everything we've seen that we can do to a list, 
we can also do to a string.
'''
print(x[0])#indexing
print(y[-3:])#slicing
print(len(x))#length of string
print([char+'!' for char in y])#we can even loop over them
'''
But a major way in which they differ from lists is that they are immutable. 
We can't modify them.
cosider this example :
x[0] = '123' -> will throw an error
'''

# 5)String methods
'''
Just like list the strings have lots of useful methods!
Only few will be covered here!
'''
a = 'Hii! this an example of strin 123 A@'
print(a.upper())#.upper()
print(a.lower())#.lower()
print(a.index('this'))#.index()->searching->returns index of first elem
print(a.startswith('Hi'))#.startswith()->compares the start of string with elem start and returns True
print(a.endswith('A'))#.endswith()->compares the end of string with start of elem

# 6)Strings to lists
'''
str.split(),str.join()
str.split() turns a string into a list of smaller strings
(breaking on white space by default!)
this is super useful for breaking big strings into a list of words
'''
b = a.split()
print(b)
'''
We can aslo split on something other than whitespace by
passing values inside str.split(' ')
'''
c = 'This is huge string! Which is separated on basis of!'
d = c.split('!')
print('Separated c on basis of ! d =',d)
date = '03-10-2023'
day, month, year = date.split('-')
print(day,month,year,date)
'''
str.join() this also helps in integrating a list of strings into string
'''
e = '/'.join([day,month,year])
print(e)
'''
We can put unicode characters in our string
'''
f = '😂'.join([char.upper() for char in d])
print(f)

# 7)Building strings with .format()
'''
Joining two strings is referred to concatenation which is done by + operator
'''
print(f+', joined part!')
'''
While concatination the elem added must be string convert it by str()
'''
str1 = 'yoyo'
num = 9
str2 = 'banti'
g = str1 + str(num) + str2
print(g)
'''
other method is by using .format()
'''
h = '{}, sample example {} of formating, {}'.format(str1,num,str2)#while inserting num we didn't used str()
print(h)
'''
Here is some special use of format()
'''
percent = 99.369639
print("{} in exam is : {:.3%}".format('My',percent))
'''
format() arguments by index starts by index 0
'''
j = '''This is of index 0 {0},
This is of index 1 {1},
{1}!,
{0}!.
'''.format('YOYO','BANTI')
print(j)
'''
f"strings {}"{}
'''
i = f"YO my id is {36}"
print(i)

# 8)Dictionaries
'''
Built-in Pythong data structure for mapping keys to values
contains key : value pairs inside {}
'''
dict1 = {'one':1,'two':2,'three':3}#one, two, three are keys & 1, 2, 3 are values
print(dict1)
print(dict1['one'])#values can be accessed via square bracket syntax
dict1['six'] = 6#same syntax can help us to add and key-value pair
print(dict1)
dict1['one'] = 'first'#or even we can change value with an existing key
print(dict1)
'''
Dictonary Comprehensions syntax same as list comprehensions
list = []
dictnew = {keys: keys[0] for keys in list }
'''
stud_names = ["Yoyo","Banti","Rapper"]
stud_names_ini = {stud:stud[0] for stud in stud_names}#Dictionary Comprehensions
print(stud_names_ini)
print('Yoyo' in stud_names_ini)#in operators tells us whether key is there in dictionary or not
print('xyz' in stud_names_ini)
'''
for loop over a dictionary
'''
for i in dict1:
    print("{} = {}".format(i,dict1[i]))
'''
Accessing all the keys or all the values using dict.keys() & dict.values()
'''
print(dict1.keys())
print(dict1.values())
'''
.join() and sorted() with dictionaries
'''
print(' '.join(sorted(stud_names_ini.values())))
'''
dict.items() method lets us iterate over the keys and values of a dictionary simultaneously
'''
for key,valini in stud_names_ini.items():
    print('{} begins with \'{}\''.format(key.rjust(10), valini))

# 9)
