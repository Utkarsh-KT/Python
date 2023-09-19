'''
Introduction to Lists
1)Intoduction
2)Motivation
3)Lists
4)Length
5)Indexing
6)Slicing
7)Removing items
8)Add items
9)Lists are not just for strings
'''

# 1)Intoduction
'''
We need a way to organize the data to work with it efficiently.
Python has many data structures available for holding data like
lists, sets, dictionaries, tuples.
Here we will explore lists 
'''

# 2)Motivation
'''
Consider a task in which you need to store the names of the flower species in the data.
Here if we use string then it wouldn't be efficient. Hence we use lists.
Lists created using [,] (items seperated by ,)
Here item can be string, int, float, etc.

'''
flowers_str = 'pink primrose,hard-leaved pocket orchid,canterbury bells,sweet pea'
print(type(flowers_str))
print(flowers_str)
 
flowers_list = ['pink primrose','hard-leaved pocket orchid','canterbury bells','sweet pea']
print(type(flowers_list))
print(flowers_list)
'''
list are different from strings as there are lot of tasks that we can do more easily with list like :
get an item a specified position
check the number of items 
add & remove item
'''

# 3)Lists
'''
List are mutable(updateable), elements in list are stored in specific order,
can contain any data type even including other lists.
'''
list1 = [123,123.010,True,'$','abcd']
print(type(list1))
print(list1)

# 4)Length
'''
We can count number of entries in any list with len()
'''
print(len(flowers_list))

# 5)Indexing
'''
Indexing : We can refer to any item in the list according to its position in the list.
Python uses zero-based indexing which means first item has index 0, next 1 and so on
final item will have index equal to length - 1.
'''
print('First Entry :',flowers_list[0])
print('Second Entry :',flowers_list[1])
print('Last Entry :',flowers_list[3])
'''
To print multiple things in Python with a single command 
we need only separate them with a comma.
'''

# 6)Slicing
'''
To remove a segment of a list we use slicing.
To pull first x entries we use [:x],
To pull last y entries we use [-y:].
list_name[start:end:step]
'''
print('First two entries :',flowers_list[:2])#prints elem of index 0,1
print('Final two entries :',flowers_list[-2:])#prints elem of index -1,-2
'''
When we slice list it returns shortened lists.
Negative indexing start from last elem with index -1 upto index -(len of list)
'''

# 7)Removing items
'''
Remove an item from a list with .reomve()
put value of item in parentheses.
'''
print('list1 before removing item :',list1)
list1.remove(True)
print('list1 after removing item :',list1)

# 8)Add items
'''
Add an item to a list with .append()
put value of item in parentheses.
'''
print('list1 before appending item :',list1)
list1.append(False)
print('list1 after appending item :',list1)

# 9)Lists are not just for strings
'''
List can have items with any data type including booleans, integers, floats, etc.
Cosider a list with number of sales in shop for first week in a month.
'''
sales_list = [139, 128, 172, 139, 191, 168, 170]
print('Length of the list :',len(sales_list))#prints length of list
print('Entry at index 3 :',sales_list[3])#prints element at index 3
print('Mininum :',min(sales_list))#prints minimum element in list
print('Maximum :',max(sales_list))#prints maximum element in list
print('Total sales :',sum(sales_list))#prints the sum of all elements in list
print('Avg slaes in first 5 days :',sum(sales_list[:5])/5)#prints avg of first 5 by using slicing and divide them by 5
print('Avg slaes in last 2 days :',sum(sales_list[-2:])/2)#prints avg of last two days by using -ve indexing (-2,-1)

# 10)Split in list
'''
We can use .split() to quickly turn string into a list
consider the first string flowers_str
'''
print(flowers_str.split(","))
flowers_str_to_list = flowers_str.split(',')
print(flowers_str_to_list)

# 11)List Comprehensions
'''
List Comprehensions allows us to create a list based on the vaslues in another list.
consider the following marks_list from which we made good_marks list
'''
marks_list = [96,36,48,87,75]
good_marks = [i>=70 for i in marks_list]#each item is turned into boolean depending upon whether or not the item staisfies the condition
print(f"good_marks = {good_marks}")
per_of_good_marks = sum(good_marks)*100/5
print('Percentage of students with good marks {}'.format(per_of_good_marks))
