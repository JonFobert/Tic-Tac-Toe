import model
import view

view.printBoard(model.GameState.theBoard)
view.askWhereToPlayNext()

while 1 < 2:
    playPos = input()
    # if (model.computeNextTurn(playPos)="acceptable")
    if model.computeNextTurn(playPos) == "marked":
        view.printBoard(model.GameState.theBoard)
        if(model.GameState.winner):
            view.printWinnerMessage(model.GameState.winner)
            break
        view.askWhereToPlayNext()
    else:
        view.askToTryAgain()
