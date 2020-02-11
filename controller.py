import model
import view

view.printBoard(model.GameState.theBoard)
view.askWhereToPlayNext()

while 1 < 2:
    playPos = input()
    # if (model.computeNextTurn(playPos)="acceptable")
    if model.computeNextTurn(playPos) == "marked":
        view.printBoard(model.GameState.theBoard)
        view.askWhereToPlayNext()
    else:
        view.askToTryAgain()

# controller askes if requested position:
#   is open
#       - tells view to mark position
#       - tells model to update model
#   is taken
#       - has view ask for another
#
#
#
