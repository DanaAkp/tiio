from scipy.optimize import linprog
from numpy import array

A = array([[8, 2, 4], [4, 5, 6], [1, 7, 3]])
# region
obj = [1, 1, 1]

lhs_ineq = [[-8, -4, -1], [-2, -5, -7], [-4, -6, -3]]
rhs_ineq = [-1, -1, -1]
bnd = [(0, float("inf")),
       (0, float("inf")),
       (0, float("inf"))]

opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
              bounds=bnd, method="simplex")
print(opt)
print(f'\nW = {1/opt.fun}\nx = {list(map(lambda x: x*(1/opt.fun), opt.x))}', end='\n\n\n')

# endregion

# region
obj = [-1, -1, -1]

lhs_ineq = [[8, 2, 4], [4, 5, 6], [1, 7, 3]]
rhs_ineq = [1, 1, 1]


bnd = [(0, float("inf")),
       (0, float("inf")),
       (0, float("inf"))]

opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
              bounds=bnd, method="revised simplex")
print(opt)
print(f'\nW = {-1/opt.fun}\nx = {list(map(lambda x: x*(-1/opt.fun), opt.x))}')
# endregion