state_names = ["Alabama", "California", "Oklahoma", "Florida"]
vowels = list('aeiou')
output = []

for state in state_names:
	state_list = list(state.lower()) # create a list of all the letters in the state name, and then convert the letters to lowercase

	for vowel in vowels:
		while True:
			try:
				state_list.remove(vowel)
			except:
				break

	output.append(''.join(state_list).capitalize()) # Capitalize the first letter in the state list and join the state_list back into a state name and then append that state name to the list named output

print(output)