import pygame

BLACK = pygame.Color(160, 82, 45)
WHITE = pygame.Color(255, 255, 255)
GREEN = pygame.Color(0, 255, 0)
STARTX = 360
STARTY = 60
WIDTH = 60


class Piece:
    def __init__(self, name, colour, unitType):
        self.piece = pygame.image.load(f"{name}.png")
        self.name = name
        self.colour = colour
        self.unitType = unitType
        # self.x = startingPositions[unitType][colour]["x"][count - 1]
        # self.y = startingPositions[unitType][colour]["y"]
        self.moved = False
        self.selected = False
        self.alive = True
        self.moving = False


class Grid:
    def __init__(self, x, y):
        self.piece = None
        self.occupied = False
        self.x = x
        self.y = y

    def liftPiece(cls):
        assert(cls.occupied)
        cls.occupied = False
        return cls.piece

    def addPiece(cls, chessPiece):
        assert(not cls.occupied)
        cls.occupied = True
        cls.piece = chessPiece


class Board:
    def __init__(self):
        self.grids = []
        for X in range(0, 8):
            row = []
            for Y in range(0, 8):
                row.append(Grid(X, Y))
            self.grids.append(row)
        self.grids[0][0].addPiece(Piece('blackrook', 'black', 'rook'))
        self.grids[1][0].addPiece(Piece('blackknight', 'black', 'knight'))
        self.grids[2][0].addPiece(Piece('blackbishop', 'black', 'bishop'))
        self.grids[3][0].addPiece(Piece('blackqueen', 'black', 'queen'))
        self.grids[4][0].addPiece(Piece('blackking', 'black', 'king'))
        self.grids[5][0].addPiece(Piece('blackbishop', 'black', 'bishop'))
        self.grids[6][0].addPiece(Piece('blackknight', 'black', 'knight'))
        self.grids[7][0].addPiece(Piece('blackrook', 'black', 'rook'))
        self.grids[0][1].addPiece(Piece('blackpawn', 'black', 'pawn'))
        self.grids[1][1].addPiece(Piece('blackpawn', 'black', 'pawn'))
        self.grids[2][1].addPiece(Piece('blackpawn', 'black', 'pawn'))
        self.grids[3][1].addPiece(Piece('blackpawn', 'black', 'pawn'))
        self.grids[4][1].addPiece(Piece('blackpawn', 'black', 'pawn'))
        self.grids[5][1].addPiece(Piece('blackpawn', 'black', 'pawn'))
        self.grids[6][1].addPiece(Piece('blackpawn', 'black', 'pawn'))
        self.grids[7][1].addPiece(Piece('blackpawn', 'black', 'pawn'))

        self.grids[0][7].addPiece(Piece('whiterook', 'white', 'rook'))
        self.grids[1][7].addPiece(Piece('whiteknight', 'white', 'knight'))
        self.grids[2][7].addPiece(Piece('whitebishop', 'white', 'bishop'))
        self.grids[3][7].addPiece(Piece('whitequeen', 'white', 'queen'))
        self.grids[4][7].addPiece(Piece('whiteking', 'white', 'king'))
        self.grids[5][7].addPiece(Piece('whitebishop', 'white', 'bishop'))
        self.grids[6][7].addPiece(Piece('whiteknight', 'white', 'knight'))
        self.grids[7][7].addPiece(Piece('whiterook', 'white', 'rook'))
        self.grids[0][6].addPiece(Piece('whitepawn', 'white', 'pawn'))
        self.grids[1][6].addPiece(Piece('whitepawn', 'white', 'pawn'))
        self.grids[2][6].addPiece(Piece('whitepawn', 'white', 'pawn'))
        self.grids[3][6].addPiece(Piece('whitepawn', 'white', 'pawn'))
        self.grids[4][6].addPiece(Piece('whitepawn', 'white', 'pawn'))
        self.grids[5][6].addPiece(Piece('whitepawn', 'white', 'pawn'))
        self.grids[6][6].addPiece(Piece('whitepawn', 'white', 'pawn'))
        self.grids[7][6].addPiece(Piece('whitepawn', 'white', 'pawn'))

    def drawBoard(cls, board):
        board.fill(WHITE)
        for x in range(0, 8):
            for y in range(0, 8):
                X = STARTX + x * WIDTH
                Y = STARTY + y * WIDTH
                if not ((x % 2) == (y % 2)):
                    pygame.draw.rect(board, BLACK, (X, Y, WIDTH, WIDTH))
                else:
                    pass
        for row in cls.grids:
            for grid in row:
                if grid.occupied:
                    chessPiece = grid.piece
                    if chessPiece.selected:
                        pygame.draw.rect(
                            board, GREEN, (STARTX + WIDTH * grid.x, STARTY + WIDTH * grid.y, WIDTH, WIDTH))
                    board.blit(chessPiece.piece, (STARTX + WIDTH *
                                                  grid.x, STARTY + WIDTH * grid.y))

    def judgePawn(cls, oldX, oldY, newX, newY):
        oldGrid = cls.grids[oldX][oldY]
        newGrid = cls.grids[newX][newY]
        worker = oldGrid.piece
        if worker.colour == 'white':
            if (oldY - newY) == 1:
                if newX == oldX:
                    if newGrid.occupied:
                        return False
                    else:
                        return True
                elif abs(newX - oldX) == 1:
                    if newGrid.occupied:
                        return True
                    else:
                        return False
            elif (oldY - newY) == 2:
                if worker.moved:
                    return False
                elif not oldX == newX:
                    return False
                else:
                    if newGrid.occupied or cls.grids[oldX][oldY-1].occupied:
                        return False
                    else:
                        return True
            else:
                return False
        else:
            if (oldY - newY) == -1:
                if newX == oldX:
                    if newGrid.occupied:
                        return False
                    else:
                        return True
                elif abs(newX - oldX) == 1:
                    if newGrid.occupied:
                        return True
                    else:
                        return False
            elif (oldY - newY) == -2:
                if worker.moved:
                    return False
                elif not oldX == newX:
                    return False
                else:
                    if newGrid.occupied or cls.grids[oldX][oldY+1].occupied:
                        return False
                    else:
                        return True
            else:
                return False

    def judgeBishop(cls, oldX, oldY, newX, newY):
        if abs(oldY - newY) == abs(oldX - newX):
            if oldY < newY:
                deltaY = 1
            else:
                deltaY = -1
            if oldX < newX:
                deltaX = 1
            else:
                deltaX = -1
            trafficControlX = oldX + deltaX
            trafficControlY = oldY + deltaY
            while (not trafficControlX == newX) and (not trafficControlY == newY):
                if cls.grids[trafficControlX][trafficControlY].occupied:
                    return False
                else:
                    trafficControlX = trafficControlX + deltaX
                    trafficControlY = trafficControlY + deltaY
            return True
        else:
            return False

    def judgeRook(cls, oldX, oldY, newX, newY):
        if not oldX == newX:
            if not oldY == newY:
                return False
            if oldX > newX:
                for x in range(newX+1, oldX):
                    if cls.grids[x][oldY].occupied:
                        return False
                    else:
                        pass
                else:
                    return True
            else:
                for x in range(oldX+1, newX):
                    if cls.grids[x][oldY].occupied:
                        return False
                    else:
                        pass
                else:
                    return True
        elif not oldY == newY:
            if not oldX == newX:
                return False
            if oldY > newY:
                for y in range(newY+1, oldY):
                    if cls.grids[oldX][y].occupied:
                        return False
                    else:
                        pass
                else:
                    return True
            else:
                for y in range(oldY+1, newY):
                    if cls.grids[oldX][y].occupied:
                        return False
                    else:
                        pass
                else:
                    return True
        else:
            return False

    def judgement(cls, oldX, oldY, newX, newY):
        newGrid = cls.grids[newX][newY]
        oldGrid = cls.grids[oldX][oldY]
        worker = oldGrid.piece
        if worker.unitType == 'pawn':
            return cls.judgePawn(oldX, oldY, newX, newY)
        elif worker.unitType == 'rook':
            return cls.judgeRook(oldX, oldY, newX, newY)
        elif worker.unitType == 'knight':
            if abs(oldX - newX) == 2:
                if abs(oldY - newY) == 1:
                    return True
                else:
                    return False
            elif abs(oldY - newY) == 2:
                if abs(oldX - newX) == 1:
                    return True
                else:
                    return False
            else:
                return False
        elif worker.unitType == 'bishop':
            return cls.judgeBishop(oldX, oldY, newX, newY)
        elif worker.unitType == 'queen':
            return cls.judgeBishop(oldX, oldY, newX, newY) or cls.judgeRook(oldX, oldY, newX, newY)
        elif worker.unitType == 'king':
            return abs(oldX - newX) <= 1 and abs(oldY - newY) <= 1
        else:
            return True

    def move(cls, oldX, oldY, newX, newY):
        if not cls.judgement(oldX, oldY, newX, newY):
            return False
        newGrid = cls.grids[newX][newY]
        oldGrid = cls.grids[oldX][oldY]
        if newGrid.occupied:
            return cls.battle(oldX, oldY, newX, newY)
        else:
            newGrid.addPiece(oldGrid.liftPiece())
            newGrid.piece.moved = True
            return True

    def battle(cls, oldX, oldY, newX, newY):
        oldGrid = cls.grids[oldX][oldY]
        newGrid = cls.grids[newX][newY]
        if oldGrid.piece.colour == newGrid.piece.colour:
            return False
        else:
            newGrid.liftPiece()
            newGrid.addPiece(oldGrid.liftPiece())
            newGrid.piece.moved = True
            return True
