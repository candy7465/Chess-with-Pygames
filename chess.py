import pygame
import sys
import Piece
import turn

pygame.init()

board = pygame.display.set_mode((1200, 600))
pygame.display.set_caption('Chess')

BLACK = pygame.Color(160, 82, 45)
WHITE = pygame.Color(255, 255, 255)
GREEN = pygame.Color(0, 255, 0)
STARTX = 360
STARTY = 60
WIDTH = 60


def getCoordinates(x, y):
    for X in range(STARTX, STARTX + WIDTH * 8):
        for Y in range(STARTY, STARTY + WIDTH * 8):
            if x == X and y == Y:
                boardX = int((X - STARTX) / WIDTH)
                boardY = int((Y - STARTY) / WIDTH)
                return (boardX, boardY)
    return (None, None)


def toggleSelect(gameBoard, x, y):
    targetGrid = gameBoard.grids[x][y]
    if not targetGrid.occupied:
        return None
    else:
        targetGrid.piece.selected = not targetGrid.piece.selected


gameBoard = Piece.Board()
gameBoard.drawBoard(board)
turn = turn.Turn("white")
FPS = 60
fpsClock = pygame.time.Clock()


mousex = 0
mousey = 0

oldSelectX = None
oldSelectY = None

while 1:
    gameBoard.drawBoard(board)
    turn.drawBackground(board)
    mouseSelect = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            mousex, mousey = event.pos
            mouseSelect = True

    if mouseSelect:
        boxx, boxy = getCoordinates(mousex, mousey)
        if oldSelectX != None and oldSelectY != None:
            toggleSelect(gameBoard, oldSelectX, oldSelectY)
        if boxx != None and boxy != None:
            if oldSelectX != None and oldSelectY != None:
                if gameBoard.move(oldSelectX, oldSelectY, boxx, boxy):
                    turn.endTurn()
                oldSelectX = None
                oldSelectY = None
            elif gameBoard.grids[boxx][boxy].occupied:
                if turn.checkTurn(gameBoard, boxx, boxy):
                    toggleSelect(gameBoard, boxx, boxy)
                    oldSelectX = boxx
                    oldSelectY = boxy
                else:
                    pass
        else:
            oldSelectX = None
            oldSelectY = None

    pygame.display.update()
    fpsClock.tick(FPS)
