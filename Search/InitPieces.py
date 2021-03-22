from Search.Piece import Piece
class InitPieces:
    redPieces=["J1","M1","X1","S1","K",
               "S2","X2","M2","J2","P1","P2",
               "B1","B2","B3","B4","B5"]
    blackPieces=["j1","m1","x1","s1","k",
               "s2","x2","m2","j2","p1","p2",
               "b1","b2","b3","b4","b5"]

    def getRedPieces(self):
        return [
            Piece("J1", [0, 9]),
            Piece("M1", [1, 9]),
            Piece("X1", [2, 9]),
            Piece("S1", [3, 9]),
            Piece("K", [4, 9]),
            Piece("S2", [5, 9]),
            Piece("X2", [6, 9]),
            Piece("M2", [7, 9]),
            Piece("J2", [8, 9]),
            Piece("P1", [1, 7]),
            Piece("P2", [7, 7]),
            Piece("B1", [0, 6]),
            Piece("B2", [2, 6]),
            Piece("B3", [4, 6]),
            Piece("B4", [6, 6]),
            Piece("B5", [8, 6])
        ]
    def getBlackPieces(self):
        return [
            Piece("j1", [0, 0]),
            Piece("m1", [1, 0]),
            Piece("x1", [2, 0]),
            Piece("s1", [3, 0]),
            Piece("k",  [4, 0]),
            Piece("s2", [5, 0]),
            Piece("x2", [6, 0]),
            Piece("m2", [7, 0]),
            Piece("j2", [8, 0]),
            Piece("p1", [1, 2]),
            Piece("p2", [7, 2]),
            Piece("b1", [0, 3]),
            Piece("b2", [2, 3]),
            Piece("b3", [4, 3]),
            Piece("b4", [6, 3]),
            Piece("b5", [8, 3])
        ]
    def getBoard(self):
        return [
            ['j1','m1','x1','s1','k','s2','x2','m2','j2'],
            ['', '', '', '', '', '', '', '', ''],
            ['','p1','','','','','','p2',''],
            ['b1','','b2','','b3','','b4','','b5'],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['B1', '', 'B2', '', 'B3', '', 'B4', '', 'B5'],
            ['', 'P1', '', '', '', '', '', 'P2', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['J1','M1','X1','S1','K','S2','X2','M2','J2']
        ]
