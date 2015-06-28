shopping_list = []


def show_help():
	print("\nSeparate each item with a comma.")
	print("Type DONE to quit, SHOW to see the current list, and HELP to get this message.")

def show_list():
	count = 1
	for item in shopping_list:
		print("{}: {}".format(count, item))
		count += 1

print("Give me a list of things you want to shop for.")
show_help()

while True:
	new_stuff = input("> ")

	if new_stuff == 'DONE':
		print("\nHere's your list:")
		show_list()
		break
	elif new_stuff == 'HELP':
		show_help()
		continue
	elif new_stuff == 'SHOW':
		show_list()
		continue
	else:
		new_list = new_stuff.split(',') # shouldn't this be new_list = list(new_stuff.split(', ')) ? Don't we need the list() function and don't we want to include the space after the comma so that the split() function doesn't start each list item with a space before it?
		index = input("Add this a certain spot? Please enter for the end of the list, " # we're breaking the string just by closing the quotes and moving to the next line. It appears that the two strings will automatically be concatenated. Don't forget to add spaces to the strings when you do this.
			"or give me a number. Currently {} items in the list.".format(len(shopping_list))) # He's making this shopping_list but I think it should be new_list because he hasn't assigned anything to shopping_list yet. The only list we actually have is the new_list from splitting the new_stuff string. 
		if index:
			
			try: 
				spot = int(index) - 1 

				for item in new_list:
				shopping_list.insert(spot, item.strip()) # here's where we're making up for not including a space with the comma delimeter in the split() function on line 31. The strip() function will remove any white spaces around the item. I wonder if it will also remove white space from within an item. Like will it remove the space between a multi word answer like "dog food." Nope, I just checked it in the shell and it only touches whitespace on the outsides of the item (before and after)
				spot += 1
			
			except:
				print("That's not a number.")
			
		else:
			for item in new_list():
				shopping_list.append(item.strip())
