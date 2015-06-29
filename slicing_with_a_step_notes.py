>>> my_list = list(range(20))
>>> my_list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

>>> my_list[::2] # you can use a step to move through the list at different rates, in this case I'm saying start at the begining, go to the end and move through it 2 items at a time
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

>>> my_list[2::2] # you can start at a specific index and still step through
[2, 4, 6, 8, 10, 12, 14, 16, 18]

>>> "Oklahoma"[::2] # you can step through strings as well
'Olhm'

>>> "Oklahoma"[::-1] # you can even step through backwards, by using negative numbers
'amohalkO'

>>> my_list[::-1]
[19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

>>> my_list[::-2] # you can move through the list backwards with a step of two
[19, 17, 15, 13, 11, 9, 7, 5, 3, 1]

>>> my_list[8:2:-1] # you can declare an index range and then move backwards. Note that when moving backwards you want to put the later indexes at the front of the slice notation since you're move from the end of the list to the beginning. 
[8, 7, 6, 5, 4, 3]

>>> my_list[7:1:-1] # also because you're moving backwards you start at that the index of the first argument and move to just before the second argument. This is the same behavior as moving forwards through a list, but it feels backwards because we're moving backwards
[7, 6, 5, 4, 3, 2]

>>> my_list[-1] # you can also slice into a list using negative numbers. the -1 slice will always give you the last item in the list. In this case my_list[-1] == my_list[len(my_list)]
19
>>>