#class that implements a state and the playing logic of the TicTacToe game.
import Square
from TicTacToeAction import TicTacToeAction

class TicTacToeState:
    # Updates the utility value.
    def updateUtility(self):
        # List all the possible rows
        same_marks = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
        
        # Give utility values to three marks in a row, a column or a diagonal.
        # Check which player gets three marks together 
        for i in range(len(same_marks)):
            x = same_marks[i][0]
            y = same_marks[i][1]
            z = same_marks[i][2] 
            if Square.O == self.field[x] == self.field[y] == self.field[z]:
                self.utility = -1
                return
            elif Square.X == self.field[x] == self.field[y] == self.field[z]:
                self.utility = 1
                return

    # Default constructor.
    def __init__(self):
        self.field = [] # < The field, consisting of nine squares.First three values correspond to first row, and so on.
        for i in range(9):
            self.field.append(Square.EMPTY)
        self.player = Square.X # < The player, either X or O.
        self.playerToMove = Square.X # < The player that is about to move.
        self.utility = 0 # < The utility value of this state.Can be 0, 1 (won) or -1 (lost).

    def getActions(self):
        # Build the list to store the actions of players
        actions = []
        for i in range(9):
            if self.field[i] == Square.EMPTY:
                actions.append(TicTacToeAction(self.playerToMove, i))
        return actions

    def getUtility(self):
        return self.utility

    def getResult(self,action):
        # The player to move must be switched. Then incorporate the action into the field of the new state.
        # Copy the contents of the current state, field and player
        new_state = TicTacToeState()
        new_state.field = list(self.field)
        new_state.player = self.player

        # To switch two players
        if self.playerToMove == Square.O:
            new_state.playerToMove = Square.X
        else:
            new_state.playerToMove = Square.O

        
        # Players can go actions in empty squares
        if self.field[action.getPosition()] == Square.EMPTY:
            new_state.field[action.getPosition()] = action.getPlayer()

        # Compute the utility of the new state
        new_state.updateUtility()
        return new_state

    def  isTerminal(self):
        # If the value result is 1 or -1, then the game is over
        if self.utility != 0:
            return True

        # If all the squres have actions, then the game is also over
        if all(square != Square.EMPTY for square in self.field):
            return True
        return False # In other cases, the game is not over

    def printresult(self):
        s = "" + self.field[0] + "|" + self.field[1] + "|" + self.field[2] + "\n"
        s += "-+-+-\n"
        s += self.field[3] + "|" + self.field[4] + "|" + self.field[5] + "\n"
        s += "-+-+-\n"
        s += self.field[6] + "|" + self.field[7] + "|" + self.field[8] + "\n"
        print(s)