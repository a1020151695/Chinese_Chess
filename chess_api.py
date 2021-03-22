import csv
from flask import Flask, jsonify, request, abort
from flask_cors import *
from Search.abSearch import ABSearch
from Search.State import State
import copy

app = Flask(__name__)
move_red = []
move_black = []
CORS(app, supports_credentials=True)
abSearch = ABSearch()
with open('chessred_wc2.csv') as f:  # 移动黑子
    reader = csv.reader(f)
    for i in reader:
        move_black.append(i)

@app.route('/suggest/<string:state64>/<int:flag>')
def login(state64: str = None, flag: int = None):
    if flag == 1:
        move = getMoveForBlackByWordsCount(state64)
        if move is not None:
            return jsonify([{
                'move': move
            }])
        move = getMoveForBlackBySearch(state64)
        return jsonify([{
            'move': move
        }])
    else:
        move = getMoveForBlackFirstBySearch(state64)
        return jsonify([{
            'move': move
        }])

def getMoveForBlackByWordsCount(state64):
    for x in move_black:
        if x[0] == state64:
            print("words count result:" + x[1])
            return x[1]
    return None

def getMoveForBlackBySearch(state64):
    stateForRed = State("Black", "Red")
    stateForRed.updateBoardState(state64)
    board = copy.deepcopy(stateForRed.board)
    searchResult = abSearch.dfsSearch(stateForRed, 2, float("inf"), float("-inf"))
    print("search result:" + str(searchResult))
    return abSearch.getMoveForApi(board, searchResult)

def getMoveForBlackFirstBySearch(state64):
    stateForRed = State("Black", "Red")
    stateForRed.updateBoardState(state64)
    board = copy.deepcopy(stateForRed.board)
    searchResult = abSearch.dfsSearch(stateForRed, 2, float("-inf"), float("inf"))
    print("search result:" + str(searchResult))
    return abSearch.getMoveForApi(board, searchResult)

app.run(debug=True)
