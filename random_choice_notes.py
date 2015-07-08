>>> my_list = list(range(50)) # create a list using the range() method to auto-populate it

>>> my_list # et voila
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]

>>> import random # import the random module

>>> help(random.choice) # look up how the random.choice() method works.  It takes a sequence (with indexes) and chooses one of the items randomly.

>>> random.choice(my_list) # here we're passing my_list into random choice to tell it choose from this sequence. 
46

>>> random.choice(my_list) # random number
32

>>> random.choice(my_list) # a different random number
7

>>> random.choice([(0,1), (2,3), (4,5)]) # note that we're passing it a list, not tuple or a dictionary. That's because random.choice() needs the indexes to make it's selections
(0, 1)

>>> random.choice({'a': True, 'b': False}) # if you try passing a dictionary to the random.choice() method it will fail with a KeyError because it doesn't have an index to pull from
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/mbp/.virtualenvs/treehouse/lib/python3.4/random.py", line 256, in choice
    return seq[i]
KeyError: 1
>>>