from numpy import array, min, max, transpose


def check_saddle_point(arr: array):
    min_ = arr.min(axis=1)
    max_ = arr.max(axis=0)
    return max if max(min_) == min(max_) else False


def row(arr: array, mass):
    # print(arr)# проверять каждый этот массив со всеми строками матрицы
    # print(f'mas = {mass}')
    for i in range(len(arr)):
        # print(f'arr[{i}] = {arr[i]}')
        for j in range(len(arr[i])):
            print(f"{arr[i][j]} - {mass[i]}")
            if arr[i][j] > mass[j]:
                print('stop----------')
                return False
    return True


def col(arr: array, mass):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[j][i] > mass[j]:
                return False
    return True


def remove_dominated_strategies(arr: array):
    # while True:
    domin = list(map(lambda x: row(arr, x), arr))
    print('row', domin)
    # domin = list(map(lambda x: col(arr, arr[:, x]), range(len(arr))))
    # print('col', domin)


# функция, которая выбирает для первого игрока его максимальный выигрыш
def max_first(arr):
    ind_max = list(arr).index(max(arr))
    return ind_max


def min_second(arr):
    ind_min = list(arr).index(min(arr))
    return ind_min


def iter_method(arr: array, epsilon):
    # region INIT
    k = 1
    i = 0
    m = arr[0][0]
    for ind in range(len(arr)):
        if m < max(arr[ind]):
            i = ind
            m = max(arr[ind])

    list_b = arr[i]
    j = min_second(list_b)
    list_a = arr[:, j]
    v_min = min(list_b) / k
    v_max = max(list_a) / k
    v_aver = (v_max + v_min) / 2
    sub = 10
    # endregion
    print(f'\n{k} -----------------------------------------')
    print(f'{i}-{list_b}\n{j}-{list_a}\n{v_min:.2f} - {v_max:.2f} - {v_aver:.2f}')

    while sub > epsilon:
        k += 1
        i = max_first(list_a)
        list_b = list(map(lambda x: list_b[x] + arr[i][x], range(len(arr[i]))))
        j = min_second(list_b)
        list_a = list(map(lambda x: list_a[x] + arr[:, j][x], range(len(arr[:, j]))))
        v_min = min(list_b) / k
        v_max = max(list_a) / k
        sub = abs(((v_max + v_min) / 2) - v_aver)
        v_aver = (v_max + v_min) / 2
        print(f'\n{k} -----------------------------------------')
        print(f'{i}-{list_b}\n{j}-{list_a}\n{v_min:.2f} - {v_max:.2f} - {v_aver}\nsub={sub}')


# A = array([[3, 2, 0, 7], [-2, 5, 7, 3], [6, 4, 0, 6], [1, 8, -3, 2]])
A = array([[6, 1, 4], [2, 4, 2], [4, 3, 5]])
iter_method(A, 0.01)
