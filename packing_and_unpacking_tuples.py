>>> a, b = 1, 2 # we can assign values to mutiple variables using tuples

>>> a
1
>>> b
2


>>> a = 4 # and when variables are assigned values in this way (using tuples) it doesn't mean that we are just accessing tuples... they're standalone values. That means they're mutable. I tested here to see if I could reassign 'a' to another value. I can, so that means it's not just returning a value from a tuple. Tuples are immutable so if this was a tuples I shouldn't have been able to change a. 
>>> a
4
>>> a = 1 # ok, reset a back to where it was for the exercise. 

>>> c = (3, 4) # that said, I can also create a tuple and assign it to a variable.
>>> c # this really is an immutable tuple
(3, 4)

>>> d, e = c # but! and this is wild. I can use the values in the tuple and assign them to new variables, which are in turn mutable. 
>>> d
3
>>> e
4

>>> f = d, e # I can also use those variables I created and assigned values to from the tuple, and turn them back into a tuple. Or for that matter, I could take any two variables (or more) and use this form of packing and unpacking to create a new variable that is a tuple compossed of the other variable. Really, this is blowing my mind a bit. 
>>> f
(3, 4)

>>> f == c # we can check to see if this new tuple is equivalent to the previous tuple we created and it is. 
True

>>> del a
>>> del b
>>> a = 1
>>> b = 2
>>> a, b = b, a # this is the wild part and a bit huge. In other languages to swap the values of two variables, you've got to use a container variable (ex. 'c') that holds one value while you do the first swap, and swaps in that first value during the second swap. It's like trying take a glass of oj and a glass of milk and swap the glasses they're in without hurting the liquids. You need a glass in the middle to do the trade off. WELL, NOT IN PYTHON. Here we can use tuple packing and unpacking to just swap the two like we did above. a is set to b and be is set to a and because (I'm guessing here) we're doing it at the same time it works... or maybe there's a hidden glass that I don't see which is the tuple. Still, it's quick, cool, and straightforward. 
>>> b
1
>>> a
2

>>> def my_func(): # define a function that returns a tuple
...   return 1, 2, 3
...
>>> my_func()
(1, 2, 3)

>>> tup = my_func() # assign a variable to the returned tuple
>>> tup
(1, 2, 3)

>>> x, y, z = my_func() # assign multiple variables to the returned tuple, each one getting it's own value. 
>>> x
1
>>> y
2
>>> z
3
>>>