>>> my_dict = {'name': 'Alex', 'job': 'Learner'} # create a dictionary

>>> my_dict
{'name': 'Alex', 'job': 'Learner'}

>>> del my_dict['job'] # use the del keyword to delete a key value pair
>>> my_dict
{'name': 'Alex'}

>>> my_dict['age'] = 34 # create a new key value pair by assigning it, note the key does not need to exist to add it in this way

>>> my_dict
{'age': 34, 'name': 'Alex'}

>>> my_dict['age'] = 35 # update a value by pulling up the key and assigning a new value

>>> my_dict
{'age': 35, 'name': 'Alex'}

>>> my_dict.update({'job': 'Learner', 'age': 34, 'state': 'New York', 'name': 'Alex Miles Younger'}) # better than assigning keys and values one pair at a time is using the update() function which will let us pass in a new dictionary with values that we want to extend into the dictionary or use to replace the old values

>>> my_dict
{'job': 'Learner', 'state': 'New York', 'age': 34, 'name': 'Alex Miles Younger'}
>>>