from game_theory import Game
from numpy import array


# A = [[1, 0, -1, 1], [2, 2, -2, 0], [4, 1, 3, 2], [5, -1, 1, 1], [3, 2, 1, -2]]
# X = [[0.2, 0.3, 0.2, 0.2], [0.1, 0.3, 0.2, 0.3], [0.4, 0.3, 0.5, 0.2], [0.3, 0.1, 0.1, 0.3]]
A = [[2, 11, 5], [6, 5, 9], [5, 5, 1]]
X = [[0.13, 0.25, 0.6], [0.51, 0.47, 0.1], [0.36, 0.28, 0.3]]
game = Game(A, X)
# проверка существования решения в чистых стратегиях
# print(game.check_saddle_point())
# Game.print_matrix(game.risk_matrix, 'Матрица риска')
# game.print_criteria_values(0.7)
d = game.function_decision()
print(d)
print(len(d))