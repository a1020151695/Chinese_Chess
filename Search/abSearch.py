from Search.State import State
from Search.Rule import Rule


class ABSearch:
    Rule = Rule()

    def dfsSearch(self, state, depth, alpha, beta):  # return [score,[pieceName,destination]]
        endState = state.isEndState()
        if endState != 0:
            if self.isRedKOver(endState):
                return [float("-inf"), None]
            elif self.isBlackKOver(endState):
                return [float("inf"), None]
        if state.isKingOnSameRow():
            if state.player == "Red":
                return [float("inf"), None]
            elif state.player == "Black":
                return [float("-inf"), None]
        piecesLegalMoves = None  # e.g {"J1" : [[1, 2],[1, 3]]}
        isMax = False
        if state.player == state.agent:
            isMax = True
        if depth == 0:
            return [self.getValueOfState(state), None]
        if state.player == "Red":
            piecesLegalMoves = self.Rule.getLegalMoves(state, state.redPieces)
        elif state.player == "Black":
            piecesLegalMoves = self.Rule.getLegalMoves(state, state.blackPieces)
        childEvalue = []
        for pieceName in piecesLegalMoves:
            for move in piecesLegalMoves[pieceName]:  # move e.g [1,2]
                nextState = state.getNextState(pieceName, move)
                scoreOfMove = [self.dfsSearch(nextState, depth - 1, alpha, beta)[0], [pieceName, move]]
                childEvalue.append(scoreOfMove)
                if isMax:
                    alpha = max(alpha, scoreOfMove[0])
                    if beta <= alpha:
                        return scoreOfMove
                else:
                    beta = min(beta, scoreOfMove[0])
                    if beta <= alpha:
                        return scoreOfMove
        scores = []
        for node in childEvalue:
            scores.append(node[0])
        if isMax:
            maxEvalue = max(scores)
        else:
            maxEvalue = min(scores)
        for node in childEvalue:
            if node[0] == maxEvalue:
                return node

    def getValueOfState(self, state):
        return state.getScoreOfRed() - state.getScoreOfBlack()

    def isBlackKOver(self, endState):
        if endState == 1:
            return True
        return False

    def getMoveForApi(self, board, move):
        # print("board in api:")
        # print(board)
        for row in range(10):
            for column in range(9):
                if board[row][column] == move[1][0]:
                    move = str(column) + str(row) + str(move[1][1][0]) + str(move[1][1][1])
                    # print("for api: " + move)
                    return move

        return "9999"

    def isRedKOver(self, endState):
        if endState == -1:
            return True
        return False
