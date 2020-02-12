class GameState:
    gameOver = False
    winner = ""
    playerXTurn = True
    spotTaken = False
    theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                'bot-L': ' ', 'bot-M': ' ', 'bot-R': ' '
                }


def computeIfWinner():
    boardList = [
        GameState.theBoard['top-L'], GameState.theBoard['top-M'], GameState.theBoard['top-R'],
        GameState.theBoard['mid-L'], GameState.theBoard['mid-M'], GameState.theBoard['mid-R'],
        GameState.theBoard['bot-L'], GameState.theBoard['bot-M'], GameState.theBoard['bot-R']
    ]
    if ((boardList[0], boardList[1], boardList[2]) == ("O", "O", "O") or
        (boardList[6], boardList[7], boardList[8]) == ("O", "O", "O") or
        (boardList[0], boardList[3], boardList[6]) == ("O", "O", "O") or
        (boardList[1], boardList[4], boardList[7]) == ("O", "O", "O") or
        (boardList[3], boardList[4], boardList[5]) == ("O", "O", "O") or
        (boardList[2], boardList[5], boardList[8]) == ("O", "O", "O") or
        (boardList[0], boardList[4], boardList[8]) == ("O", "O", "O") or
            (boardList[6], boardList[4], boardList[2]) == ("O", "O", "O")):
        return "X"
    elif ((boardList[0], boardList[1], boardList[2]) == ("X", "X", "X") or
          (boardList[3], boardList[4], boardList[5]) == ("X", "X", "X") or
          (boardList[6], boardList[7], boardList[8]) == ("X", "X", "X") or
          (boardList[0], boardList[3], boardList[6]) == ("X", "X", "X") or
          (boardList[1], boardList[4], boardList[7]) == ("X", "X", "X") or
          (boardList[2], boardList[5], boardList[8]) == ("X", "X", "X") or
          (boardList[0], boardList[4], boardList[8]) == ("X", "X", "X") or
          (boardList[6], boardList[4], boardList[2]) == ("X", "X", "X")):
        return "O"
    elif " " not in boardList:
        return "draw"
    else:
        return ""


def computeNextTurn(posInput):
    if GameState.theBoard[posInput] == ' ':
        if (GameState.playerXTurn):
            GameState.theBoard[posInput] = 'X'
        else:
            GameState.theBoard[posInput] = 'O'
        GameState.playerXTurn = not GameState.playerXTurn
        GameState.winner = computeIfWinner()
        return "marked"
    else:
        return


# printBoard(theBoard)
# Game loop
# while gameNotOver:
# executeNextTurn()
# printBoard(theBoard)
