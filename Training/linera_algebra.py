import numpy as np


vector_2d = np.array([1, 2])
vector_3d = np.array([1, 2, 3])

print("Definition and notation of vectors using Python")
print("2D Vector:", vector_2d)
print("3D Vector:", vector_3d)


vector_a = np.array([1, 2])
vector_b = np.array([3, 4])
print(type(vector_a))
vector_add = vector_a + vector_b
vector_sub = vector_a + vector_b

print("Vector Addition (A + B):", vector_add)
print("Vector Subtraction (A - B):", vector_sub)


vector_c= np.array([1, 2, 3])
vector_d = np.array([3,
                     4,
                     6])
print(type(vector_c))
vector_add = vector_c + vector_d
vector_sub = vector_c - vector_d
print("Vector Addition (C + D):", vector_add)
print("Vector Subtraction (C - D):", vector_sub)

