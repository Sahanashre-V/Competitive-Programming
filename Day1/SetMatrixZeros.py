row = int(input())
column = int(input())
matrix = []
for i in range(row):
    a = list(map(int, input().split()))
    matrix.append(a)

row=[]
column=[]
for i in range(0,len(matrix)):
    for j in range(0,len(matrix[i])):
        if matrix[i][j]==0:
            row.append(i)
            column.append(j)
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i in row:
            matrix[i][j]=0
        if j in column:
            matrix[i][j]=0
print(matrix)