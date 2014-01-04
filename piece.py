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

rotation_state = 0

piece = t_piece

def getPiece():
	return piece[rotation_state]

def rotate(direction):
	global rotation_state
	if direction == "cw":
		rotation_state = (rotation_state - 1) % 4
	elif direction == "ccw":
		rotation_state = (rotation_state + 1) % 4

i_piece = [
		[0, 1, 0, 0],
		[0, 1, 0, 0],
		[0, 1, 0, 0],
		[0, 1, 0, 0],
		]

l_piece = [
		[0, 1, 1, 0],
		[0, 1, 0, 0],
		[0, 1, 0, 0],
		[0, 0, 0, 0],
		]
j_piece = [
		[0, 1, 0, 0],
		[0, 1, 0, 0],
		[0, 1, 1, 0],
		[0, 0, 0, 0],
		]
s_piece = [
		[0, 0, 1, 0],
		[0, 1, 1, 0],
		[0, 1, 0, 0],
		[0, 0, 0, 0],
		]
z_piece = [
		[0, 1, 0, 0],
		[0, 1, 1, 0],
		[0, 0, 1, 0],
		[0, 0, 0, 0],
		]
o_piece = [
		[0, 0, 0, 0],
		[1, 1, 0, 0],
		[1, 1, 0, 0],
		[0, 0, 0, 0],
		]
