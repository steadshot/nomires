import pygame, sys
from pygame.locals import *

block_size = 20
playfield = [[0 for i in range(20)] for j in range(10)]
playfield[2][3] = 1
playfield[5][10] = 1
start_x = 50
start_y = 100

t_pieces = [
		[1, 0, 0, 0],
		[1, 1, 0, 0],
		[1, 0, 0, 0],
		[0, 0, 0, 0],
		]

i_piece = [
		[1, 0, 0, 0],
		[1, 0, 0, 0],
		[1, 0, 0, 0],
		[1, 0, 0, 0],
		]

piece_position = (3, 0)

current_piece = i_piece


def drawField(screen):
	"""draws a field, big whoop"""
	for i, line in enumerate(playfield):
		for j, x in enumerate(line):
			if x == 1:
				pygame.draw.rect(screen, (255, 255, 255), (start_x + i * block_size, start_y + j * block_size, block_size, block_size), 0)
			if x == 0:
				pygame.draw.rect(screen, (0, 0, 0), (start_x + i * block_size, start_y + j * block_size, block_size, block_size), 0)

def drawPiece(screen):
	for i, line in enumerate(current_piece):
		for j, x in enumerate(line):
			if x == 1:
				pygame.draw.rect(screen, (255, 255, 255), (piece_position[0] * block_size + start_x + i * block_size, piece_position[1] * block_size + start_y + j * block_size, block_size, block_size), 0)


def drawBorder(screen):
	pygame.draw.lines(screen, (255, 255, 255), False, 
			[(start_x, start_y), (start_x + 10 * block_size, start_y), 
				(start_x + 10 * block_size, start_y + 20 * block_size), 
				(start_x, start_y + 20 * block_size), (start_x, start_y)], 1)





def movePiece(screen, key):
	global piece_position
	if key == "DOWN":
		new_piece_position = (piece_position[0], piece_position[1] + 1)
	elif key == "UP":
		new_piece_position = (piece_position[0], piece_position[1] - 1)
	elif key == "LEFT":
		new_piece_position = (piece_position[0] - 1, piece_position[1])
	elif key == "RIGHT":
		new_piece_position = (piece_position[0] + 1, piece_position[1])
	if not outOfBounds(new_piece_position):
		piece_position = new_piece_position
	drawField(screen)
	drawPiece(screen)
	drawBorder(screen)
	
def outOfBounds(position):
	for i, line in enumerate(current_piece):
		for j,x in enumerate(line):
			if x == 1:
				if (not i + position[0] in range(10)) or (not j + position[1] in range(20)):
					return True
	
	return False


pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption('nomires - where tetris goes to die')
drawField(DISPLAYSURF)
drawPiece(DISPLAYSURF)
drawBorder(DISPLAYSURF)
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_DOWN:
				movePiece(DISPLAYSURF, "DOWN")
			if event.key == K_UP:
				movePiece(DISPLAYSURF, "UP")
			if event.key == K_RIGHT:
				movePiece(DISPLAYSURF, "RIGHT")
			if event.key == K_LEFT:
				movePiece(DISPLAYSURF, "LEFT")
			if event.key == K_RETURN:
				pygame.quit()
				sys.exit()
		pygame.display.update()
