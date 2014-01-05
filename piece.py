t_piece = [
		[
		[0, 1, 0, 0],
		[0, 1, 1, 0],
		[0, 1, 0, 0],
		[0, 0, 0, 0],
		],
		[
		[0, 0, 0, 0],
		[1, 1, 1, 0],
		[0, 1, 0, 0],
		[0, 0, 0, 0],
		],
		[
		[0, 1, 0, 0],
		[1, 1, 0, 0],
		[0, 1, 0, 0],
		[0, 0, 0, 0],
		],
		[
		[0, 1, 0, 0],
		[1, 1, 1, 0],
		[0, 0, 0, 0],
		[0, 0, 0, 0],
		]
	]
i_piece = [
		[
		[0, 1, 0, 0],
		[0, 1, 0, 0],
		[0, 1, 0, 0],
		[0, 1, 0, 0],
		],
		[
		[0, 0, 0, 0],
		[0, 0, 0, 0],
		[1, 1, 1, 1],
		[0, 0, 0, 0],
		],
		[
		[0, 1, 0, 0],
		[0, 1, 0, 0],
		[0, 1, 0, 0],
		[0, 1, 0, 0],
		],
		[
		[0, 0, 0, 0],
		[0, 0, 0, 0],
		[1, 1, 1, 1],
		[0, 0, 0, 0],
		]
	]
l_piece = [
		[
		[0, 1, 1, 0],
		[0, 1, 0, 0],
		[0, 1, 0, 0],
		[0, 0, 0, 0],
		],
		[
		[0, 0, 0, 0],
		[1, 1, 1, 0],
		[0, 0, 1, 0],
		[0, 0, 0, 0],
		],
		[
		[0, 1, 0, 0],
		[0, 1, 0, 0],
		[1, 1, 0, 0],
		[0, 0, 0, 0],
		],
		[
		[1, 0, 0, 0],
		[1, 1, 1, 0],
		[0, 0, 0, 0],
		[0, 0, 0, 0],
		]
	]
j_piece = [
		[
		[0, 1, 0, 0],
		[0, 1, 0, 0],
		[0, 1, 1, 0],
		[0, 0, 0, 0],
		],
		[
		[0, 0, 0, 0],
		[1, 1, 1, 0],
		[1, 0, 0, 0],
		[0, 0, 0, 0],
		],
		[
		[1, 1, 0, 0],
		[0, 1, 0, 0],
		[0, 1, 0, 0],
		[0, 0, 0, 0],
		],
		[
		[0, 0, 1, 0],
		[1, 1, 1, 0],
		[0, 0, 0, 0],
		[0, 0, 0, 0],
		]
	]
s_piece = [
		[
		[0, 0, 1, 0],
		[0, 1, 1, 0],
		[0, 1, 0, 0],
		[0, 0, 0, 0],
		],
		[
		[1, 1, 0, 0],
		[0, 1, 1, 0],
		[0, 0, 0, 0],
		[0, 0, 0, 0],
		],
		[
		[0, 0, 1, 0],
		[0, 1, 1, 0],
		[0, 1, 0, 0],
		[0, 0, 0, 0],
		],
		[
		[1, 1, 0, 0],
		[0, 1, 1, 0],
		[0, 0, 0, 0],
		[0, 0, 0, 0],
		]
	]
z_piece = [
		[
		[0, 1, 0, 0],
		[0, 1, 1, 0],
		[0, 0, 1, 0],
		[0, 0, 0, 0],
		],
		[
		[0, 1, 1, 0],
		[1, 1, 0, 0],
		[0, 0, 0, 0],
		[0, 0, 0, 0],
		],
		[
		[0, 1, 0, 0],
		[0, 1, 1, 0],
		[0, 0, 1, 0],
		[0, 0, 0, 0],
		],
		[
		[0, 1, 1, 0],
		[1, 1, 0, 0],
		[0, 0, 0, 0],
		[0, 0, 0, 0],
		]
	]
o_piece = [
		[
		[0, 0, 0, 0],
		[1, 1, 0, 0],
		[1, 1, 0, 0],
		[0, 0, 0, 0],
		],
		[
		[0, 0, 0, 0],
		[1, 1, 0, 0],
		[1, 1, 0, 0],
		[0, 0, 0, 0],
		],
		[
		[0, 0, 0, 0],
		[1, 1, 0, 0],
		[1, 1, 0, 0],
		[0, 0, 0, 0],
		],
		[
		[0, 0, 0, 0],
		[1, 1, 0, 0],
		[1, 1, 0, 0],
		[0, 0, 0, 0],
		]
	]

rotation_state = 0
piece_position = (3, 0)

piece = l_piece

def getPiece():
	return piece[rotation_state]


current_piece = getPiece()

def collides(position, piece, field):
	for i, line in enumerate(piece):
		for j, x in enumerate(line):
			if x == 1:
				if field[position[0] + i][position[1] + j] == 1:
					return True
	return False
	

def outOfBounds(position, piece):
	for i, line in enumerate(piece):
		for j,x in enumerate(line):
			if x == 1:
				if (not i + position[0] in range(10)) or (not j + position[1] in range(20)):
					return True
	return False

def movePiece(key, field):
	global piece_position
	if key == "DOWN":
		new_piece_position = (piece_position[0], piece_position[1] + 1)
	elif key == "UP":
		new_piece_position = (piece_position[0], piece_position[1] - 1)
	elif key == "LEFT":
		new_piece_position = (piece_position[0] - 1, piece_position[1])
	elif key == "RIGHT":
		new_piece_position = (piece_position[0] + 1, piece_position[1])
	if (not outOfBounds(new_piece_position, getPiece())) and (not collides(new_piece_position, getPiece(), field)):
		piece_position = new_piece_position

def setPiece(new_piece):
	global current_piece, piece, piece_position, rotation_state
	if new_piece == 0:
		piece = i_piece
	elif new_piece == 1:
		piece = l_piece
	elif new_piece == 2:
		piece = j_piece
	elif new_piece == 3:
		piece = s_piece
	elif new_piece == 4:
		piece = z_piece
	elif new_piece == 5:
		piece = t_piece
	elif new_piece == 6:
		piece = o_piece
	rotation_state = 0
	current_piece = piece[rotation_state]
	piece_position = (3, 0)



def rotatePiece(screen, rotation):
	global current_piece
	if rotation == "cw":
		rotate('cw')
		if not outOfBounds(piece_position, getPiece()):
			current_piece = getPiece()
		else:
			rotate('ccw')
	elif rotation == "ccw":
		rotate('ccw')
		if not outOfBounds(piece_position, getPiece()):
			current_piece = getPiece()
		else:
			rotate('cw')

def rotate(direction):
	global rotation_state
	if direction == "cw":
		rotation_state = (rotation_state - 1) % 4
	elif direction == "ccw":
		rotation_state = (rotation_state + 1) % 4
