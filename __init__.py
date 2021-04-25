import numpy

from game_theory import Game
from numpy import array

A = [[2, 11, 5], [6, 5, 9], [5, 5, 1]]  # Моя игра
X = [[0.72, 0.27, 0.3], [0.14, 0.53, 0.09], [0.14, 0.2, 0.61]]
q = [0.3, 0.4, 0.3]


game = Game(A, X)
# проверка существования решения в чистых стратегиях
print(game.check_saddle_point())
Game.print_matrix(game.risk_matrix, 'Матрица риска')
game.print_criteria_values(0.7)
Game.print_matrix(game.loss_function, 'Функция потерь L')
print("Цена эксперимента", game.price_with_experience(q))
d = game.get_decision_function()
Game.print_matrix(d, 'Функции решений d(x)')
risk_func = game.get_risk_function()
Game.print_matrix(risk_func, 'Функция риска R')
min_val = game.get_min_value_from_baiesian_function(q)
print('Минимальное значение функции Байеса', min_val)
print("минимальная функция", min_val[1], game.get_decision_function()[min_val[1]])
risk_func = numpy.transpose(array(risk_func)).tolist()
significant_probabilities = game.get_game_price(0.02, risk_func)
print('Значимые вероятности:')
for i in range(len(significant_probabilities[2])):
    print(i, significant_probabilities[2][i])
mixed_strategy_solution = game.get_decision_in_mixed_strategy(significant_probabilities[2])
print(mixed_strategy_solution)
print('Решение в смешанных стратегиях:')
for i in mixed_strategy_solution:
    print(f'X{list(mixed_strategy_solution.keys()).index(i)} =', end=' ')
    val = mixed_strategy_solution[i]
    for j in range(len(val)):
        print(f'a{j}*{round(val[j], 3)}', end='+')
    print()
