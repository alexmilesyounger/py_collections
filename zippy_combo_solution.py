# NO
def combo(iter1, iter2):
  list_of_tuples = []
  for step in enumerate(iter1, iter2):
    list_of_tuples.append(iter1[step], iter2[step])
  return list_of_tuples  


# NO
def combo(iter1, iter2):
  list_of_tuples = []
  for step in enumerate(iter1):
    a = *step
    print(a)
    for step in enumerate(iter2):
      b = *step
      print(b)
      list_of_tuples.append(a, b)
  return list_of_tuples 


# NO, 'list' object has no atribute 'values'
 def combo(iter1, iter2):
  list_of_tuples = []
  for value in iter1.values():
    a = value
    for value in iter2.values():
      b = value
      list_of_tuples.append(a, b)
  return list_of_tuples  

# NO, append() takes exactly one argument (2 given) 
def combo(iter1, iter2):
  list_of_tuples = []
  for value in iter1:
    a = value
    for value in iter2:
      b = value
      list_of_tuples.append(a, b)
  return list_of_tuples  

# NO, iterated through a too many times
def combo(iter1, iter2):
  list_of_tuples = []
  for value in iter1:
    a = value
    for value in iter2:
      b = value
      temp_tuple = (a, b)
      list_of_tuples.append(temp_tuple)
  return list_of_tuples  

# NOT YET
def combo(iter1, iter2):
  list_of_tuples = []
  for value1 in iter1 and value2 in iter2:
    a = value1
    b = value2
    temp_tuple = (a, b)
    list_of_tuples.append(temp_tuple)
  return list_of_tuples  