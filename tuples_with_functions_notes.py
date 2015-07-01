>>> my_alphabet_list = list('abcdefghijklmnopqrstuvwxyz')
>>> count = 0 # it used to be that I had to use a counter variable to keep track of my progress stepping through some sort of data collection
>>> for letter in my_alphabet_list:
...   print('{}: {}'.format(count, letter))
...   count += 1
...
0: a
1: b
2: c
3: d
4: e
5: f
6: g
7: h
8: i
9: j
10: k
11: l
12: m
13: n
14: o
15: p
16: q
17: r
18: s
19: t
20: u
21: v
22: w
23: x
24: y
25: z

>>> for index, letter in enumerate(my_alphabet_list): # with enumerate() we can just get the index of the item automatically
...   print('{}: {}'.format(index, letter))
0: a
1: b
2: c
3: d
4: e
5: f
6: g
7: h
8: i
9: j
10: k
11: l
12: m
13: n
14: o
15: p
16: q
17: r
18: s
19: t
20: u
21: v
22: w
23: x
24: y
25: z

>>> for step in enumerate(my_alphabet_list): # I'm a little less clear here, but I think that we can say X in enumerate() and then since the values returned are index and value we just use two value returns, like the first one the index has an index of 0 and the value associated with that index has an index of 1. This seems confusing since I'm trying to get the index of a value as a value. 
...   print('{}: {}'.format(step[0], step[1])) 
...
0: a
1: b
2: c
3: d
4: e
5: f
6: g
7: h
8: i
9: j
10: k
11: l
12: m
13: n
14: o
15: p
16: q
17: r
18: s
19: t
20: u
21: v
22: w
23: x
24: y
25: z


>>> for step in enumerate(my_alphabet_list):
...   print('{}: {}'.format(*step)) # here we can access all of the things in a tuple by using one asterik, two for dicts and one for tuples
...
0: a
1: b
2: c
3: d
4: e
5: f
6: g
7: h
8: i
9: j
10: k
11: l
12: m
13: n
14: o
15: p
16: q
17: r
18: s
19: t
20: u
21: v
22: w
23: x
24: y
25: z
>>> my_dict = {'name': 'Alex', 'job': 'Learner', 'employer': 'self'}


>>> for key, value in my_dict.items(): # we can use key, value to get at the values and keys in a dictionary as long as we use the items() method of the dictionary
...   print('{}: {}'.format(key.title(), value))
...
Employer: self
Name: Alex
Job: Learner
>>>