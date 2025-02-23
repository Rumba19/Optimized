# **HPC Optimization Project**

## **Project Overview**
This project demonstrates **cache optimization techniques** used in **High-Performance Computing (HPC)**, specifically **loop tiling** and **data alignment** to improve matrix multiplication performance. The project includes:
- A **naive matrix multiplication implementation**.
- An **optimized version using loop tiling and data alignment**.
- **Execution time comparison** to evaluate performance improvements.


## **Implementation Details**

### **Naive Implementation**

- Uses triple nested loops to multiply matrices.

- Causes frequent cache misses leading to high execution time.

### **Optimized Implementation (Loop Tiling + Data Alignment)**

- Loop Tiling: Processes smaller sub-blocks to improve cache locality.

- Expected Outcome: Significant reduction in execution time compared to the naive approach.

## **Prerequisites**
Ensure you have the following installed:
- **Python 3.x** (Recommended: Python 3.8 or later)
- **NumPy**

  ### **Expected OutPut:**
 Execution Time (Naive): 129.01953387260437 seconds
Execution Time (Optimized): 117.46461534500122 seconds
## **How to Run**
### **Clone the repository and Run the python script**
    ```sh 
    git clone https://github.com/Rumba19/Optimized
    cd Optimized
    python3 matrix_optimization.py


