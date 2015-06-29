>>> my_string = "hello there"
>>> my_string[1:5] # slice from the start index to the position before the end index
'ello'
>>> my_string[2]
'l'

>>> my_list = list(range(1,6))
>>> my_list
[1, 2, 3, 4, 5]

>>> my_list[1:3] # get from the start index to the value before the end index. This can get tricky because indexes are still starting at 0 for counting AND the slicing is going up to, but not including the end index. 
[2, 3]

>>> my_list[2]
3

>>> my_list[0:2]
[1, 2]

>>> my_list[2:len(my_list)]
[3, 4, 5]

>>> my_list[:2] # colon at the start says start at index[0]
[1, 2]

>>> my_list[2:] # colon at the eend says go until the end of the list, whatever the last index is
[3, 4, 5]

>>> my_list[:] # colon alone says make a copy of this list
[1, 2, 3, 4, 5]

>>> my_new_list = [4, 2, 1, 3, 5]

>>> my_new_list.sort() # the sort() function will sort the list in alphanumberic order starting with the lower values at the beginning of the list

>>> my_new_list
[1, 2, 3, 4, 5]
>>> my_new_list = [4, 2, 1, 3, 5]

>>> my_sorted_list = my_new_list[:] # use the colon alone slice to create a full copy of the list. Instead of just pointing at the existing list, which would change both lists, this truely makes a copy of the list

>>> my_sorted_list
[4, 2, 1, 3, 5]
>>> my_sorted_list.sort()
>>> my_sorted_list
[1, 2, 3, 4, 5]
>>> my_new_list
[4, 2, 1, 3, 5]
>>>