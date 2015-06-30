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

def courses(dict_of_teachers): # doesn't work, returns a list of lists instead of a list of all the values, I need to get those nested lists to not be nested
  list_of_all_courses = []
  for value in dict_of_teachers.values():
    list_of_all_courses.append(value)
  return list_of_all_courses


def courses(dict_of_teachers): # doesn't work, trying to break apart those value lists
  list_of_all_courses = []
  for value in dict_of_teachers.values():
    temp_list = [] 
    temp_list.append(value)
    temp_string = ','.join(temp_list)
    list_of_all_courses.append(list(temp_string))
  return list_of_all_courses

def courses(dict_of_teachers): # realized the solution was just to keep looping and that I could iterate over values and that the computer would know that the values returned were iterable.
  list_of_all_courses = []
  for value in dict_of_teachers.values():
    for each in value:
      list_of_all_courses.append(each)
  return list_of_all_courses