import Piece
import pygame
import sys

BLACK = pygame.Color(160, 82, 45)
WHITE = pygame.Color(255, 255, 255)
GREEN = pygame.Color(0, 255, 0)
STARTX = 360
STARTY = 60
WIDTH = 60


class Turn:
    def __init__(self, start):
        self.currentTurn = start

    def endTurn(cls):
        if cls.currentTurn == "white":
            cls.currentTurn = "black"
        else:
            cls.currentTurn = "white"

    def checkTurn(cls, gameBoard, X, Y):
        return gameBoard.grids[X][Y].occupied and (gameBoard.grids[X][Y].piece.colour == cls.currentTurn)

    def drawBackground(cls, board):
        if cls.currentTurn == "white":
            pygame.draw.rect(board, GREEN, (0, 0, 360, 600))
            pygame.draw.rect(board, WHITE, (840, 0, 360, 600))
            board.blit(pygame.image.load("white.png"), (60, 0))
            board.blit(pygame.image.load("black.png"), (900, 0))
        else:
            pygame.draw.rect(board, WHITE, (0, 0, 360, 600))
            pygame.draw.rect(board, GREEN, (840, 0, 360, 600))
            board.blit(pygame.image.load("white.png"), (60, 0))
            board.blit(pygame.image.load("black.png"), (900, 0))
