def word_count(string):
  string = string.lower()
  string_list = string.split()
  dict_word_count = {}
  for each in string_list:
    if each in dict_word_count:
    count = 0
    dict_word_count[each] = count
    if each in dict_word_count:
      count += 1
      dict_word_count[each] = count
  return dict_word_count