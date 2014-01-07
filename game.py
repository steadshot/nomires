import pygame, sys
from pygame.locals import *
import piece
import random

# only for testing purposes
#import os
#os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (-1300, 100)

def drawPreview(screen):
	x = piece.nextPiece()
	str = 'ILJSZTO'.lower()
	exec('piece = piece.' + str[x] + '_piece[0]')
	for i, line in enumerate(piece):
		for j, x in enumerate(line):
			if x == 1:
				pygame.draw.rect(screen, WHITE, (preview_x + i * block_size, preview_y + j * block_size, block_size, block_size), 0)
			else:
				pygame.draw.rect(screen, (0, 0, 0), (preview_x + i * block_size, preview_y + j * block_size, block_size, block_size), 0)
	pygame.draw.rect(screen, WHITE, (preview_x, preview_y, block_size * 4, block_size * 4), 1)

def drawEmptyField(screen):
	"""draws a field, big whoop"""
	for i, line in enumerate(playfield):
		for j, x in enumerate(line):
			pygame.draw.rect(screen, (0, 0, 0), (start_x + i * block_size, start_y + j * block_size, block_size, block_size), 0)

def drawField(screen):
	"""draws a field, big whoop"""
	for i, line in enumerate(playfield):
		for j, x in enumerate(line):
			if x == 1:
				pygame.draw.rect(screen, WHITE, (start_x + i * block_size, start_y + j * block_size, block_size, block_size), 0)
			if x == 0:
				pygame.draw.rect(screen, (0, 0, 0), (start_x + i * block_size, start_y + j * block_size, block_size, block_size), 0)

def drawPiece(screen):
	for i, line in enumerate(piece.getPiece()):
		for j, x in enumerate(line):
			if x == 1:
				pygame.draw.rect(screen, WHITE, (piece.piece_position[0] * block_size + start_x + i * block_size, piece.piece_position[1] * block_size + start_y + j * block_size, block_size, block_size), 0)


def drawBorder(screen):
	pygame.draw.lines(screen, WHITE, False, 
			[(start_x, start_y), (start_x + 10 * block_size, start_y), 
				(start_x + 10 * block_size, start_y + 20 * block_size), 
				(start_x, start_y + 20 * block_size), (start_x, start_y)], 1)

def drawGrid(screen):
	for i in range(10):
		pygame.draw.lines(screen, WHITE, False, 
				[(start_x + i * block_size, start_y), (start_x + i * block_size, start_y + 20 * block_size)], 1)



def refresh(screen):
	if invisible_flag:
		drawEmptyField(screen)
	else:
		drawField(screen)
	drawPiece(screen)
	drawBorder(screen)
	drawGrid(screen)
	drawPreview(DISPLAYSURF)


def addToPlayfield():
	global playfield
	for i, line in enumerate(piece.getPiece()):
		for j, x in enumerate(line):
			if x == 1:
				playfield[piece.piece_position[0] + i][piece.piece_position[1] + j] = 1

	# check if there are lines to clear

	flipped = [[playfield[i][j] for i in range(10)] for j in range(20)]
	for i, line in enumerate(flipped):
		if reduce(lambda x,y: x + y, line) == 10:
			flipped[i] = [0]*10
			for j in range(1, i + 1)[::-1]:
				flipped[j] = flipped[j - 1]
	playfield = [[flipped[i][j] for i in range(20)] for j in range(10)]

	#check for holes

	global game_over
	if createsHoles():
		#print "REGRET!"
		#game_over = True
		#pygame.draw.rect(DISPLAYSURF, (255, 0, 0), (2, 2, 50, 50), 0)
		pass
	else:
		#print "COOL!!"
		pass

def createsHoles():
	global playfield
	for i, line in enumerate(piece.getPiece()):
		for j, x in enumerate(line[::-1]):
			if x == 1 and piece.piece_position[1] + 4 - j < 20:
				if playfield[piece.piece_position[0] + i][piece.piece_position[1] + 3 - j] == 1 and playfield[piece.piece_position[0] + i][piece.piece_position[1] + 3 - j + 1] == 0:
					return True
				else:
					break
	return False

def lock():
	global piece_counter, game_over
	addToPlayfield()
	piece_counter += 1
	if 'end' == piece.setPiece(piece.next_piece, playfield) or game_over:
		pygame.draw.rect(DISPLAYSURF, (255, 0, 0), (2, 2, 50, 50), 0)
		game_over = True
	refresh(DISPLAYSURF)

def peek(screen):
	pass

def flash(screen, time):
	pass

def reset():
	global playfield, game_over, piece_counter
	playfield = [[0 for i in range(20)] for j in range(10)]
	piece.resetHistory()
	refresh(DISPLAYSURF)
	pygame.draw.rect(DISPLAYSURF, (0, 0, 0), (2, 2, 50, 50), 0)
	game_over = False
	piece_counter = 1
	pass

def quit():
	pygame.quit()
	sys.exit()

block_size = 20
playfield = [[0 for i in range(20)] for j in range(10)]
start_x = 50
start_y = 140
preview_x = start_x + 3 * block_size
preview_y = start_y - 5 * block_size
das = 0
das_flag = False
soft_drop_flag = False
invisible_flag = False
WHITE = (255, 255, 255)

piece_counter = 1
pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption('nomires - where tetris goes to die')
clock = pygame.time.Clock()
refresh(DISPLAYSURF)
game_over = False
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			quit()
		if event.type == KEYDOWN:
			if event.key == K_r:
				reset()
			if event.key == K_RETURN:
				quit()
			if game_over:
				continue
			if event.key == K_z:
				piece.rotatePiece(DISPLAYSURF, 'ccw', playfield)
				refresh(DISPLAYSURF)
			if event.key == K_x:
				piece.rotatePiece(DISPLAYSURF, 'cw', playfield)
				refresh(DISPLAYSURF)
			if event.key == K_DOWN:
				#soft drop
				#soft_drop_flag = True
				#piece.movePiece("DOWN", playfield)
				#refresh(DISPLAYSURF)

				#sonic drop instead
				x = 0
				while x != -1:
					x = piece.movePiece("DOWN", playfield)
				refresh(DISPLAYSURF)
			if event.key == K_UP:
				x = 0
				while x != -1:
					x = piece.movePiece("DOWN", playfield)

				#drawEmptyField(DISPLAYSURF)
				#if piece_counter % 5 == 0:
				#	drawField(DISPLAYSURF)
				#drawPiece(DISPLAYSURF)
				#drawBorder(DISPLAYSURF)
				#drawGrid(DISPLAYSURF)
				#pygame.display.update()
				##pygame.time.wait(1000)
				#drawEmptyField(DISPLAYSURF)

				lock()
			if event.key == K_RIGHT:
				piece.movePiece("RIGHT", playfield)
				piece.setDirection("RIGHT")
				das_flag = True
				refresh(DISPLAYSURF)
			if event.key == K_LEFT:
				piece.movePiece("LEFT", playfield)
				piece.setDirection("LEFT")
				das_flag = True
				refresh(DISPLAYSURF)
			if event.key == K_w:
				#drawField(DISPLAYSURF)
				#drawGrid(DISPLAYSURF)
				#drawBorder(DISPLAYSURF)
				if invisible_flag:
					invisible_flag = False
					refresh(DISPLAYSURF)
					invisible_flag = True
		if event.type == KEYUP:
			if event.key == K_RIGHT or event.key == K_LEFT:
				das = 0
				das_flag = False
			if event.key == K_DOWN or event.key == K_UP:
				soft_drop_flag = False
			if event.key == K_w:
				refresh(DISPLAYSURF)

	if das_flag:
			das += 1
	if soft_drop_flag and not game_over:
		if piece.movePiece("DOWN", playfield) == -1:
			lock()
		refresh(DISPLAYSURF)
	if das >= 12:
			piece.movePiece(piece.getDirection(), playfield)
			refresh(DISPLAYSURF)
	pygame.display.update()
	clock.tick(60)
