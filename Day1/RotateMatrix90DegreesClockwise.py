row = int(input())
column = int(input())
matrix = []
newMatrix = []
for i in range(row):
    a = list(map(int, input().split()))
    matrix.append(a)
for i in range(row):
    for j in range(row-1, -1, -1):
        newMatrix.append(matrix[j][i])

print(newMatrix)