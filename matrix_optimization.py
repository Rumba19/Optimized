import numpy as np
import time

N = 512  # Matrix size
A = np.random.rand(N, N)
B = np.random.rand(N, N)

# Naive Implementation
C = np.zeros((N, N))
start_time = time.time()
for i in range(N):
    for j in range(N):
        for k in range(N):
            C[i][j] += A[i][k] * B[k][j]
end_time = time.time()
print("Execution Time (Naive):", end_time - start_time, "seconds")

# Optimized Implementation Using Loop Tiling
BLOCK_SIZE = 32  # Tile size
C = np.zeros((N, N))
start_time = time.time()
for i in range(0, N, BLOCK_SIZE):
    for j in range(0, N, BLOCK_SIZE):
        for k in range(0, N, BLOCK_SIZE):
            for ii in range(i, min(i + BLOCK_SIZE, N)):
                for jj in range(j, min(j + BLOCK_SIZE, N)):
                    for kk in range(k, min(k + BLOCK_SIZE, N)):
                        C[ii][jj] += A[ii][kk] * B[kk][jj]
end_time = time.time()
print("Execution Time (Optimized):", end_time - start_time, "seconds")