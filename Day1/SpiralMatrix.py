row = int(input())
column = int(input())
matrix = []
for i in range(row):
    a = list(map(int, input().split()))
    matrix.append(a)
    
if not matrix or not matrix[0]:  
    print("[]")    

top = 0
right = column - 1
bottom = row - 1
left = 0
count = 0
newMatrix = []

while count < row * column:
    for i in range(left, right + 1):
        if count < row * column:
            newMatrix.append(matrix[top][i])
            count += 1
    top += 1

    for i in range(top, bottom + 1):
        if count < row * column:
            newMatrix.append(matrix[i][right])
            count += 1
    right -= 1

    for i in range(right, left - 1, -1):
        if count < row * column:
            newMatrix.append(matrix[bottom][i])
            count += 1
    bottom -= 1

    for i in range(bottom, top - 1, -1):
        if count < row * column:
            newMatrix.append(matrix[i][left])
            count += 1
    left += 1

print(newMatrix)