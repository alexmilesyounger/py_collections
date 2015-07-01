>>> my_tuple = (1, 2, 3) # create a tuple by assigning it to a variable, and placing the values in parenthesis and separating them with commas
>>> my_tuple
(1, 2, 3)

>>> my_second_tuple = 1, 2, 3 # however, the most important part of the tuple is the comma. Using a comma or multiple commas will create a tuple. The parenthesis aren't required. They're used in output display to help keep them distinct looking from lists and dictionaries, but they're not required. It helps to create them using parenthesis just because it helps with human readability, but the parenthesis are not necessary. I feel like this is a huge point that I really need to drive home to myself. Why? Because if I put commas into my code and I'm not paying attention I may inadvertently create a tuple. 
>>> my_second_tuple
(1, 2, 3)

>>> my_third_tuple = tuple([1,2,3]) # you can also create a tuple using the tuple() method, but you've got to give it something iterable to work over (in this case a list). This means I could lock down a list by creating a tuple version of it, and that's useful, but if i'm starting from scratch this is a harder way to type it all out. I think I'm most likely to go with solution number one (or zero if I'm counting like a programmer) above for creating tuples.
>>> my_third_tuple
(1, 2, 3)

>>> my_third_tuple[1] # we can access values using indexes, and with tuples the index will never change. 
2

>>> my_third_tuple[1] = 5 # tuples are immutable, which means we can't reassign any values in them. 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment


>>> dir(tuple) # when we take a look at the supported pieces of the tuple, all that's really of interest to me at the moment is the 'count' and 'index' which are not new. Note to self, this is why (maybe) the language writers Guido & co. put __ before and after some of the (classes?) that are baked in. Those __ help to show what's used to build the thing vs. what the thing can do. I think I'm reading that right. 
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>>