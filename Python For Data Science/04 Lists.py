'''
Lists
1)Introduction
2)Indexing
3)Slicing
4)Changing lists
5)List Functions
6)Interlude: objects
7)List Methods
8)Searching Lists
9)Tuples
10)Something Special
'''
# 1)Introduction
'''
List in Python -> ordered sequences of values
'''
prime_one_digit = [5,3,7,2]
print(prime_one_digit)
'''
List can also contain different data types
'''
vowel = ['a','e','i','o','u']#list containing char (technical strings only :)
Students_name = ['Yoyo','Bantai','Rapper']#list containing strings
print(vowel)
print(Students_name)
'''
We can make list of lists:(2D/3d lists)
'''
menu = [
    [1,2,3],
    [4,5,6],
    [7,8,9],#comma after last elem is optional but in betn others is compalsory
        ]
menu = [ [1,2,3],[4,5,6],[7,8,9] ]#can represent list in lists in this way also
print(menu)
# 2)Indexing
'''
Can access the individual list elems using indes inside []
         0   1   2 ->positive indexing
list = ['a','b','c']
        -3  -2  -1 ->negative indexing
'''
print('prime_one_digit[0] =',prime_one_digit[0])
print('prime_one_digit[-3] =',prime_one_digit[-3])

# 3)Slicing
'''
Getting a specific part of list / cutting the list / slicing list
[Start:End:Step]
by default Start->0, End->len(list)-1, Step = 1
'''
print('vowel[0:5] =',vowel[0:5])
print('vowel[:] =',vowel[:])
print('vowel[2:4] =',vowel[2:4])
print('vowel[1:-1] =',vowel[1:-1])#prints from index 1 to index -2
print('vowel[-3:] =',vowel[-3:])#prints elem from -3 to -1

# 4)Changing lists
'''
Lists are mutable -> can be modified/ updateable
One way is to assign to an index or slice expression.
'''
Students_name[1] = 'Om Dada'
print(Students_name)
'''
To shorten the elem we can do the operation mentioned below
it shorten the elem from index[m:n] and then append remaining elem
'''
Students_name[:2] = ['Yoy','Om ','Rap']
print(Students_name)
Students_name[:] = ['Yoyo','Om Dada','Rapper']

# 5)List Functions
'''
Few useful function with lists are :
len(), sorted(), sum(), max()
'''
print(len(menu))#returns len
print(sorted(prime_one_digit))#returns sorted list
print(sorted(vowel))#returns sorted list
print(sum(prime_one_digit))#returns sum of elem in list
print(max(prime_one_digit))#returns max of elem in list
print(min(prime_one_digit))#returns min of elem in list

# 6)Interlude: objects
'''
Objects carry somethings around with them.
So that we can access stuff using Python's dot syntax
'''
x = 12
print(x.imag)#x is real number so its imaginary part is 0
c = 12 + 3j #this is complex number with real part 12 and imaginary part 3
print(c.imag)
'''
The things an object carries around can also include functions. 
A function attached to an object is called a method. 
Non-function things attached to an object, such as imag, are called attributes.
'''
print(x.bit_length)
print(x.bit_length())# passing bit_length() as object to print()
#help(x.bit_length) #we can also pass functions to the help()
'''
None of the types of objects we've looked at so far (numbers, functions, booleans)
have attributes or methods you're likely ever to use.
'''

# 7)List Methods
'''
list.append modifies a list by adding an item to the end : list_name.append(elem)
'''
Students_name.append('Code kar')
print('Before modifying -> Students_name =',Students_name)
print('After modifying  -> Students_name =',Students_name)
'''
help(list_name.append)
append is a method carried around by all objects of type list, not just Students_name, so we also could have called help(list.append). 
However, if we try to call help(append), Python will complain that no variable exists called "append". 
The "append" name only exists within lists - it doesn't exist as a standalone name like builtin functions such as max or len
'''
print('Before pop -> Students_name =',Students_name)
print('Removes last elem and returns it :',Students_name.pop())
print('After  pop -> Students_name =',Students_name)

# 8)Searching Lists
'''
To get the index of particualr elem we use list_name.index(elem)
'''
print("Index of elem 'Om Dada' is",Students_name.index('Om Dada'))
'''
Students_name.index('Code kar')
If you search an elem which is not in the list then it throws an error!
To avoid such errors we use member-Ship (in) operators!
'''
print("'Code kar' in Students_name :",'Code kar' in Students_name)
print("'Yoyo' in Students_name :",'Yoyo' in Students_name)
'''
Use following code to search an elem from list which won't throw an error!
'''
if 'Code kar' in Students_name:
    print('"Code kar" found at index :',Students_name.index('Code kar'))
else :
    print("'Code kar' is not in the list Students_name")
    
if 'Yoyo' in Students_name:
    print('"Yoyo" found at index :',Students_name.index('Yoyo'))
else :
    print("'Yoyo' is not in the list Students_name")
'''
The most interesting methods are toward the bottom of the list (append, clear, copy,etc)
'''

# 9)Tuples
'''
Tuples are almost same as lists but they differ in just two ways :
1) syntax of creating them uses parentheses instead of sqauare brackets
2) they cannot be modified! (immutable)
'''
prn_no = (123,234,345)
print(prn_no[2])
print(prn_no)
'''
prn_no[0] = 456
will give an error as they aren't mutable
Tuples are often used for functions that have multiple return values.
example : as_integer_ratio() method of float objects returns a 
numerator and a denominator  in the form of a tuple
'''
x = 0.125 
print(x.as_integer_ratio())
'''
multiple return values can be assigned individually as follows:
'''
numerator, denominator = x.as_integer_ratio()
print(numerator, denominator, numerator/denominator)
'''
swapping two variables :
'''
a = 1
b = 0
print('a =',a)
print('b =',b)
a , b = b , a
print('a =',a)
print('b =',b)

# 10)Something Special
'''
To extract an elem of multi dimensiton list which is in another list, two ways 
1)listname.pop() store that poped list and then extract the elem
2)use index list_name[m][n]
'''
menu = [ 
    [1,2,3],
    [4,5,6],
    [7,8,9] 
        ]
print(menu)
print('To print 5 from menu :',menu[1][1])
'''
lengths of list can be tricky consider the following example
'''
list1 = []
list2 = [1,2,3][1:]
print('Length of list1 :',len(list1))
print('Length of list2 :',len(list2))#list2 = [2,3] elems from index 1 to index 3-1=2
print(round(7/2))
arrivals=['Paul', 'John', 'Ringo', 'George']
name = 'Ringo'
print(arrivals.index(name))

'''
We're using lists to record people who attended our party and what order they arrived in. 
For example, the following list represents a party with 7 guests, 
in which Adela showed up first and Ford was the last to arrive:
party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
A guest is considered 'fashionably late' if they arrived after at least half of the party's guests. 
However, they must not be the very last guest (that's taking it too far). In the above example, Mona and Gilbert are the only guests who were fashionably late.
Complete the function below which takes a list of party attendees as well as a person, and tells us whether that person is fashionably late.

my solution:
def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    n = len(arrivals)
    if n%2!=0 :
        x = round(n/2)
    else :
        x = (n/2)
        
    if (name in arrivals) and (arrivals.index(name) != (n-1)) and (arrivals.index(name) >= x) :
        return True
    else :
        return False
  
modal answer:      
def fashionably_late(arrivals, name):
    order = arrivals.index(name)
    return order >= len(arrivals) / 2 and order != len(arrivals) - 1
explanation:
order >= len(arrivals) / 2:
This condition checks if the order (the position of the person in the list) 
is greater than or equal to half of the length of the arrivals list. 
order != len(arrivals) - 1: 
This condition checks if the order is not equal to len(arrivals) - 1. len(arrivals) - 1
if both True then returns True else returns False (as and operator is used)
'''