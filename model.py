class GameState:
    gameNotOver = True
    playerXTurn = True
    theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                'bot-L': ' ', 'bot-M': ' ', 'bot-R': ' '
                }
    spotTaken = False


def computeNextTurn(posInput):
    if GameState.theBoard[posInput] == ' ':
        if (GameState.playerXTurn):
            GameState.theBoard[posInput] = 'X'
        else:
            GameState.theBoard[posInput] = 'O'
        GameState.playerXTurn = not GameState.playerXTurn
        return "marked"
    else:
        return


# printBoard(theBoard)
# Game loop
# while gameNotOver:
# executeNextTurn()
# printBoard(theBoard)
