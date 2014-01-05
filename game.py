import pygame, sys
from pygame.locals import *
import piece
import random

block_size = 20
playfield = [[0 for i in range(20)] for j in range(10)]
start_x = 50
start_y = 100
das = 0
das_flag = False


def drawField(screen):
	"""draws a field, big whoop"""
	for i, line in enumerate(playfield):
		for j, x in enumerate(line):
			if x == 1:
				pygame.draw.rect(screen, (255, 255, 255), (start_x + i * block_size, start_y + j * block_size, block_size, block_size), 0)
			if x == 0:
				pygame.draw.rect(screen, (0, 0, 0), (start_x + i * block_size, start_y + j * block_size, block_size, block_size), 0)

def drawPiece(screen):
	for i, line in enumerate(piece.getPiece()):
		for j, x in enumerate(line):
			if x == 1:
				pygame.draw.rect(screen, (255, 255, 255), (piece.piece_position[0] * block_size + start_x + i * block_size, piece.piece_position[1] * block_size + start_y + j * block_size, block_size, block_size), 0)


def drawBorder(screen):
	pygame.draw.lines(screen, (255, 255, 255), False, 
			[(start_x, start_y), (start_x + 10 * block_size, start_y), 
				(start_x + 10 * block_size, start_y + 20 * block_size), 
				(start_x, start_y + 20 * block_size), (start_x, start_y)], 1)


def refresh(screen):
	drawField(screen)
	drawPiece(screen)
	drawBorder(screen)


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

def printField():
	for line in playfield:
		print line

pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption('nomires - where tetris goes to die')
clock = pygame.time.Clock()
refresh(DISPLAYSURF)
game_over = False
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_r:
				playfield = [[0 for i in range(20)] for j in range(10)]
				refresh(DISPLAYSURF)
				game_over = False
			if event.key == K_RETURN:
				pygame.quit()
				sys.exit()
			if game_over:
				continue
			if event.key == K_z:
				piece.rotatePiece(DISPLAYSURF, 'ccw', playfield)
				refresh(DISPLAYSURF)
			if event.key == K_x:
				piece.rotatePiece(DISPLAYSURF, 'cw', playfield)
				refresh(DISPLAYSURF)

			if event.key == K_DOWN:

				piece.movePiece("DOWN", playfield)
				refresh(DISPLAYSURF)
			if event.key == K_UP:
				exec('piece.movePiece("DOWN", playfield);'*20)
				# ^^^ uuuuuuglyyyyyyy
				addToPlayfield()
				if 'end' == piece.setPiece(-1, playfield):
					game_over = True
				refresh(DISPLAYSURF)
					


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
		if event.type == KEYUP:
			if event.key == K_RIGHT or event.key == K_LEFT:
				das = 0
				das_flag = False

	if das_flag:
			das += 1
	if das >= 12:
			piece.movePiece(piece.getDirection(), playfield)
			refresh(DISPLAYSURF)
	pygame.display.update()
	clock.tick(60)
