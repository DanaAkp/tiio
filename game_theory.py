from numpy import array
import numpy as np


class Game:
    def __init__(self, payoff_matrix, experience_matrix):
        self.payoff_matrix = payoff_matrix
        self.risk_matrix = self.get_matrix_risk()
        #  матрица экспериментов Х
        self.experience_matrix = experience_matrix
        self.loss_function = self.get_loss_function()

    def get_a_(self, q):
        a_i = list(map(lambda x:
                       sum(list(map(
                           lambda y: self.payoff_matrix[x][y] * q[y],
                           range(len(self.payoff_matrix[x]))))),
                       range(len(self.payoff_matrix))))
        #  а с домиком
        return max(a_i)

    #  цена игры без эксперимента
    def price_without_experience(self, q: list):
        a_ = self.get_a_(q)
        B_j = list(map(lambda x: max(self.get_column(self.payoff_matrix, x)), range(len(self.payoff_matrix[0]))))
        #  а с тильдой
        a__ = sum(list(map(lambda x: B_j[x]*q[x], range(len(B_j)))))
        return a__-a_

    def price_with_experience(self, q: list):
        a_ = self.get_a_(q)
        p_xl = list(map(lambda x: sum(list(map(lambda y: x[y]*q[y], range(len(x))))), self.experience_matrix))
        q_il = []
        for j in range(len(self.experience_matrix[0])):
            buf = []
            for l in range(len(self.experience_matrix)):
                buf.append((q[j] * self.experience_matrix[l][j]) / p_xl[l])
            q_il.append(buf)
        a_l = []
        for l in range(len(q_il[0])):
            buf = []
            for i in range(len(self.payoff_matrix)):
                buf_sum = []
                for j in range(len(self.payoff_matrix[i])):
                    buf_sum.append(self.payoff_matrix[i][j]*q_il[j][l])
                buf.append(sum(buf_sum))
            a_l.append(buf)
        a_l = list(map(lambda x: max(x), a_l))
        a__ = sum(list(map(lambda x: a_l[x]*p_xl[x], range(len(a_l)))))
        return a__-a_

    def get_min_value_from_baiesian_function(self, p):
        risk_function = self.get_risk_function()
        list_max = list(map(lambda x: max(list(map(lambda y: x[y]*p[y], range(len(x))))), risk_function))
        return self.get_min_index_from_list(list_max)

    # функция решений d(x)
    def get_decision_function(self):
        base = len(self.payoff_matrix)
        decision_function = []
        dimension = pow(len(self.payoff_matrix), len(self.payoff_matrix[0]))
        for i in range(dimension):
                buf = []
                while i > 0:
                    buf.append(i % base)
                    i //= base
                while len(buf) != 3:
                    buf.append(0)
                buf.reverse()
                decision_function.append(buf)
        return decision_function

    #  функция риска R(d(x), Tetta)
    def get_risk_function(self):
        d = self.get_decision_function()
        risk_function = []
        for i in range(len(d)):
            buf = []
            for j in range(len(d[i])):
                buf.append(sum(list(map(lambda k: self.loss_function[int(d[i][k])][j] * self.experience_matrix[k][j],
                                        range(len(d[i]))))))
            risk_function.append(buf)
        return risk_function

    #  критерий крайнего пессимизма для матрицы выигрышей
    def extreme_pessimism_criterion_payoff(self):
        max_ind = 0
        max_ = self.payoff_matrix[0][0]
        for i in range(len(self.payoff_matrix)):
            for j in range(len(self.payoff_matrix[i])):
                if max_ < self.payoff_matrix[i][j]:
                    max_ind = i
                    max_ = self.payoff_matrix[i][j]
        return max_, max_ind + 1

    #  получение фукнции потерь L
    def get_loss_function(self):
        return list(map(lambda x:list(map(lambda y: (-1)*y, x)), self.payoff_matrix))

    #  критерий крайнего пессимизма для матрицы риска
    def extreme_pessimism_criterion_risk(self):
        min_ind = 0
        min_ = self.risk_matrix[0][0]
        for i in range(len(self.risk_matrix)):
            for j in range(len(self.risk_matrix[i])):
                if min_ > self.risk_matrix[i][j]:
                    min_ind = i
                    min_ = self.risk_matrix[i][j]
        return min_, min_ind + 1

    #  критерий Вальда
    def test_wald(self):
        # min_i = self.payoff_matrix[:, 0]
        min_i = self.get_column(self.payoff_matrix, 0)
        for i in range(len(self.payoff_matrix)):
            for j in range(len(self.payoff_matrix[i])):
                if min_i[i] > self.payoff_matrix[i][j]:
                    min_i[i] = self.payoff_matrix[i][j]
        return self.get_max_index_from_list(min_i)

    @staticmethod
    def get_column(matrix, index):
        return [row[index] for row in matrix]

    #  критерий Сэвиджа
    def test_savage(self):
        max_i = self.get_column(self.risk_matrix, 0)
        for i in range(len(self.risk_matrix)):
            for j in range(len(self.risk_matrix[i])):
                if max_i[i] < self.risk_matrix[i][j]:
                    max_i[i] = self.risk_matrix[i][j]
        return self.get_min_index_from_list(max_i)

    #  критерий Байеса для матрицы выигрышей
    def test_bayes_payoff_matrix(self, p: list):
        list_sum = list(map(lambda x: sum(list(map(lambda y: x[y] * p[y], range(len(x))))), self.payoff_matrix))
        return self.get_max_index_from_list(list_sum)

    #  критерий Байеса для матрицы риска
    def test_bayes_risk_matrix(self, p: list):
        list_sum = list(map(lambda x: sum(list(map(lambda y: x[y] * p[y], range(len(x))))), self.risk_matrix))
        return self.get_min_index_from_list(list_sum)

    @staticmethod
    def get_max_index_from_list(from_list: list):
        max_ind = 0
        max_ = from_list[0]
        for i in range(len(from_list)):
            if max_ < from_list[i]:
                max_ind = i
                max_ = from_list[i]
        return max_, max_ind+1

    @staticmethod
    def get_min_index_from_list(from_list: list):
        min_ind = 0
        min_ = from_list[0]
        for i in range(len(from_list)):
            if min_ > from_list[i]:
                min_ind = i
                min_ = from_list[i]
        return min_, min_ind+1

    #  критерий Гурвица для матрицы выигрышей
    def test_hurwitz_payoff_matrix(self, lambda_: float):
        list_max = list(map(lambda x: (lambda_ * min(x) + (1 - lambda_) * max(x)), self.payoff_matrix))
        return self.get_max_index_from_list(list_max)

    #  критерий Гурвица для матрицы риска
    def test_hurwitz_risk_matrix(self, lambda_: float):
        list_min = list(map(lambda x:(lambda_ * max(x) + (1 - lambda_) * min(x)), self.risk_matrix))
        return self.get_min_index_from_list(list_min)

    #  получение матрицы риска из матрицы выигрышей
    def get_matrix_risk(self):
        # list_ = list(
        #     map(lambda x: array(list(
        #         map(lambda y: max(x)-y, x))),
        #         np.transpose(self.payoff_matrix)))
        # return np.transpose(list_)
        # # max_j = self.payoff_matrix.max(axis=0)
        return [[max(self.get_column(self.payoff_matrix, j)) - self.payoff_matrix[i][j]
        for j in range(len(self.payoff_matrix[i]))]
                      for i in range(len(self.payoff_matrix))]

    #  критерий Байеса для матрицы выигрышей с одинаковыми вероятностями
    def test_bayes_payoff_matrix_with_equal_probabilities(self):
        n = len(self.payoff_matrix[0])
        return self.test_bayes_payoff_matrix([1/n]*n)

    #  критерий Байеса для матрицы риска с одинаковыми вероятностями
    def test_bayes_risk_matrix_with_equal_probabilities(self):
        n = len(self.risk_matrix[0])
        return self.test_bayes_risk_matrix([1/n]*n)

    # цена игры в смешанных стратегиях
    def get_game_price(self, epsilon, arr):
        # region INIT
        k = 1
        NA = [0] * len(arr)
        NB = [0] * len(arr[0])
        i = 0
        m = arr[0][0]
        for ind in range(len(arr)):
            if m < max(arr[ind]):
                i = ind
                m = max(arr[ind])

        NA[i] += 1
        list_b = arr[i]
        j = self.min_second(list_b)
        NB[j] += 1
        list_a = self.get_column(arr, j)
        v_min = min(list_b) / k
        v_max = max(list_a) / k
        v_aver = (v_max + v_min) / 2
        sub = 10
        # endregion

        while sub > epsilon:
            k += 1
            i = self.max_first(list_a)
            NA[i] += 1
            list_b = list(map(lambda x: list_b[x] + arr[i][x], range(len(arr[i]))))
            j = self.min_second(list_b)
            NB[j] += 1
            list_a = list(map(lambda x: list_a[x] + self.get_column(arr, j)[x], range(len(self.get_column(arr, j)))))
            v_min = min(list_b) / k
            v_max = max(list_a) / k
            sub = v_max - v_min
            v_aver = (v_max + v_min) / 2
        p = list(map(lambda x: x / k, NA))
        q = list(map(lambda x: x / k, NB))
        return v_aver, p, q

    def check_saddle_point(self):
        max_ = list(map(lambda x: max(self.get_column(self.payoff_matrix, x)), range(len(self.payoff_matrix[0]))))
        min_ = list(map(lambda x: min(x), self.payoff_matrix))
        return max(min_) if max(min_) == min(max_) else False

    # функция, которая выбирает для первого игрока его максимальный выигрыш
    @staticmethod
    def max_first(arr):
        ind_max = list(arr).index(max(arr))
        return ind_max

    # функция, которая выбирает для 2 игрока минимальный выигрыш первого игрока
    @staticmethod
    def min_second(arr):
        ind_min = list(arr).index(min(arr))
        return ind_min

    @staticmethod
    def print_matrix(matrix, description: str):
        print(description)
        for i in matrix:
            for j in i:
                print(j, end='\t')
            print()

    def print_criteria_values(self, lambda_):
        print('Критерий крайнего пессимизма для А', self.extreme_pessimism_criterion_payoff())
        print('Критерий крайнего пессимизма для R', self.extreme_pessimism_criterion_risk())
        print('Критерий Вальда', self.test_wald())
        print('Критерий Сэвиджа', self.test_savage())
        print('Критерий Байеса для А', self.test_bayes_payoff_matrix_with_equal_probabilities())
        print('Критерий Байеса для R', self.test_bayes_risk_matrix_with_equal_probabilities())
        print('Критерий Гурвица для А', self.test_hurwitz_payoff_matrix(lambda_))
        print('Критерий Гурвица для R', self.test_hurwitz_risk_matrix(lambda_))



