>>> my_dict = {'name': 'Alex', 'age': 34, 'state': 'New York', 'country': 'USA', 'employer': 'self', 'job': 'Learner'} # create a dictionary

>>> for thing in my_dict: # for loop to iterate through the dictionary, what does it return
...   print(thing) # let's find out
...
name # it returns the keys of the dictionary, but not the values
job
state
country
employer
age

>>> for key in my_dict: # let's iterate through the dictionary again, this time calling the first part key, because we know it returns the keys 
...   print(my_dict[key]) # here we give the dictionary the key and ask for the corresponding value 
...
Alex # now we get values
Learner
New York
USA
self
34

>>> dir(my_dict) # let's get a list of the valid attributes for that object
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'] # notice that a dictionary has an attribute called 'values' which will let us access the values directly


>>> for value in my_dict.values(): # for loop again, values in this section could have been anything, but the values() method is the real key here it's going to give us access to the values of the dictionary instead of the keys it doesn't seem all that different than using keys and getting my_dict[value], but Kenneth says it's more efficient because you only query the dictionary once. I guess that makes sense. 
...   print(value)
...
Alex
Learner
New York
USA
self
34
>>>