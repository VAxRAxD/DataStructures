def ComputePrefix(pattern):
    pi=[0 for _ in range(len(pattern))]
    k=0
    for i in range(1,len(pattern)):
        while k>0 and pattern[k]!=pattern[i]:
            k=pi[k]
        if pattern[k]==pattern[i]:
            k+=1
        pi[i]=k
    return pi

text=input("Enter the text : ")
pattern=input("Enter the pattern : ")

pi=ComputePrefix(pattern)
i=0
for j in range(len(text)):
    while i>0 and pattern[i]!=text[j]:
        i=pi[i-1]
    if pattern[i]==text[j]:
        i+=1
    if i == len(pattern):
        print("Pattern found at shift ", j-len(pattern)+1)
        i=pi[i-1]