x=input("Enter the first string : ")
y=input("Enter the second string : ")
matrix=[[ [0] for _ in range(len(y)+1)] for _ in range(len(x)+1)]
for i in range(1,len(x)+1):
    for j in range(1,len(y)+1):
        if x[i-1]==y[j-1]:
            matrix[i][j]=[matrix[i-1][j-1][0]+1, "↖"]
        else:
            if matrix[i-1][j][0]>=matrix[i][j-1][0]:
                matrix[i][j]=[matrix[i-1][j][0],"↑"]
            else:
                matrix[i][j]=[matrix[i][j-1][0],"←"]
i=len(x)
j=len(y)
lcs=list()
while len(matrix[i][j])!=1:
    if matrix[i][j][1]=="↖":
        lcs.append(x[i-1])
        i-=1
        j-=1
    elif matrix[i][j][1]=="←":
        j-=1
    else:
        i-=1
print("\nThe matrix is : ")
for row in matrix:
    for elem in row:
        if len(elem)==1:
            print(*elem, end=" ")
            print(" ",end=" |")
        else:
            print(*elem, end=" |")
    print()
print("\nThe longest common subsequence is ",end="")
print(*lcs[::-1])
