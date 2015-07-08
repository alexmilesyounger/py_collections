import random

CELLS = [(0,0), (0,1), (0,2),
		 (1,0), (1,1), (1,2),
		 (2,0), (2,1), (2,2)] # it's a Python convention that if a variable is a constant (it won't ever change) it is listed in CAPS. Python doesn't care if it's  Also, we can use whitespace in Python to layout the variables the same way we'd see them in the physcial world which can really help with thinking through the logic of the game. 

def get_locations():
	monster = random.choice(CELLS)
	door = random.choice(CELLS)
	start = random.choice(CELLS)

	# if monster, door, or start are the same, try again
	if monster == door or monster == start or door == start:
		return get_locations() # by returning the function, we call the function again

	# otherwise return the variables
	return monster, door, start

def move_player(player, move): # player = (x, y)
	# get the player's current location
	x, y = player

	if move == 'LEFT':
		y -= 1
	elif move == 'RIGHT':
		y += 1
	elif move == 'UP':
		x -= 1
	elif move == 'DOWN':
		x += 1
	
	return x, y

def get_moves(player): # player = (x, y)
	moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
	
	# if player's y is 0, remove LEFT
	if player[1] == 0:
		moves.remove('LEFT')
	# if player's y is 2, remove RIGHT
	if player[1] == 2:
		moves.remove('RIGHT') 
	# if player's x is 0, remove UP
	if player[0] == 0:
		moves.remove('UP')
	# if player's x is 2, remove DOWN
	if player[0] == 2:
		moves.remove('DOWN')

	return moves

def draw_map(player):
	print(' _ _ _')
	tile = '|{}'
	for index, cell in enumerate(CELLS):
		if index in [0, 1, 3, 4, 6, 7]:
			if cell == player:
				print(tile.format('X'), end='') # you can pass an optional argument to format that tells it what kind of end to the line to use, by default it is a newline. We use an empty space here because these cells are in the left and middle of the grid and we don't want to end the line until we get to the right-hand side of the grid.
			else:
				print(tile.format('_'), end='')
		else:
			if cell == player:
				print(tile.format('X|')) # we're adding the pipe here to close the right-hand side of the grid.
			else:
				print(tile.format('_|'))

monster, door, player = get_locations() # we're assiging the three values in the function to three global functions, this time, however, we're calling the 'start' position the 'player' position

print("Welcome to THE dungeon!") 

while True:
	moves = get_moves(player)
	
	print("You're currently in room {}".format(player)) # fill in with player position
	
	draw_map(player)

	print("You can move {}".format(moves)) # fill in with available moves
	print("Enter QUIT, to quit.")

	move = input("> ")
	move = move.upper()

	if move == 'QUIT':
		break

	if move in moves:
		player = move_player(player, move)
	else: 
		print("** Walls are hard, stop walking into them! **")
		continue

	if player == door:
		print("You escaped!")
		break
	elif player == monster:
		print("You were eaten by the grue!")
		break



	# if it's a good move, change the player's position
	# if it's a bad move, don't change anything
	# if the new player position is the door, they win!
	# if the new player postion is the monster, they lose!
	# otherwise, continue
