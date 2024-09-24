This is the code of the minimax algorithm with alpha-beta pruning, which is based on FanZhang's framework. 

In this tic-tac-toe game, human player has options to choose the first player and whether to implement alpha-beta pruning. If the computer player goes first, it will select its first movement randomly. Regardless the initial setting at the beginning of this game, the algorithm will find the most optimal solutions and the results show that human can hardly beat the AI in this game. 

When running Main.py, the agent will display how the squares are numbered, helping users understand how to select their desired square.
1 | 2 | 3
- + - + -
4 | 5 | 6
- + - + -
7 | 8 | 9

Before the game begins, users must answer two questions to configure the game settings:

1. Do you want to use pruning?
Press 1 for "No" or 2 for "Yes." This determines whether the computer player will use the alpha-beta pruning algorithm.
2. Who should start?
Press 1 if the user plays first, or 2 if the computer plays first.
