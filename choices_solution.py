import random

def nchoices(iterable, integer):
  list_of_random_items = []
  while len(list_of_random_items) < integer: # less than, not less than or equal to because the len starts counting from 0 and the integer isn't including the 0
    list_of_random_items.append(random.choice(iterable))
  return list_of_random_items