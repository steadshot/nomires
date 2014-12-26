import random
from collections import deque

t_piece = [ [ [0, 1, 0, 0], [0, 1, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0], ], [ [0, 0, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0], ], [ [0, 1, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], ], [ [0, 1, 0, 0], [1, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], ] ]
i_piece = [ [ [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], ], [ [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], ], [ [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], ], [ [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], ] ]
l_piece = [ [ [0, 1, 1, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], ], [ [0, 0, 0, 0], [1, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0], ], [ [0, 1, 0, 0], [0, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], ], [ [1, 0, 0, 0], [1, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], ] ]
j_piece = [ [ [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0], ], [ [0, 0, 0, 0], [1, 1, 1, 0], [1, 0, 0, 0], [0, 0, 0, 0], ], [ [1, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], ], [ [0, 0, 1, 0], [1, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], ] ]
s_piece = [ [ [0, 0, 1, 0], [0, 1, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0], ], [ [1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], ], [ [0, 0, 1, 0], [0, 1, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0], ], [ [1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], ] ]
z_piece = [ [ [0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0], ], [ [0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], ], [ [0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0], ], [ [0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], ] ]
o_piece = [ [ [0, 0, 0, 0], [1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], ], [ [0, 0, 0, 0], [1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], ], [ [0, 0, 0, 0], [1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], ], [ [0, 0, 0, 0], [1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], ] ]


def newPiece():
	for i in range(6):
		candidatePiece = random.randint(0, 6)
		if candidatePiece not in history:
			break
	while first_piece and candidatePiece in [3, 4, 6]:
		candidatePiece = random.randint(0, 6)

	history.append(candidatePiece)
	history.popleft()
	#print history
	return candidatePiece


def nextPiece():
	return next_piece


def resetHistory():
	global history, first_piece, next_piece
	history = deque([3, 4, 3, 4])
	first_piece = True
	dummy = [[0 for i in range(20)] for j in range(10)]
	setPiece(-1, dummy)
	next_piece = newPiece()
	first_piece = False



def collides(position, piece, field):
	for i, line in enumerate(piece):
		for j, x in enumerate(line):
			if x == 1:
				if field[position[0] + i][position[1] + j] == 1:
					return True
	return False

def setPiece(new_piece, field):
	global current_piece, piece, piece_position, rotation_state, next_piece

	if new_piece == -1:
		new_piece = newPiece()

	pieces = 'iljszto'
	piece = eval(pieces[new_piece] + "_piece")


	rotation_state = 0
	current_piece = piece[rotation_state]
	piece_position = (3, 0)
	next_piece = newPiece()
	if collides(piece_position, current_piece, field):
		#print 'alles hat ein ende, nur die wurst hat zwei'
		return 'end'

def getPiece():
	return piece[rotation_state]


def setDirection(direction):
	global piece_direction
	piece_direction = direction

def getDirection():
	global piece_direction
	return piece_direction

	

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
	else:
		return -1




def rotatePiece(screen, rotation, field):
	global current_piece, piece_position
	x,y = piece_position
	# for wall kicks: try basic rotation, 1 space right of basic rotation, 1 space left of basic rotation
	# TODO: implement exceptions
	# final (x, y) is for when all three tries fail, to set the piece_position to its original position
	# having to change the piece_position itself is wacky
	# rotating back and forth all the time ain't pretty either,
	# we should have getter methods and not manipulate global variables all the time
	positions = [(x, y), (x + 1, y), (x - 1, y), (x, y)]
	for pos in positions:
		piece_position = pos
		if rotation == "cw":
			rotate('cw')
			if not outOfBounds(pos, getPiece()) and not collides(pos, getPiece(), field):
				current_piece = getPiece()
				break
			else:
				rotate('ccw')
		elif rotation == "ccw":
			rotate('ccw')
			if not outOfBounds(pos, getPiece()) and not collides(pos, getPiece(), field):
				current_piece = getPiece()
				break
			else:
				rotate('cw')

def rotate(direction):
	global rotation_state
	if direction == "cw":
		rotation_state = (rotation_state - 1) % 4
	elif direction == "ccw":
		rotation_state = (rotation_state + 1) % 4

next_piece = 0
history = deque([3, 4, 3, 4])
first_piece = True

rotation_state = 0
piece_position = (3, 0)

dummy = [[0 for i in range(20)] for j in range(10)]
setPiece(-1, dummy)
first_piece = False

piece_direction = "RIGHT"
