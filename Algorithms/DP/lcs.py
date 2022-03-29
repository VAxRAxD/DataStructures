x="QSRPQ"
y="PQRQSPQ"
matrix=[[ [0] for _ in range(len(y)+1)] for _ in range(len(x)+1)]
arrows=["left","top","slant"]
for i in range(1,len(x)+1):
    for j in range(1,len(y)+1):
        if x[i-1]==y[j-1]:
            matrix[i][j]=[matrix[i-1][j-1][0]+1, "slant"]
        else:
            if matrix[i-1][j][0]>=matrix[i][j-1][0]:
                matrix[i][j]=[matrix[i-1][j][0],"top"]
            else:
                matrix[i][j]=[matrix[i][j-1][0],"right"]
i=len(x)
j=len(y)
lcs=list()
while len(matrix[i][j])!=1:
    if matrix[i][j][1]=="slant":
        lcs.append(x[i-1])
        i-=1
        j-=1
    elif matrix[i][j][1]=="right":
        j-=1
    else:
        i-=1
print(*lcs[::-1])
for row in matrix:
    print(*row)

