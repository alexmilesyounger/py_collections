def word_count(string): 
	string = string.lower() # convert the string to lowercase using the lower() method
	string_list = string.split() # create a list by spliting the string using the split() method
	word_count_dict = {} # create an empty dictionary
	for each in string_list: # run a for loop on the string list
		if each in word_count_dict: # if the word in the string list is already in the dictionary
			word_count_dict[each] += 1 # then increment it's value by one
		else: # otherwise
			word_count_dict[each] = 1 # initialize it's value to one (and put the word in the dictionary i.e. create a key value pair)
	return word_count_dict # return the dictionary