>>> my_dict = {'name': 'Alex'} # create a dictionary

>>> my_dict[0] # you can't use indexes
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 0


>>> my_dict['name'] # you use the value pairs to pull out the values, note that you use square brackets instead of curly brackets
'Alex'

>>> my_dict
{'name': 'Alex'}

>>> my_dict = {'name': 'Alex', 'job': 'Learner'} # There's probably a better way to extend the values in a dict, like using the extend() function that we use with lists, but for the moment we're just reassigning the variable to a new dictionary

>>> my_dict['job'] # going to use a key to pull out the value
'Learner'

>>> name_dict = {'names': {'first': 'Alex', 'middle': 'Miles', 'last': 'Younger'}} # dictionary key value pairs can contain dictionaries as values ... that means stacking one dictionary inside of another dictionary

>>> name_dict
{'names': {'last': 'Younger', 'middle': 'Miles', 'first': 'Alex'}}

>>> name_dict['names']
{'last': 'Younger', 'middle': 'Miles', 'first': 'Alex'}

>>> name_dict['last'] # you can't jump to a value if the key isn't a 'top level' key. In this case the ['last'] key is under the ['names'] key so we've got to use both.
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'last'

>>> name_dict['names']['last'] # there we go, to get the 'last' key value we have to go through 'names' to find 'last'
'Younger'

>>> game_dict = {(2,2): True, (1,2): False} # dictionaries can contain lists, tuples and other dictionaries

>>> game_dict[(1,2)]
False
>>>