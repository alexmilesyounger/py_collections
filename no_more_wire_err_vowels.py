string = "Treehouse"
string_list = list(string)
vowels = list('aeiou')

for letter in vowels: 
	while letter in string_list: 
		try:
			string_list.remove('{}'.format(letter))
			print(string_list)
		except:
			continue

string = ''.join(string_list)
print(string)