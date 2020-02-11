class GameState:
    gameNotOver = True
    playerXTurn = True
    spotTaken = False
    theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                'bot-L': ' ', 'bot-M': ' ', 'bot-R': ' '
                }
    # If X in list of spots win
    # if O in list of spots win
    # if statements for this?


def computeIfWinner():
    boardList = [
        GameState.theBoard['top-L'], GameState.theBoard['top-M'], GameState.theBoard['top-R'],
        GameState.theBoard['mid-L'], GameState.theBoard['mid-M'], GameState.theBoard['mid-R'],
        GameState.theBoard['bot-L'], GameState.theBoard['bot-M'], GameState.theBoard['bot-R']
    ]
    print(boardList)


def computeNextTurn(posInput):
    if GameState.theBoard[posInput] == ' ':
        if (GameState.playerXTurn):
            GameState.theBoard[posInput] = 'X'
        else:
            GameState.theBoard[posInput] = 'O'
        GameState.playerXTurn = not GameState.playerXTurn
        computeIfWinner()
        return "marked"
    else:
        return


# printBoard(theBoard)
# Game loop
# while gameNotOver:
# executeNextTurn()
# printBoard(theBoard)
