from scipy.optimize import linprog

# region прямая задача
obj = [1, 1, 1]

lhs_ineq = [[-2, -10, -5], [-9, -8, -12], [-11, -4, -1]]
rhs_ineq = [-1, -1, -1]
bnd = [(0, float("inf")),
       (0, float("inf")),
       (0, float("inf"))]

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