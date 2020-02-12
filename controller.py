import model
import view

view.printBoard(model.GameState.theBoard)
view.askWhereToPlayNext()


# Consider getting rid of GameState. "function as a black box"
while 1 < 2:
    playedPos = input()
    if model.computeNextTurn(playedPos) == "marked":
        view.printBoard(model.GameState.theBoard)
        if(model.GameState.winner):
            view.printWinnerMessage(model.GameState.winner)
            break
        view.askWhereToPlayNext()
    else:
        view.askToTryAgain()
