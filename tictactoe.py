gameState = {gameNotOver: True, playerXTurn: True}
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'bot-L': ' ', 'bot-M': ' ', 'bot-R': ' '
            }


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['bot-L'] + '|' + board['bot-M'] + '|' + board['bot-R'])


def executeNextTurn():
    posInput = input("Where do you want to play: ")
    if theBoard[posInput] == ' ':
        if (gameState.playerXTurn):
            theBoard[posInput] = 'X'
        else:
            theBoard[posInput] = 'O'
        playerXTurn = not playerXTurn
    else:
        print("Already Taken... Try again")
        executeNextTurn()


printBoard(theBoard)
# Game loop
while gameNotOver:
    executeNextTurn()
    printBoard(theBoard)
