from game_theory import Game
from numpy import array

A = [[2, 11, 5], [6, 5, 9], [5, 5, 1]]  # Моя игра
X = [[0.72, 0.27, 0.3], [0.14, 0.53, 0.09], [0.14, 0.2, 0.61]]
q = [0.3, 0.4, 0.3]

# A = [[100, 30, -30], [0, 0, 0]]
# X = [[0.7, 0.3, 0.1], [0.2, 0.5, 0.2], [0.1, 0.2, 0.7]]


game = Game(A, X)
# проверка существования решения в чистых стратегиях
print(game.check_saddle_point())
Game.print_matrix(game.risk_matrix, 'Матрица риска')
game.print_criteria_values(0.7)

print('Цена игры без эксперимента', game.price_without_experience(q))
risk_func = game.get_risk_function()
Game.print_matrix(risk_func, 'Функция риска R')
Game.print_matrix(game.loss_function, 'Функция потерь L')
print('Минимальное значение функции Байеса', game.get_min_value_from_baiesian_function(q))
print('Цена игры', game.get_game_price(0.02, risk_func))
# game.print_matrix(game.get_decision_function(),'функции решения')
