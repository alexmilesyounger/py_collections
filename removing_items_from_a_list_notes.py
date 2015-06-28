>>> a_list = list('abzcd')
>>> a_list
['a', 'b', 'z', 'c', 'd']

>>> a_list.index('z') # the index() function takes a value from the list and then gives you the index position in the list for that value
2

>>> del a_list[2] # del is a keyword, not a function, that will delete things for you. In this case we're deleting the value at index 2 of the list

>>> a_list
['a', 'b', 'c', 'd']
>>> a_list.insert(2, 'z')
>>> a_list
['a', 'b', 'z', 'c', 'd']
>>> del a_list[a_list.index('z')] # here I combined the del keyword and the index() function to remove the offending value from the list without knowing its index place
>>> a_list
['a', 'b', 'c', 'd']

>>> a_string = 'Hello'
>>> del a_string # you can use del to delete a string
>>> a_string
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a_string' is not defined


>>> a_num = 1
>>> del a_num # you can use del to delete a number
>>> a_num
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a_num' is not defined


>>> a_string = "Helllo"
>>> del a_string[2] # you can't use del to delete items from a string based on their index, because in Python strings are immutable, unlike lists which are mutable. This just means we can't change them directly.
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
# TypeError: 'str' object doesn't support item deletion


>>> my_list = [1, 2, 3, 1]
>>> my_list.remove(1) # the remove() function works similarly to the del keyword, but let's use remove items from a list the same way that we insert() them. remove() only takes one argument, the value which it should look for to remove from the list. Also, remove is a sub-function of the list() function. So to look up info on it I had to use help(list.remove)
>>> my_list
[2, 3, 1]
>>> my_list.remove(1) # remove() will remove the first instance of the value it's looking for
>>> my_list
[2, 3]
>>> my_list.remove(1) # when the list doesn't contain any of the values that remove is looking for it throws an exception. That means we can use while loops and try/except to delete all of the values from a list
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
