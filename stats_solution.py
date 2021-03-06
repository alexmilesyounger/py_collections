def most_classes(dict_of_teachers):
  max_count = 0
  count = 0
  for teacher in dict_of_teachers: # use the key, which is the teacher
    count = len(dict_of_teachers[teacher]) # set the count to the length of the values
    if count > max_count:
      max_count = count
      teacher_with_most = teacher
  return teacher_with_most

def num_teachers(dict_of_teachers):
  num_of_teachers = 0
  for teacher in dict_of_teachers:
    num_of_teachers += 1
  return num_of_teachers

def stats(dict_of_teachers):
  list_of_lists = []
  for teacher in dict_of_teachers:
    number_of_classes = len(dict_of_teachers[teacher])
    teacher_list = [teacher, number_of_classes]
    list_of_lists.append(teacher_list)
  return list_of_lists