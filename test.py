import random
import math

class Square:
    EMPTY = ' '
    X = 'X'
    O = 'O'

class TicTacToeAction:
    def __init__(self, player, position):
        self.player = player
        self.position = position

    def getPosition(self):
        return self.position

    def getPlayer(self):
        return self.player

class TicTacToeState:
    def __init__(self):
        self.field = [Square.EMPTY] * 9
        self.player = Square.X
        self.playerToMove = Square.X
        self.utility = 0

    def getActions(self):
        actions = []
        for i in range(9):
            if self.field[i] == Square.EMPTY:
                actions.append(TicTacToeAction(self.playerToMove, i))
        return actions

    def getUtility(self):
        return self.utility

    def updateUtility(self):
        # Check for win conditions
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]

        for condition in win_conditions:
            if self.field[condition[0]] == self.field[condition[1]] == self.field[condition[2]]:
                if self.field[condition[0]] == Square.X:
                    self.utility = 1
                elif self.field[condition[0]] == Square.O:
                    self.utility = -1

    def getResult(self, action):
        new_state = TicTacToeState()
        new_state.field = list(self.field)  # Copy the current field
        new_state.player = self.player
        new_state.playerToMove = Square.X if self.playerToMove == Square.O else Square.O

        if self.field[action.getPosition()] == Square.EMPTY:
            new_state.field[action.getPosition()] = action.getPlayer()
        new_state.updateUtility()
        return new_state

    def isTerminal(self):
        return self.utility != 0 or all(square != Square.EMPTY for square in self.field)

    def printResult(self):
        s = f"{self.field[0]}|{self.field[1]}|{self.field[2]}\n-+-+-\n{self.field[3]}|{self.field[4]}|{self.field[5]}\n-+-+-\n{self.field[6]}|{self.field[7]}|{self.field[8]}\n"
        print(s)

class MiniMax:
    def __init__(self):
        self.numberOfStates = 0
        self.usePruning = False

    def MinimaxDecision(self, state, usePruning):
        self.usePruning = usePruning
        self.numberOfStates = 0
        best_action, _ = self.maxValue(state, -math.inf, math.inf)
        print("State space size:", self.numberOfStates)
        return best_action

    def minValue(self, state, alpha, beta):
        self.numberOfStates += 1
        if state.isTerminal():
            return None, state.getUtility()

        v = math.inf
        best_action = None
        for action in state.getActions():
            new_state = state.getResult(action)
            _, max_val = self.maxValue(new_state, alpha, beta)
            if max_val < v:
                v = max_val
                best_action = action
            if self.usePruning:
                if v <= alpha:
                    return best_action, v
                beta = min(beta, v)
        return best_action, v

    def maxValue(self, state, alpha, beta):
        self.numberOfStates += 1
        if state.isTerminal():
            return None, state.getUtility()

        v = -math.inf
        best_action = None
        for action in state.getActions():
            new_state = state.getResult(action)
            _, min_val = self.minValue(new_state, alpha, beta)
            if min_val > v:
                v = min_val
                best_action = action
            if self.usePruning:
                if v >= beta:
                    return best_action, v
                alpha = max(alpha, v)
        return best_action, v

if __name__ == '__main__':
    print("The squares are numbered as follows:")
    print("1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9\n")
    mark = False
    print("Do you want to use pruning? 1=no 2=yes ")
    use = int(input())
    if use == 2:
        mark = True
    print("Who should start? 1=you 2=computer ")
    temp = int(input())
    s = TicTacToeState()
    s.player = Square.X
    if temp == 1:
        s.playerToMove = Square.O
    else:
        s.playerToMove = Square.X
    while True:
        if s.playerToMove == Square.X:
            minimax = MiniMax()
            s = s.getResult(minimax.MinimaxDecision(s, mark))
        else:
            print("Which square do you want to set? (1--9) ")
            while True:
                temp = int(input())
                if 1 <= temp <= 9:
                    break
            a = TicTacToeAction(Square.O, temp - 1)
            s = s.getResult(a)
        s.printResult()
        if s.isTerminal():
            break
    if s.getUtility() > 0:
        print("You lost")
    elif s.getUtility() < 0:
        print("You win")
    else:
        print("Draw")
