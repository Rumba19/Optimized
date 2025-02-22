import numpy as np
import time

N = 512  # Matrix size
A = np.random.rand(N, N)
B = np.random.rand(N, N)
C = np.zeros((N, N))

start_time = time.time()
for i in range(N):
    for j in range(N):
        for k in range(N):
            C[i][j] += A[i][k] * B[k][j]
end_time = time.time()

print("Execution Time (Naive):", end_time - start_time, "seconds")

