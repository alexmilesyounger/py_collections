# notes from working in the python shell

>>> a_list = [1, 2, 3] # create a list
>>> a_list.append([4, 5]) # append to the list
>>> a_list
[1, 2, 3, [4, 5]] # it appends the list, not the individual items


>>> our_list = list(range(10)) # create a list of 10 items, using the list() function and the range() function. The range() function incldes as many items as are passed as arguments, starting with zero and going up to the number before the number entered
>>> our_list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


>>> test_list = range(10) # if I try to create a list using range() wihtout the list() function it just assigns the range(0,10) to the variable. I think I'd read in the docs that range() would create a list, but I was wrong about that (or it was a Python 2 convention that doesn't work in Python 3, more likely I was just wrong). 
>>> test_list
range(0, 10)
>>> test_list.append('a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'range' object has no attribute 'append'


>>> our_list + [10, 11, 12] # adding one list to another is how you combine lists, just like adding one string to another. Concatenating is I think the right term, because we're not really doing addition with the lists, we're just joining them. 
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
>>> our_list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # however concatenating the lists doesn't change the original lists unless you reassign them to a (new) variable.
>>> our_list = our_list + [10, 11, 12]
>>> our_list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


>>> list_1 = list(range(2))
>>> list_1
[0, 1]


>>> our_list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
>>> our_list.extend(range(13, 21)) # The extend() function is an easy way to extend a list when you don't have an existing list to concatenate onto it. The teacher, Kenneth Love, said that the extend() function (a method call) works better in scripts than concatenating with the + operator. I'm guessing because it's more explict than using the addition operator which could also be used for addition. 

# Additionally, you can also specify a start and end point while using the range() function. Again, we'll go from the first argument (which if not explicitly stated defaults to zero) to the number just before the second argument
>>> our_list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


>>> alpha = list('acdf') # using the list() function is a great way to write a list of strings where I would otherwise have to type a shitton of quotes around the strings. 
>>> alpha
['a', 'c', 'd', 'f']

>>> alpha.insert(1, 'b') # the insert() function takes two arguments, the first is the list index where the insertion will be made and the second is the value of the item being inserted
>>> alpha
['a', 'b', 'c', 'd', 'f']
>>> alpha.insert(4, 'e') # you can insert() into any place in the list. This function is useful when you want to add items to a list, but you don't want to append() them to the end of the list or don't want to extend() the list with another list. 
>>> alpha
['a', 'b', 'c', 'd', 'e', 'f']


