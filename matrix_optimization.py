import numpy as np
import time

# Define matrix size
N = 512  # Increase to 1024 or 2048 for better performance
A = np.random.rand(N, N)
B = np.random.rand(N, N)

# Naive Implementation (Pure Python)
def naive_multiplication(A, B, N):
    C = np.zeros((N, N))
    start_time = time.time()
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i][j] += A[i][k] * B[k][j]
    end_time = time.time()
    print("Execution Time (Naive):", end_time - start_time, "seconds")
    return C

# **Optimized Implementation using NumPy's matmultiplication**
def numpy_optimized_multiplication(A, B):
    start_time = time.time()
    C = np.dot(A, B)  # Using NumPy's optimized matrix multiplication
    end_time = time.time()
    print("Execution Time (Optimized with NumPy):", end_time - start_time, "seconds")
    return C

# Run Naive Implementation
naive_multiplication(A, B, N)

# Run Optimized Implementation
numpy_optimized_multiplication(A, B)
