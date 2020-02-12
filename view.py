

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['bot-L'] + '|' + board['bot-M'] + '|' + board['bot-R'])


def askWhereToPlayNext():
    print("Where do you want to play: ")


def printWinnerMessage(winner):
    if(winner == "X" or winner == "O"):
        print(f"{winner} is the winner!")
    else:
        print("draw :(")


def askToTryAgain():
    print("Sorry, Already Taken!\n Try again: ")
