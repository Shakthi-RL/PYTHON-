def flippingMatrix(matrix):
    n = len(matrix) // 2
    total = 0
    for i in range(n):
        for j in range(n):
            total += max(
                matrix[i][j],
                matrix[i][2*n - 1 - j],
                matrix[2*n - 1 - i][j],
                matrix[2*n - 1 - i][2*n - 1 - j]
            )
    return total

# Example input
rows = int(input("Rows (must be even): "))
matrix = []
print("Enter matrix row by row:")
for _ in range(rows):
    matrix.append(list(map(int, input().split())))

print("Max sum in upper-left quadrant:", flippingMatrix(matrix))

