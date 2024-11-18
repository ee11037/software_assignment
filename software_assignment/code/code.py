import math
def qr_decomposition(matrix):
    n = len(matrix)
    Q = [[0] * n for _ in range(n)]
    R = [[0] * n for _ in range(n)]

    for j in range(n):
        v = [matrix[i][j] for i in range(n)]
        
        for i in range(j):
            R[i][j] = sum(Q[k][i] * matrix[k][j] for k in range(n))
            v = [v[k] - R[i][j] * Q[k][i] for k in range(n)]
        
        R[j][j] = math.sqrt(sum(v[k] ** 2 for k in range(n)))
        if R[j][j] > 0:
            for i in range(n):
                Q[i][j] = v[i] / R[j][j]
    
    return Q, R

def qr_algorithm(matrix, max_iterations=100, tol=1e-10):
    n = len(matrix)
    A = [row[:] for row in matrix]  
    
    for _ in range(max_iterations):
        
        Q, R = qr_decomposition(A)
        
        A = [[sum(R[i][k] * Q[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
        
        
        off_diagonal_norm = math.sqrt(sum(A[i][j] ** 2 for i in range(n) for j in range(i)))
        if off_diagonal_norm < tol:
            break
    
    
    eigenvalues = [A[i][i] for i in range(n)]
    return eigenvalues


m = int(input("Enter the order of matrix(m): "))



print(f"Enter the matrix (each row should have {m} space-separated values):")
matrix = [list(map(int, input().split())) for _ in range(m)]

eigenvalues = qr_algorithm(matrix)
print("Eigenvalues:", eigenvalues)
