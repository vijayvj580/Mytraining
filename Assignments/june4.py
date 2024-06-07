#june4

#1
import numpy as np

# Create two 3x3 matrices A and B with random integer values between 1 and 10
A = np.random.randint(1, 11, size=(3, 3))
B = np.random.randint(1, 11, size=(3, 3))

print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)

# Compute the sum of A and B
sum_matrix = np.add(A, B)
print("\nSum of A and B:")
print(sum_matrix)

# Compute the difference between A and B
diff_matrix = np.subtract(A, B)
print("\nDifference between A and B:")
print(diff_matrix)

# Compute the element-wise product of A and B
elementwise_product = np.multiply(A, B)
print("\nElement-wise product of A and B:")
print(elementwise_product)

# Compute the matrix product of A and B
matrix_product = np.dot(A, B)
print("\nMatrix product of A and B:")
print(matrix_product)

# Compute the transpose of matrix A
transpose_A = np.transpose(A)
print("\nTranspose of matrix A:")
print(transpose_A)

# Compute the determinant of matrix A
determinant_A = np.linalg.det(A)
print("\nDeterminant of matrix A:", determinant_A)



#2

import numpy as np
from scipy.linalg import solve

# Coefficients of the linear equations
A = np.array([[2, 3], [3, 4]])
B = np.array([8, 11])

# Solve the system of equations
solution = solve(A, B)

# Extract the solution
x, y = solution

print("Solution:")
print("x =", x)
print("y =", y)


#3

from scipy import integrate
import sympy as sp

# Define the function f(x) = x^3 + 2x^2 + x + 1
def f(x):
    return x**3 + 2*x**2 + x + 1

# Define the symbolic variable
x_sym = sp.Symbol('x')

# Compute the first derivative of f(x) at x = 1
f_prime = sp.diff(f(x_sym), x_sym)
f_prime_at_1 = f_prime.subs(x_sym, 1)

# Compute the second derivative of f(x) at x = 1
f_double_prime = sp.diff(f_prime, x_sym)
f_double_prime_at_1 = f_double_prime.subs(x_sym, 1)

# Compute the definite integral of f(x) from x = 0 to x = 2
definite_integral, _ = integrate.quad(f, 0, 2)

print("First derivative of f(x) at x = 1:", f_prime_at_1)
print("Second derivative of f(x) at x = 1:", f_double_prime_at_1)
print("Definite integral of f(x) from x = 0 to x = 2:", definite_integral)



#4

import numpy as np
from scipy import stats

# Create a dataset with 20 random values between 1 and 100
dataset = np.random.randint(1, 101, size=20)

mean = np.mean(dataset)

median = np.median(dataset)

std_dev = np.std(dataset)

variance = np.var(dataset)

skewness = stats.skew(dataset)

kurtosis = stats.kurtosis(dataset)

print("Dataset:", dataset)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)
print("Variance:", variance)
print("Skewness:", skewness)
print("Kurtosis:", kurtosis)