from Search.InitPieces import InitPieces
from Search.Evaluation import Evaluation
import copy

class State:
    player = None
    agent = None  # human can play red or black
    redPieces = None
    blackPieces = None
    board = None  # 2D
    alpha = float("-inf")
    beata = float("inf")

    Evaluation = Evaluation()

    def __init__(self, player, agent):
        self.player = player
        self.agent = agent
        self.redPieces = InitPieces().getRedPieces()
        self.blackPieces = InitPieces().getBlackPieces()
        self.board = InitPieces().getBoard()

    def getIndexOfRedPiece(self, pieceName):
        index = 0
        for piece in self.redPieces:
            if piece.name == pieceName:
                return index
            index += 1

    def getIndexOfBlackPiece(self, pieceName):
        index = 0
        for piece in self.blackPieces:
            if piece.name == pieceName:
                return index
            index += 1
    def updateBoardState(self, state64):
        counter = 0
        diedPieces = []
        for pointer in range(0, 32, 2):
            pieceColumn = self.redPieces[counter].position[0]
            pieceRow = self.redPieces[counter].position[1]
            pieceName = self.redPieces[counter].name
            destinationColumn = int(state64[pointer])
            destinationRow = int(state64[pointer + 1])
            if destinationColumn == 9:
                if self.board[pieceRow][pieceColumn] == pieceName:
                    self.board[pieceRow][pieceColumn] = ''
                diedPieces.append(pieceName)
                counter += 1
                continue
            if destinationColumn != pieceColumn or destinationRow != pieceRow:
                if self.board[pieceRow][pieceColumn] == pieceName:
                    self.board[pieceRow][pieceColumn] = ''
                self.board[destinationRow][destinationColumn] = pieceName
                self.redPieces[counter].position[0] = destinationColumn
                self.redPieces[counter].position[1] = destinationRow
            counter += 1
        for diedPiece in diedPieces:
            del (self.redPieces[self.getIndexOfRedPiece(diedPiece)])
        diedPieces = []
        counter = 0
        for pointer in range(32, 64, 2):
            pieceColumn = self.blackPieces[counter].position[0]
            pieceRow = self.blackPieces[counter].position[1]
            pieceName = self.blackPieces[counter].name
            destinationColumn = int(state64[pointer])
            destinationRow = int(state64[pointer + 1])
            if destinationColumn == 9:
                if self.board[pieceRow][pieceColumn] == pieceName:
                    self.board[pieceRow][pieceColumn] = ''
                diedPieces.append(pieceName)
                counter += 1
                continue
            if destinationColumn != pieceColumn or destinationRow != pieceRow:
                if self.board[pieceRow][pieceColumn] == pieceName:
                    self.board[pieceRow][pieceColumn] = ''
                self.board[destinationRow][destinationColumn] = pieceName
                self.blackPieces[counter].position[0] = destinationColumn
                self.blackPieces[counter].position[1] = destinationRow
            counter += 1
        for diedPiece in diedPieces:
            del (self.blackPieces[self.getIndexOfBlackPiece(diedPiece)])

    def isEndState(self):
        if self.isRedKOver():
            return -1
        if self.isBlackKOver():
            return 1
        return 0

    def isRedKOver(self):
        if "K" not in self.board[7] \
                and "K" not in self.board[8] \
                and "K" not in self.board[9]:
            return True

    def isBlackKOver(self):
        if "k" not in self.board[0] \
                and "k" not in self.board[1] \
                and "k" not in self.board[2]:
            return True

    def isKingOnSameRow(self):
        redKingColumn = 9
        blackKingColumn = 9
        for piece in self.redPieces:
            if piece.name == "K":
                redKingColumn=piece.position[0]
        for piece in self.blackPieces:
            if piece.name == "k":
                blackKingColumn=piece.position[0]
        if redKingColumn != blackKingColumn:
            return False
        for piece in self.redPieces:
            if piece.position[0] == redKingColumn:
                return False
        for piece in self.blackPieces:
            if piece.position[0] == redKingColumn:
                return False
        return True

    def getNextState(self, pieceName, move):
        nextState = State(self.player, self.agent)
        nextState.board = copy.deepcopy(self.board)
        nextState.redPieces = copy.deepcopy(self.redPieces)
        nextState.blackPieces = copy.deepcopy(self.blackPieces)
        if self.player == "Red":
            nextState.player = "Black"
            for piece in nextState.redPieces:  # don't modify directly in for
                if pieceName == piece.name:
                    piecePosition = piece.position
                    nextState.board[piecePosition[1]][piecePosition[0]] = ''
                    nextState.board[move[1]][move[0]] = pieceName
                    pieceIndex = nextState.redPieces.index(piece)
                    nextState.redPieces[pieceIndex].position = move
                    break
            diedPiece = ''
            for piece in nextState.blackPieces:
                if piece.position == move:
                    diedPiece = piece.name
                    # print("diedPiece:" + diedPiece)
                    break
            if diedPiece != '':
                del (nextState.blackPieces[nextState.getIndexOfBlackPiece(diedPiece)])
        else:
            nextState.player = "Red"
            for piece in nextState.blackPieces:
                if pieceName == piece.name:
                    piecePosition = piece.position
                    nextState.board[piecePosition[1]][piecePosition[0]] = ''
                    nextState.board[move[1]][move[0]] = pieceName
                    pieceIndex = nextState.blackPieces.index(piece)
                    nextState.blackPieces[pieceIndex].position = move
                    break
            diedPiece = ''
            for piece in nextState.redPieces:
                if piece.position == move:
                    diedPiece = piece.name
                    # print("diedPiece:" + diedPiece)
                    break
            if diedPiece != '':
                del (nextState.redPieces[nextState.getIndexOfRedPiece(diedPiece)])
        return nextState

    def getScoreOfRed(self):
        score = 0
        for piece in self.redPieces:
            score += self.getScoreOfRedPiece(piece)
        return score

    def getScoreOfRedPiece(self, piece):
        return self.getScoreOfPositionForRed(piece) + self.Evaluation.getPieceValueByName(piece.name)

    def getScoreOfPositionForRed(self, piece):
        return self.Evaluation.getPositionValueForRed(piece)

    def getScoreOfBlack(self):
        score = 0
        for piece in self.blackPieces:
            score += self.getScoreOfBlackPiece(piece)
        return score

    def getScoreOfBlackPiece(self, piece):
        return self.getScoreOfPositionForBlack(piece) + self.Evaluation.getPieceValueByName(piece.name[0])

    def getScoreOfPositionForBlack(self, piece):
        return self.Evaluation.getPositionValueForBlack(piece)
