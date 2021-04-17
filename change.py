from numpy import array, min, max, transpose


def check_saddle_point(arr: array):
    min_ = arr.min(axis=1)
    max_ = arr.max(axis=0)
    print(f'min Ai = {min_}\nmax Bi = {max_}\nmaxmin Ai = {max(min_)}\nminmax Bi = {min(max_)}')
    return max(min_) if max(min_) == min(max_) else False


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


# функция, которая выбирает для 2 игрока минимальный выигрыш первого игрока
def min_second(arr):
    ind_min = list(arr).index(min(arr))
    return ind_min


def iter_method(arr: array, epsilon):
    # region INIT
    k = 1
    NA = [0]*len(arr)
    NB = [0]*len(arr[:, 0])
    i = 0
    m = arr[0][0]
    for ind in range(len(arr)):
        if m < max(arr[ind]):
            i = ind
            m = max(arr[ind])

    NA[i]+=1
    list_b = arr[i]
    j = min_second(list_b)
    NB[j]+=1
    list_a = arr[:, j]
    v_min = min(list_b) / k
    v_max = max(list_a) / k
    v_aver = (v_max + v_min) / 2
    sub = 10
    # endregion
    print(f'\nk = {k} ')
    print(f'i = {i}: {list_b}\nj = {j}: {list_a}\nV: {v_min:.2f} - {v_max:.2f} - {v_aver:.2f}')

    while sub > epsilon:
        k += 1
        i = max_first(list_a)
        NA[i]+=1
        list_b = list(map(lambda x: list_b[x] + arr[i][x], range(len(arr[i]))))
        j = min_second(list_b)
        NB[j]+=1
        list_a = list(map(lambda x: list_a[x] + arr[:, j][x], range(len(arr[:, j]))))
        v_min = min(list_b) / k
        v_max = max(list_a) / k
        sub = v_max - v_min
        v_aver = (v_max + v_min) / 2
        print(f'\nk = {k}')
        print(f'i = {i}: {list_b}\nj = {j}: {list_a}\nV: {v_min:.2f} - {v_max:.2f} - {v_aver:.2f}\n')
        print(v_min, v_max)
    p = list(map(lambda x: x/k, NA))
    q = list(map(lambda x: x/k, NB))

    print(f'\nP = {p}\nQ = {q}')
    print(f'W = {v_aver}\nk = {k}')


# A = array([[3, 2, 0, 7], [-2, 5, 7, 3], [6, 4, 0, 6], [1, 8, -3, 2]])
# A = array([[6, 1, 4], [2, 4, 2], [4, 3, 5]])
A = array([[8, 2, 4], [4, 5, 6], [1, 7, 3]])
# A = array([[0.6, 0.1, 0.9], [0.2, 0.7, 0.4], [0.5, 0.1, 0.5]])
# A = array([[10, 1], [2, 7]])
# # B = array([[6, 3], [-5, 11]])
# # AB = array([[16, -4], [8, 18]])
# # # print(f'saddle point = {check_saddle_point(A)}')
# # iter_method(A, 0.01)
# # iter_method(B, 0.01)
# # iter_method(AB, 0.01)

# A = array([[5, 4, 2, 1], [3, 9, 5,11]])
# print(check_saddle_point(A))
iter_method(A, 0.004)