"""
ALGORITHM_KMP
#text[1:n] is the input text of size n
#pattern[1:m] is the pattern of size m

pi=COMPUTE_PREFIX(pattern[1:m])
j=-1
for i=0 to n do
    while j>=0 and text[i]!=text[j+1] do
        j=pi[j]-1
    if pattern[i]==pattern[j+1] then
        j+=1
    if j==n-1 then
        PRINT "Pattern found at shift " (i-m)+1
        j=pi[j]-1

COMPUTE_PREFIX(pattern[1:m])
#pi[1:m] is the lcs/prefix array

pi[1]=0
k=0
for i=1 to m do
    if pattern[i]==pattern[k] then
        k+=1
    else
        k=0
    pi[i]=k
return pi

"""

def ComputePrefix(pattern):
    pi=[0 for _ in range(len(pattern))]
    k=0
    for i in range(1,len(pattern)):
        if pattern[i]==pattern[k]:
            k+=1
        else:
            k=0
        pi[i]=k
    return pi

text=input("Enter the text : ")
pattern=input("Enter the pattern : ")

pi=ComputePrefix(pattern)
i=-1
for j in range(len(text)):
    while i>=0 and pattern[i+1]!=text[j]:
        i=pi[i]-1
    if pattern[i+1]==text[j]:
        i+=1
    if i == len(pattern)-1:
        print("Pattern found at shift ", j-len(pattern)+1)
        i=pi[i]-1