>>> string = "Hi! My name is {name} and I live in {state}." # create a string with placeholders for content, but unlike before I'm putting something inside the curly braces which is a key, just like a key in a key value pair in a dictionary

>>> string.format(name='Alex', state='New York') # I can use the str.format() method to assign values to the keys and return the result
'Hi! My name is Alex and I live in New York.'

>>> string.format(state='New York', name='Alex') # It doesn't matter what order I put the values in when I'm formatting because the state value will look for the state placeholder, all through the magic of matching keys
'Hi! My name is Alex and I live in New York.'

>>> my_dict = {'name': 'Alex', 'state': 'New York'} # we can also assign values by using a dictionary of key value pairs

>>> string.format(**my_dict) # by using the str.format() method and passing in ** dictionary name the format() method knows to look inside the dictionary that is passed as an argument to look for the values that align with the keys which are used as placeholders
'Hi! My name is Alex and I live in New York.'

>>> my_dict.update({'job': 'Learner'}) # extend the dictionary using the update() method to add a key value pair that isn't a placeholder in the string, just to test if it will muck things up.

>>> string.format(**my_dict) # it doesn't muck up a thing, because the string isn't using indexes (dictionaries don't have index positions) to return values it's using keys, and no matter how many key value pairs I have in the dictionary, as long as there is a key that matches the key in the placeholder it's going to work
'Hi! My name is Alex and I live in New York.'