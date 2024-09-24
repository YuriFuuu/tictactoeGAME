#class that implements the MiniMax algorithm.
import math
from TicTacToeAction import TicTacToeAction

class MiniMax:
    def __init__(self):
        self.numberOfStates=0 #< counter to measure the number of iterations / states.
        self.usePruning=False

    # Start procedure of the MiniMax algorithm.
    # state: The state where the MiniMax algorithm starts searching
    # usePruning: Whether to use alpha - beta - pruning
    # return An optimal action to be taken at this point.
    def MinimaxDecision(self,state, usePruning):
        self.usePruning = usePruning
        self.numberOfStates = 0
        ### But I fail to select one of them randomly here ###
        best_action, _ = self.MaxValue(state, -math.inf, math.inf)
        print("State space size:", self.numberOfStates)
        return best_action

    # state: The current state to be evaluated
    # alpha: The current value for alpha
    # beta: The current value for beta
    # return The minimum of the utilites invoking MaxValue, or the utility of the state if it is a leaf.
    def MinValue(self, state, alpha, beta):
        self.numberOfStates += 1

        # To check if the game is over
        if state.isTerminal():
            return None, state.getUtility()
        
        # Implement the MinValue procedure according to the pseudo code
        value = +math.inf
        best_action = None
        for action in state.getActions():
            new_state = state.getResult(action)
            _, max_value = self.MaxValue(new_state, alpha, beta)
            if max_value < value:
                value = max_value
                best_action = action
            if self.usePruning:
                if value <= alpha:
                    return best_action, value
                beta = min(beta, value)
        return best_action, value
    
    # state: The current state to be evaluated
    # alpha: The current value for alpha
    # beta: The current value for beta
    # The maximum of the utilites invoking MinValue, or the utility of the state if it is a leaf.
    def MaxValue(self,state,alpha,beta):
        self.numberOfStates += 1

        # To check if the game is over        
        if state.isTerminal():
            return None, state.getUtility()
        
        # Implement the MaxValue procedure according to the pseudo code
        value = -math.inf
        best_action = None
        for action in state.getActions():
            new_state = state.getResult(action)
            _, min_value = self.MinValue(new_state, alpha, beta)
            if min_value > value:
                value = min_value
                best_action = action
            if self.usePruning:
                if value >= beta:
                    return best_action, value
                alpha = max(alpha, value)
        return best_action, value