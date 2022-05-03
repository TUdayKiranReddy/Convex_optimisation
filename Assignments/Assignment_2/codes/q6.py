import numpy as np
import cvxpy as cp
import matplotlib.pyplot as plt



A = np.array([[1, -0.5], [-0.5, 2]])
print(np.linalg.eig(A))
c = np.array([[-1, 0]])

def get_b(u1, u2):
	return np.array([[u1, u2, 1]])


