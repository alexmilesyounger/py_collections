>>> my_list = list('12abcd567fgh89j') # create a mixed list
>>> my_list
['1', '2', 'a', 'b', 'c', 'd', '5', '6', '7', 'f', 'g', 'h', '8', '9', 'j']

>>> my_list[:2] # slice the first two numbers
['1', '2']
>>> del my_list[:2] # delete the first two iterables using the del keyword and a slice
>>> my_list
['a', 'b', 'c', 'd', '5', '6', '7', 'f', 'g', 'h', '8', '9', 'j']

>>> my_list[4:7] = list('ef') # replace a slice by assigning a new list to those index positions
>>> my_list
['a', 'b', 'c', 'd', 'e', 'f', 'f', 'g', 'h', '8', '9', 'j']

>>> my_list.index('f') # find the index position of the first 'f' value
5
>>> my_list.remove('f') # use the remove() function to remove the first instance of 'f'
>>> my_list
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', '8', '9', 'j']

>>> my_list[8:10] = list('i') # replace a slice by assigning those index positions to a new list (note: the list we assign to those index positions doesn't need to match the number of values that the slice had i.e. we can insert more values or fewer). 
>>> my_list
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
