from Search.InitPieces import InitPieces


class Rule:
    minRow = 0
    maxRow = 9
    minColumn = 0
    maxColumn = 8
    redTianMinRow = 7
    redTianMaxRow = 9
    redTianMinColumn = 3
    redTianMaxColumn = 5
    blackTianMinRow = 0
    blackTianMaxRow = 2
    blackTianMinColumn = 3
    blackTianMaxColumn = 5
    upRiverRow = 4
    lowRiverRow = 5
    invalidPosition = [9, 9]
    def __init__(self):
        pass
    def getLegalMovesForPiece(self, piece, state, piecesLegalMoves):
        pieceName = piece.name
        pieceType = pieceName[0]
        piecePosition = piece.position
        board = state.board
        player = state.player
        if pieceType == "J" or pieceType == "j":
            self.setPiecesLegalMovesForJ(piecesLegalMoves, pieceName, board, piecePosition, player)
        elif pieceType == "M" or pieceType == "m":
            self.setPiecesLegalMovesForM(piecesLegalMoves, pieceName, board, piecePosition, player)
        elif pieceType == "X" or pieceType == "x":
            self.setPiecesLegalMovesForX(piecesLegalMoves, pieceName, board, piecePosition, player)
        elif pieceType == "S" or pieceType == "s":
            self.setPiecesLegalMovesForS(piecesLegalMoves, pieceName, board, piecePosition, player)
        elif pieceType == "K" or pieceType == "k":
            self.setPiecesLegalMovesForK(piecesLegalMoves, pieceName, board, piecePosition, player)
        elif pieceType == "P" or pieceType == "p":
            self.setPiecesLegalMovesForP(piecesLegalMoves, pieceName, board, piecePosition, player)
        elif pieceType == "B" or pieceType == "b":
            self.setPiecesLegalMovesForB(piecesLegalMoves, pieceName, board, piecePosition, player)
        return piecesLegalMoves

    def getLegalMoves(self, state, pieces):
        piecesLegalMoves = {}  # dict e.g {"J1":[[1,1],[1,2]...]}
        for piece in pieces:
            if piece.position != self.invalidPosition:
                piecesLegalMoves = self.getLegalMovesForPiece(piece, state, piecesLegalMoves)
        return piecesLegalMoves

    def setPiecesLegalMovesForB(self, piecesLegalMoves, pieceName, board, piecePosition, player):
        pieceLegalMoves = self.getBLegalMoves(board, piecePosition, player)
        if pieceName == "B1":
            piecesLegalMoves["B1"] = pieceLegalMoves
        elif pieceName == "B2":
            piecesLegalMoves["B2"] = pieceLegalMoves
        elif pieceName == "B3":
            piecesLegalMoves["B3"] = pieceLegalMoves
        elif pieceName == "B4":
            piecesLegalMoves["B4"] = pieceLegalMoves
        elif pieceName == "B5":
            piecesLegalMoves["B5"] = pieceLegalMoves
        elif pieceName == "b1":
            piecesLegalMoves["b1"] = pieceLegalMoves
        elif pieceName == "b2":
            piecesLegalMoves["b2"] = pieceLegalMoves
        elif pieceName == "b3":
            piecesLegalMoves["b3"] = pieceLegalMoves
        elif pieceName == "b4":
            piecesLegalMoves["b4"] = pieceLegalMoves
        elif pieceName == "b5":
            piecesLegalMoves["b5"] = pieceLegalMoves
        return piecesLegalMoves

    def getBLegalMoves(self, board, piecePosition, player):
        moves = [] # list e.g [[1, 2], [1, 3]]
        pieceColumn = piecePosition[0]
        pieceRow = piecePosition[1]
        BUpPosition = [pieceColumn, pieceRow - 1]
        BDownPosition = [pieceColumn, pieceRow + 1]
        BLeftPosition = [pieceColumn - 1, pieceRow]
        BRightPosition = [pieceColumn + 1, pieceRow]
        if self.checkBUpPosition(BUpPosition, board, player) \
                and player == "Red":
            moves.append(BUpPosition)
        if self.checkBDownPosition(BDownPosition, board, player) \
                and player == "Black":
            moves.append(BDownPosition)
        if self.checkBLeftPosition(BLeftPosition, board, player) \
                and self.isCrossRiver(BLeftPosition[1], player):
            moves.append(BLeftPosition)
        if self.checkBRightPosition(BRightPosition, board, player) \
                and self.isCrossRiver(BRightPosition[1], player):
            moves.append(BRightPosition)
        return moves

    def checkBRightPosition(self, BRightPosition, board, player):
        if self.isOutOfBoard(BRightPosition[0], BRightPosition[1]):
            return False
        destination = board[BRightPosition[1]][BRightPosition[0]]
        if destination != '':
            if ((destination in InitPieces.blackPieces and player == "Red")
                    or (destination in InitPieces.redPieces and player == "Black")):
                return True
            return False
        return True

    def checkBLeftPosition(self, BLeftPosition, board, player):
        if self.isOutOfBoard(BLeftPosition[0], BLeftPosition[1]):
            return False
        destination = board[BLeftPosition[1]][BLeftPosition[0]]
        if destination != '':
            if ((destination in InitPieces.blackPieces and player == "Red")
                    or (destination in InitPieces.redPieces and player == "Black")):
                return True
            return False
        return True

    def checkBUpPosition(self, BUpPosition, board, player):
        if self.isOutOfBoard(BUpPosition[0], BUpPosition[1]):
            return False
        destination = board[BUpPosition[1]][BUpPosition[0]]
        if destination != '':
            if ((destination in InitPieces.blackPieces and player == "Red")
                    or (destination in InitPieces.redPieces and player == "Black")):
                return True
            return False
        return True

    def checkBDownPosition(self, BDownPosition, board, player):
        if self.isOutOfBoard(BDownPosition[0], BDownPosition[1]):
            return False
        destination = board[BDownPosition[1]][BDownPosition[0]]
        if destination != '':
            if ((destination in InitPieces.blackPieces and player == "Red")
                    or (destination in InitPieces.redPieces and player == "Black")):
                return True
            return False
        return True

    def setPiecesLegalMovesForP(self, piecesLegalMoves, pieceName, board, piecePosition, player):
        pieceLegalMoves = self.getPLegalMoves(board, piecePosition, player)
        if pieceName == "P1":
            piecesLegalMoves["P1"] = pieceLegalMoves
        elif pieceName == "P2":
            piecesLegalMoves["P2"] = pieceLegalMoves
        elif pieceName == "p1":
            piecesLegalMoves["p1"] = pieceLegalMoves
        elif pieceName == "p2":
            piecesLegalMoves["p2"] = pieceLegalMoves
        return piecesLegalMoves

    def getPLegalMoves(self, board, piecePosition, player):
        moves = []
        pieceColumn = piecePosition[0]
        pieceRow = piecePosition[1]
        movesOnRow = self.getPLegalMovesOnRow(board, pieceColumn, pieceRow, player)
        movesOnColumn = self.getPLegalMovesOnColumn(board, pieceColumn, pieceRow, player)
        for move in movesOnRow:
            moves.append(move)
        for move in movesOnColumn:
            moves.append(move)
        return moves

    def getPLegalMovesOnRow(self, board, pieceColumn, pieceRow, player):
        moves = []
        counter = 0
        for column in range(pieceColumn - 1, self.minColumn - 1, -1):
            destination = board[pieceRow][column]
            if destination != '':
                counter += 1
                if counter == 2:
                    if ((destination in InitPieces.blackPieces and player == "Red")
                            or (destination in InitPieces.redPieces and player == "Black")):
                        moves.append([column, pieceRow])
                    break
            if counter == 0:
                moves.append([column, pieceRow])
        counter = 0
        for column in range(pieceColumn + 1, self.maxColumn + 1):
            destination = board[pieceRow][column]
            if destination != '':
                counter += 1
                if counter == 2:
                    if ((destination in InitPieces.blackPieces and player == "Red")
                            or (destination in InitPieces.redPieces and player == "Black")):
                        moves.append([column, pieceRow])
                    break
            if counter == 0:
                moves.append([column, pieceRow])
        return moves

    def getPLegalMovesOnColumn(self, board, pieceColumn, pieceRow, player):
        moves = []
        counter = 0
        for row in range(pieceRow - 1, self.minRow - 1, -1):
            destination = board[row][pieceColumn]
            if destination != '':
                counter += 1
                if counter == 2:
                    if ((destination in InitPieces.blackPieces and player == "Red")
                            or (destination in InitPieces.redPieces and player == "Black")):
                        moves.append([pieceColumn, row])
                    break
            if counter == 0:
                moves.append([pieceColumn, row])
        counter = 0
        for row in range(pieceRow + 1, self.maxRow + 1):
            destination = board[row][pieceColumn]
            if destination != '':
                counter += 1
                if counter == 2:
                    if ((destination in InitPieces.blackPieces and player == "Red")
                            or (destination in InitPieces.redPieces and player == "Black")):
                        moves.append([pieceColumn, row])
                    break
            if counter == 0:
                moves.append([pieceColumn, row])
        return moves
        pass

    def setPiecesLegalMovesForK(self, piecesLegalMoves, pieceName, board, piecePosition, player):
        pieceLegalMoves = self.getKLegalMoves(board, piecePosition, player)
        if pieceName == "K":
            piecesLegalMoves["K"] = pieceLegalMoves
        elif pieceName == "k":
            piecesLegalMoves["k"] = pieceLegalMoves
        return piecesLegalMoves

    def getKLegalMoves(self, board, piecePosition, player):
        moves = []
        pieceColumn = piecePosition[0]
        pieceRow = piecePosition[1]
        KUpPosition = [pieceColumn, pieceRow - 1]
        KDownPosition = [pieceColumn, pieceRow + 1]
        KLeftPosition = [pieceColumn - 1, pieceRow]
        KRightPosition = [pieceColumn + 1, pieceRow]
        if self.checkKUpPosition(KUpPosition, board, player) \
                and not self.isOutOfTian(KUpPosition[0], KUpPosition[1], player):
            moves.append(KUpPosition)
        if self.checkKDownPosition(KDownPosition, board, player) \
                and not self.isOutOfTian(KDownPosition[0], KDownPosition[1], player):
            moves.append(KDownPosition)
        if self.checkKLeftPosition(KLeftPosition, board, player) \
                and not self.isOutOfTian(KLeftPosition[0], KLeftPosition[1], player):
            moves.append(KLeftPosition)
        if self.checkKRightPosition(KRightPosition, board, player) \
                and not self.isOutOfTian(KRightPosition[0], KRightPosition[1], player):
            moves.append(KRightPosition)
        return moves

    def checkKUpPosition(self, KUpPosition, board, player):
        if self.isOutOfBoard(KUpPosition[0], KUpPosition[1]):
            return False
        destination = board[KUpPosition[1]][KUpPosition[0]]
        if destination != '':
            if ((destination in InitPieces.blackPieces and player == "Red")
                    or (destination in InitPieces.redPieces and player == "Black")):
                return True
            return False
        return True

    def checkKDownPosition(self, KDownPosition, board, player):
        if self.isOutOfBoard(KDownPosition[0], KDownPosition[1]):
            return False
        destination = board[KDownPosition[1]][KDownPosition[0]]
        if destination != '':
            if ((destination in InitPieces.blackPieces and player == "Red")
                    or (destination in InitPieces.redPieces and player == "Black")):
                return True
            return False
        return True

    def checkKLeftPosition(self, KLeftPosition, board, player):
        if self.isOutOfBoard(KLeftPosition[0], KLeftPosition[1]):
            return False
        destination = board[KLeftPosition[1]][KLeftPosition[0]]
        if destination != '':
            if ((destination in InitPieces.blackPieces and player == "Red")
                    or (destination in InitPieces.redPieces and player == "Black")):
                return True
            return False
        return True

    def checkKRightPosition(self, KRightPosition, board, player):
        if self.isOutOfBoard(KRightPosition[0], KRightPosition[1]):
            return False
        destination = board[KRightPosition[1]][KRightPosition[0]]
        if destination != '':
            if ((destination in InitPieces.blackPieces and player == "Red")
                    or (destination in InitPieces.redPieces and player == "Black")):
                return True
            return False
        return True

    def setPiecesLegalMovesForS(self, piecesLegalMoves, pieceName, board, piecePosition, player):
        pieceLegalMoves = self.getSLegalMoves(board, piecePosition, player)
        if pieceName == "S1":
            piecesLegalMoves["S1"] = pieceLegalMoves
        elif pieceName == "S2":
            piecesLegalMoves["S2"] = pieceLegalMoves
        elif pieceName == "s1":
            piecesLegalMoves["s1"] = pieceLegalMoves
        elif pieceName == "s2":
            piecesLegalMoves["s2"] = pieceLegalMoves
        return piecesLegalMoves

    def getSLegalMoves(self, board, piecePosition, player):
        moves = []
        pieceColumn = piecePosition[0]
        pieceRow = piecePosition[1]
        SUpRightPosition = [pieceColumn + 1, pieceRow - 1]
        SUpLeftPosition = [pieceColumn - 1, pieceRow - 1]
        SDownRightPosition = [pieceColumn + 1, pieceRow + 1]
        SDownLeftPosition = [pieceColumn - 1, pieceRow + 1]
        if self.checkSUpRightPosition(SUpRightPosition, board, player) \
                and not self.isOutOfTian(SUpRightPosition[0], SUpRightPosition[1], player):
            moves.append(SUpRightPosition)
        if self.checkSUpLeftPosition(SUpLeftPosition, board, player) \
                and not self.isOutOfTian(SUpLeftPosition[0], SUpLeftPosition[1], player):
            moves.append(SUpLeftPosition)
        if self.checkSDownRightPosition(SDownRightPosition, board, player) \
                and not self.isOutOfTian(SDownRightPosition[0], SDownRightPosition[1], player):
            moves.append(SDownRightPosition)
        if self.checkSDownLeftPosition(SDownLeftPosition, board, player) \
                and not self.isOutOfTian(SDownLeftPosition[0], SDownLeftPosition[1], player):
            moves.append(SDownLeftPosition)
        return moves

    def checkSUpRightPosition(self, SUpRightPosition, board, player):
        if self.isOutOfBoard(SUpRightPosition[0], SUpRightPosition[1]):
            return False
        destination = board[SUpRightPosition[1]][SUpRightPosition[0]]
        if destination != '':
            if ((destination in InitPieces.blackPieces and player == "Red")
                    or (destination in InitPieces.redPieces and player == "Black")):
                return True
            return False
        return True

    def checkSUpLeftPosition(self, SUpLeftPosition, board, player):
        if self.isOutOfBoard(SUpLeftPosition[0], SUpLeftPosition[1]):
            return False
        destination = board[SUpLeftPosition[1]][SUpLeftPosition[0]]
        if destination != '':
            if ((destination in InitPieces.blackPieces and player == "Red")
                    or (destination in InitPieces.redPieces and player == "Black")):
                return True
            return False
        return True

    def checkSDownRightPosition(self, SDownRightPosition, board, player):
        if self.isOutOfBoard(SDownRightPosition[0], SDownRightPosition[1]):
            return False
        destination = board[SDownRightPosition[1]][SDownRightPosition[0]]
        if destination != '':
            if ((destination in InitPieces.blackPieces and player == "Red")
                    or (destination in InitPieces.redPieces and player == "Black")):
                return True
            return False
        return True

    def checkSDownLeftPosition(self, SDownLeftPosition, board, player):
        if self.isOutOfBoard(SDownLeftPosition[0], SDownLeftPosition[1]):
            return False
        destination = board[SDownLeftPosition[1]][SDownLeftPosition[0]]
        if destination != '':
            if ((destination in InitPieces.blackPieces and player == "Red")
                    or (destination in InitPieces.redPieces and player == "Black")):
                return True
            return False
        return True

    def setPiecesLegalMovesForX(self, piecesLegalMoves, pieceName, board, piecePosition, player):
        pieceLegalMoves = self.getXLegalMoves(board, piecePosition, player)
        if pieceName == "X1":
            piecesLegalMoves["X1"] = pieceLegalMoves
        elif pieceName == "X2":
            piecesLegalMoves["X2"] = pieceLegalMoves
        elif pieceName == "x1":
            piecesLegalMoves["x1"] = pieceLegalMoves
        elif pieceName == "x2":
            piecesLegalMoves["x2"] = pieceLegalMoves
        return piecesLegalMoves

    def getXLegalMoves(self, board, piecePosition, player):
        moves = []
        pieceColumn = piecePosition[0]
        pieceRow = piecePosition[1]
        XUpRightPosition = [pieceColumn + 2, pieceRow - 2]
        XUpLeftPosition = [pieceColumn - 2, pieceRow - 2]
        XDownRightPosition = [pieceColumn + 2, pieceRow + 2]
        XDownLeftPosition = [pieceColumn - 2, pieceRow + 2]
        if self.checkXUpRightPosition(XUpRightPosition, board, player) \
                and not self.isCrossRiver(XUpRightPosition[1], player):
            moves.append(XUpRightPosition)
        if self.checkXUpLeftPosition(XUpLeftPosition, board, player) \
                and not self.isCrossRiver(XUpLeftPosition[1], player):
            moves.append(XUpLeftPosition)
        if self.checkXDownRightPosition(XDownRightPosition, board, player) \
                and not self.isCrossRiver(XDownRightPosition[1], player):
            moves.append(XDownRightPosition)
        if self.checkXDownLeftPosition(XDownLeftPosition, board, player) \
                and not self.isCrossRiver(XDownLeftPosition[1], player):
            moves.append(XDownLeftPosition)
        return moves

    def checkXUpRightPosition(self, XUpRightPosition, board, player):
        if self.isOutOfBoard(XUpRightPosition[0], XUpRightPosition[1]):
            return False
        blockPosition = [XUpRightPosition[0] - 1, XUpRightPosition[1] + 1]
        if board[blockPosition[1]][blockPosition[0]] != '':
            return False
        destination = board[XUpRightPosition[1]][XUpRightPosition[0]]
        if destination != '':
            if ((destination in InitPieces.blackPieces and player == "Red")
                        or (destination in InitPieces.redPieces and player == "Black")):
                return True
            return False
        return True

    def checkXUpLeftPosition(self, XUpLeftPosition, board, player):
        if self.isOutOfBoard(XUpLeftPosition[0], XUpLeftPosition[1]):
            return False
        blockPosition = [XUpLeftPosition[0] + 1, XUpLeftPosition[1] + 1]
        if board[blockPosition[1]][blockPosition[0]] != '':
            return False
        destination = board[XUpLeftPosition[1]][XUpLeftPosition[0]]
        if destination != '':
            if ((destination in InitPieces.blackPieces and player == "Red")
                    or (destination in InitPieces.redPieces and player == "Black")):
                return True
            return False
        return True

    def checkXDownRightPosition(self, XDownRightPosition, board, player):
        if self.isOutOfBoard(XDownRightPosition[0], XDownRightPosition[1]):
            return False
        blockPosition = [XDownRightPosition[0] - 1, XDownRightPosition[1] - 1]
        if board[blockPosition[1]][blockPosition[0]] != '':
            return False
        destination = board[XDownRightPosition[1]][XDownRightPosition[0]]
        if destination != '':
            if ((destination in InitPieces.blackPieces and player == "Red")
                    or (destination in InitPieces.redPieces and player == "Black")):
                return True
            return False
        return True

    def checkXDownLeftPosition(self, XDownLeftPosition, board, player):
        if self.isOutOfBoard(XDownLeftPosition[0], XDownLeftPosition[1]):
            return False
        blockPosition = [XDownLeftPosition[0] + 1, XDownLeftPosition[1] - 1]
        if board[blockPosition[1]][blockPosition[0]] != '':
            return False
        destination = board[XDownLeftPosition[1]][XDownLeftPosition[0]]
        if destination != '':
            if ((destination in InitPieces.blackPieces and player == "Red")
                    or (destination in InitPieces.redPieces and player == "Black")):
                return True
            return False
        return True

    def setPiecesLegalMovesForM(self, piecesLegalMoves, pieceName, board, piecePosition, player):
        pieceLegalMoves = self.getMLegalMoves(board, piecePosition, player)
        if pieceName == "M1":
            piecesLegalMoves["M1"] = pieceLegalMoves
        elif pieceName == "M2":
            piecesLegalMoves["M2"] = pieceLegalMoves
        elif pieceName == "m1":
            piecesLegalMoves["m1"] = pieceLegalMoves
        elif pieceName == "m2":
            piecesLegalMoves["m2"] = pieceLegalMoves
        return piecesLegalMoves

    def getMLegalMoves(self, board, piecePosition, player):
        moves = []
        pieceColumn = piecePosition[0]
        pieceRow = piecePosition[1]
        MUpRightPosition = [pieceColumn + 1, pieceRow - 2]
        MUpLeftPosition = [pieceColumn - 1, pieceRow - 2]
        MDownRightPosition = [pieceColumn + 1, pieceRow + 2]
        MDownLeftPosition = [pieceColumn - 1, pieceRow + 2]
        MRightUpPosition = [pieceColumn + 2, pieceRow - 1]
        MRightDownPosition = [pieceColumn + 2, pieceRow + 1]
        MLeftUpPosition = [pieceColumn - 2, pieceRow - 1]
        MLeftDownPosition = [pieceColumn - 2, pieceRow + 1]
        if self.checkMUpRightPosition(MUpRightPosition, board, player):
            moves.append(MUpRightPosition)
        if self.checkMUpLeftPosition(MUpRightPosition, board, player):
            moves.append(MUpLeftPosition)
        if self.checkMDownRightPosition(MDownRightPosition, board, player):
            moves.append(MDownRightPosition)
        if self.checkMDownLeftPosition(MDownLeftPosition, board, player):
            moves.append(MDownLeftPosition)
        if self.checkMRightUpPosition(MRightUpPosition, board, player):
            moves.append(MRightUpPosition)
        if self.checkMRightDownPosition(MRightDownPosition, board, player):
            moves.append(MRightDownPosition)
        if self.checkMLeftUpPosition(MLeftUpPosition, board, player):
            moves.append(MLeftUpPosition)
        if self.checkMLeftDownPosition(MLeftDownPosition, board, player):
            moves.append(MLeftDownPosition)
        return moves

    def checkMUpRightPosition(self, MUpRightPosition, board, player):
        if self.isOutOfBoard(MUpRightPosition[0], MUpRightPosition[1]):
            return False
        blockPosition = [MUpRightPosition[0] - 1, MUpRightPosition[1] + 1]
        if self.isOutOfBoard(blockPosition[0], blockPosition[1]):
            return False
        if board[blockPosition[1]][blockPosition[0]] != '':
            return False
        destination = board[MUpRightPosition[1]][MUpRightPosition[0]]
        if destination != '':
            if ((destination in InitPieces.blackPieces and player == "Red")
                    or (destination in InitPieces.redPieces and player == "Black")):
                return True
            return False
        return True

    def checkMUpLeftPosition(self, MUpLeftPosition, board, player):
        if self.isOutOfBoard(MUpLeftPosition[0], MUpLeftPosition[1]):
            return False
        blockPosition = [MUpLeftPosition[0] + 1, MUpLeftPosition[1] + 1]
        if self.isOutOfBoard(blockPosition[0], blockPosition[1]):
            return False
        if board[blockPosition[1]][blockPosition[0]] != '':
            return False
        destination = board[MUpLeftPosition[1]][MUpLeftPosition[0]]
        if destination != '':
            if ((destination in InitPieces.blackPieces and player == "Red")
                    or (destination in InitPieces.redPieces and player == "Black")):
                return True
            return False
        return True

    def checkMDownRightPosition(self, MDownRightPosition, board, player):
        if self.isOutOfBoard(MDownRightPosition[0], MDownRightPosition[1]):
            return False
        blockPosition = [MDownRightPosition[0] - 1, MDownRightPosition[1] - 1]
        if self.isOutOfBoard(blockPosition[0], blockPosition[1]):
            return False
        if board[blockPosition[1]][blockPosition[0]] != '':
            return False
        destination = board[MDownRightPosition[1]][MDownRightPosition[0]]
        if destination != '':
            if ((destination in InitPieces.blackPieces and player == "Red")
                    or (destination in InitPieces.redPieces and player == "Black")):
                return True
            return False
        return True

    def checkMDownLeftPosition(self, MDownLeftPosition, board, player):
        if self.isOutOfBoard(MDownLeftPosition[0], MDownLeftPosition[1]):
            return False
        blockPosition = [MDownLeftPosition[0] + 1, MDownLeftPosition[1] - 1]
        if self.isOutOfBoard(blockPosition[0], blockPosition[1]):
            return False
        if board[blockPosition[1]][blockPosition[0]] != '':
            return False
        destination = board[MDownLeftPosition[1]][MDownLeftPosition[0]]
        if destination != '':
            if ((destination in InitPieces.blackPieces and player == "Red")
                    or (destination in InitPieces.redPieces and player == "Black")):
                return True
            return False
        return True

    def checkMRightUpPosition(self, MRightUpPosition, board, player):
        if self.isOutOfBoard(MRightUpPosition[0], MRightUpPosition[1]):
            return False
        blockPosition = [MRightUpPosition[0] - 1, MRightUpPosition[1] + 1]
        if self.isOutOfBoard(blockPosition[0], blockPosition[1]):
            return False
        if board[blockPosition[1]][blockPosition[0]] != '':
            return False
        destination = board[MRightUpPosition[1]][MRightUpPosition[0]]
        if destination != '':
            if ((destination in InitPieces.blackPieces and player == "Red")
                    or (destination in InitPieces.redPieces and player == "Black")):
                return True
            return False
        return True

    def checkMRightDownPosition(self, MRightDownPosition, board, player):
        if self.isOutOfBoard(MRightDownPosition[0], MRightDownPosition[1]):
            return False
        blockPosition = [MRightDownPosition[0] - 1, MRightDownPosition[1] - 1]
        if self.isOutOfBoard(blockPosition[0], blockPosition[1]):
            return False
        if board[blockPosition[1]][blockPosition[0]] != '':
            return False
        destination = board[MRightDownPosition[1]][MRightDownPosition[0]]
        if destination != '':
            if ((destination in InitPieces.blackPieces and player == "Red")
                    or (destination in InitPieces.redPieces and player == "Black")):
                return True
            return False
        return True

    def checkMLeftUpPosition(self, MLeftUpPosition, board, player):
        if self.isOutOfBoard(MLeftUpPosition[0], MLeftUpPosition[1]):
            return False
        blockPosition = [MLeftUpPosition[0] + 1, MLeftUpPosition[1] + 1]
        if self.isOutOfBoard(blockPosition[0], blockPosition[1]):
            return False
        if board[blockPosition[1]][blockPosition[0]] != '':
            return False
        destination = board[MLeftUpPosition[1]][MLeftUpPosition[0]]
        if destination != '':
            if ((destination in InitPieces.blackPieces and player == "Red")
                    or (destination in InitPieces.redPieces and player == "Black")):
                return True
            return False
        return True

    def checkMLeftDownPosition(self, MLeftDownPosition, board, player):
        if self.isOutOfBoard(MLeftDownPosition[0], MLeftDownPosition[1]):
            return False
        blockPosition = [MLeftDownPosition[0] + 1, MLeftDownPosition[1] - 1]
        if self.isOutOfBoard(blockPosition[0], blockPosition[1]):
            return False
        if board[blockPosition[1]][blockPosition[0]] != '':
            return False
        destination = board[MLeftDownPosition[1]][MLeftDownPosition[0]]
        if destination != '':
            if ((destination in InitPieces.blackPieces and player == "Red")
                    or (destination in InitPieces.redPieces and player == "Black")):
                return True
            return False
        return True

    @classmethod
    def setPiecesLegalMovesForJ(self, piecesLegalMoves, pieceName, board, piecePosition, player):
        pieceLegalMoves = self.getJLegalMoves(board, piecePosition, player)
        if pieceName == "J1":
            piecesLegalMoves["J1"] = pieceLegalMoves
        elif pieceName == "j1":
            piecesLegalMoves["j1"] = pieceLegalMoves
        elif pieceName == "J2":
            piecesLegalMoves["J2"] = pieceLegalMoves
        elif pieceName == "j2":
            piecesLegalMoves["j2"] = pieceLegalMoves
        return piecesLegalMoves
    @classmethod
    def getJLegalMovesOnRow(self, board, pieceColumn, pieceRow, player):
        moves = []
        for column in range(pieceColumn - 1, self.minColumn - 1, -1):
            destination = board[pieceRow][column]
            if destination != '':
                if ((destination in InitPieces.blackPieces and player == "Red")
                        or (destination in InitPieces.redPieces and player == "Black")):
                    moves.append([column, pieceRow])
                break
            moves.append([column, pieceRow])

        for column in range(pieceColumn + 1, self.maxColumn + 1):
            destination = board[pieceRow][column]
            if destination != '':
                if ((destination in InitPieces.blackPieces and player == "Red")
                        or (destination in InitPieces.redPieces and player == "Black")):
                    moves.append([column, pieceRow])
                break
            moves.append([column, pieceRow])
        return moves

    @classmethod
    def getJLegalMoves(self, board, piecePosition, player):
        moves = []
        pieceColumn = piecePosition[0]
        pieceRow = piecePosition[1]
        movesOnRow = self.getJLegalMovesOnRow(board, pieceColumn, pieceRow, player)
        movesOnColumn = self.getJLegalMovesOnColumn(board, pieceColumn, pieceRow, player)
        for move in movesOnRow:
            moves.append(move)
        for move in movesOnColumn:
            moves.append(move)
        return moves
    @classmethod
    def getJLegalMovesOnColumn(self, board, pieceColumn, pieceRow, player):
        moves = []
        for row in range(pieceRow - 1, self.minRow - 1, -1):
            destination = board[row][pieceColumn]
            if destination != '':
                if ((destination in InitPieces.blackPieces and player == "Red")
                        or (destination in InitPieces.redPieces and player == "Black")):
                    moves.append([pieceColumn, row])
                break
            moves.append([pieceColumn, row])

        for row in range(pieceRow + 1, self.maxColumn + 1):
            destination = board[row][pieceColumn]
            if destination != '':
                if ((destination in InitPieces.blackPieces and player == "Red")
                        or (destination in InitPieces.redPieces and player == "Black")):
                    moves.append([pieceColumn, row])
                break
            moves.append([pieceColumn, row])
        return moves

    def isOutOfBoard(self, destinationColumn, destinationRow):
        if destinationColumn > self.maxColumn or destinationRow < self.minRow \
                or destinationColumn < self.minColumn or destinationRow > self.maxRow:
            return True
        return False

    def isCrossRiver(self, destinationRow, player):
        if player == "Red" and destinationRow < self.lowRiverRow:
            return True
        elif player == "Black" and destinationRow > self.upRiverRow:
            return True
        return False

    def isOutOfTian(self, destinationColumn, destinationRow, player):
        if player == "Red":
            if destinationColumn < self.redTianMinColumn \
                    or destinationColumn > self.redTianMaxColumn \
                    or destinationRow < self.redTianMinRow \
                    or destinationRow > self.redTianMaxRow:
                return True
        elif player == "Black":
            if destinationColumn < self.blackTianMinColumn \
                    or destinationColumn > self.blackTianMaxColumn \
                    or destinationRow > self.blackTianMaxRow \
                    or destinationRow < self.blackTianMinRow:
                return True
