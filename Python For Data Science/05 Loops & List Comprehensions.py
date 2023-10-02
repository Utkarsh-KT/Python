'''
Loops & List Comprehensions
1)Introduction to Loops
2)for loops
3)range()
4)while loops
5)List Comprehensions
6)Something Special
'''

# 1)Introduction to Loops
'''
Loops help to do repeated work/ iterate
'''
Stud_names = ['abc','xyz','def','uvw']
print('Stud_names =',Stud_names)
print('Stud_names =',end=" ")
for elem in Stud_names:
    print(elem, end=' ')
print()

# 2)for loops
'''
for loop consist of 3 things
elem to iterate , in , set of values
these set of values can be any data structure which supports iterations!
example : lists, tuples, strings, dictonary, etc.
'''
transcation_amt = (3,9,6,12)
net_amt = 0
for trans in transcation_amt:#example of iteration in tuple
     net_amt += trans
print('net_amt =',net_amt)

letter = 'Hii I am Ignlo Bigger I am The Cooler is Hamm :)'
for char in letter:
    if char.isupper():
        print(char, end=' ')
print()

# 3)range()
'''
range() returns a sequence of numbers!
'''
print('First 5 whole numbers : ',end=' ')
for i in range(5):
    print(i,end=' ')
print()
   
# 4)while loops
'''
Loop runs/iterates until some condition is met
while loop is evaluated as a boolean statement, 
and the loop is executed until the statement evaluates to False
'''
iter = 0
while iter<10:
    print(iter,end=' ')
    iter += 1
print()

# 5)List Comprehensions
'''
List Comprehension helps us using loops inside the list
'''
sqrs = [n**2 for n in range(11)]#by using List Comprehensions
print(sqrs)
sqrs = []
for n in range(11):
    sqrs.append(n**2)#without using List Comprehension
print(sqrs)
Stud_names = ['abc','xyz','def','uvw','ghij','qrst']
#Just like SQL, you might think of this as being like a "WHERE" clause
Big_Stud_names = [elem for elem in Stud_names if len(elem)>3]#we can also add an if condition!
print(Big_Stud_names)
Shor_Stud_Upper_names = [ name.upper() + '!' for name in Stud_names if len(name)<4]#using List Comprehensions with if conditions for transforming
print(Shor_Stud_Upper_names)
'''
these three lines as SELECT, FROM, and WHERE
structure is clearer when it's split up over 3 lines
Shor_Stud_Upper_names = [ 
                        name.upper() + '!'
                        for name in Stud_names 
                        if len(name)<4
                        ]
'''
test_list = [3 for name in Stud_names]
print(test_list)
'''
List Comprehensions when combined with functions like min, max, sum give intresting one line solutions 
for problems which may take multiple lines
consider following two examples
'''
nos = [-3,9,12,0,-6,-9]
def count_neg(nums):
    neg = 0 
    for no in nums :
        if no<0:
            neg += 1
    return neg
def count_neg_list_comp(nums):
    return len([no for no in nums if no<0])
def count_neg_list_comp_sum(nums):
    return sum([no<0 for no in nums])#Python calculates booleans and implicitly to int
print(count_neg(nos))
print(count_neg_list_comp(nos))
print(count_neg_list_comp_sum(nos))
'''
Which of these solutions is the "best" is entirely subjective. 
Solving a problem with less code is always nice, 
but it's worth keeping in mind the following lines from The Zen of Python:
Readability counts.
Explicit is better than implicit.
'''

# 6) Something Special
'''
return True if list has atleast one elem divisible by 7
else return False!
'''
def Lucky(nums):
    return any([num%7==0 for num in nums])
list1 = [17,7,35,3,6,9]
list2 = [17,27,37,47,57,67]
print(Lucky(list1))
print(Lucky(list2))
'''
Return a list with True or False values depending upon input values have elem greater than given elem
'''
def elemwise_greater_than(L,thresh):
    return [i>thresh for i in L]#returns a list with boolean values
print(elemwise_greater_than(list1,21))