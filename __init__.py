# import numpy as np
# from scipy.optimize import linprog
#
# b_ub = [74,40,36]
# b_eq = [20,45,30]
# A=np.array([[2, 9, 11],[10, 8, 4],[5, 12, 1]])
# m, n = A.shape
# c=list(np.reshape(A,n*m))# Преобразование матрицы A в список c.
# A_ub= np.zeros([m,m*n])
# for i in np.arange(0,m,1):# Заполнение матрицы условий –неравенств.
#          for j in np.arange(0,n*m,1):
#                   if i*n<=j<=n+i*n-1:
#                         A_ub  [i,j]=1
# A_eq= np.zeros([m,m*n])
# for i in np.arange(0,m,1):# Заполнение матрицы условий –равенств.
#          k=0
#          for j in np.arange(0,n*m,1):
#                   if j==k*n+i:
#                            A_eq [i,j]=1
#                            k=k+1
# print(linprog(c, A_ub, b_ub, A_eq, b_eq))
# # print(linprog(c=c, A_ub=A_ub, A_eq=A_eq))
# from scipy.optimize import minimize
# import numpy as np
#
# def rosen(x):
#     """The Rosenbrock function"""
#     return np.sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0, axis=0)
#
#
# x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])
# res = minimize(rosen, x0, method='nelder-mead',
#     options={'xtol': 1e-8, 'disp': True})
# print(res.x)

# from scipy import optimize
# from scipy.optimize import Bounds
# import numpy as np
# from scipy.optimize import LinearConstraint
#
# # уравнения
# linear_constraint = LinearConstraint(A=[[2, 10, 5], [9, 8, 12], [11, 4, 1]], ub=[np.inf, np.inf, np.inf], lb=[1, 1, 1])
# # Xi - ограничения
# bounds = Bounds(lb=[0, 0, 0], ub=[np.inf, np.inf, np.inf])
#
#
# def func(x):
#     return x[0] + x[1] + x[2]
#
#
# x0 = [23, 31, 14]
# res = optimize.minimize(func, x0, method='trust-constr', bounds=bounds, constraints=[linear_constraint])

# import scipy
# from scipy.optimize import linprog # загрузка библиотеки ЛП
# c = [-25, -35,-25,-40,-30] # список коэффициентов функции цели
# b_ub = [700,250,600,400] # список объёмов ресурсов
# A_ub = [[1,2,3,2,4], # матрица удельных значений ресурсов
#                [5,4,3,2,1],
#               [3,4,2,5,3],
#               [4,2,5,3,1]]
# d=linprog(c, A_ub, b_ub) # поиск решения
# for key,val in d.items():
#          print(key,val) # вывод решения
#          if key=='x':
#                   q=[sum(i) for i in A_ub*val]#использованные ресурсы
#                   print('A_ub*x',q)
#                   q1= scipy.array(b_ub)-scipy.array(q) #остатки ресурсов
#                   print('b_ub-A_ub*x', q1)


from scipy.optimize import linprog

# region прямая задача
obj = [1, 1, 1]

lhs_ineq = [[-2, -10, -5], [-9, -8, -12], [-11, -4, -1]]  # левая сторона желтого неравенства
rhs_ineq = [-1, -1, -1]  # правая сторона желтого неравенства
bnd = [(0, float("inf")),  # Границы x
       (0, float("inf")),
       (0, float("inf"))]  # Границы y

opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
              bounds=bnd, method="simplex")
print(opt, end='\n\n\n')
# endregion

# region
obj = [-1, -1, -1]

lhs_ineq = [[2, 9, 11], [10, 8, 4], [5, 12, 1]]
rhs_ineq = [1, 1, 1]


bnd = [(0, float("inf")),
       (0, float("inf")),
       (0, float("inf"))]

opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
              bounds=bnd, method="revised simplex")
print(opt)
# endregion