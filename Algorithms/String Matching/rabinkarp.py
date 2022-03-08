string=input("Enter the text : ")
pattern=input("Enter the pattern : ")
n=len(string)
m=len(pattern)
d=26
q=7
p=0
txt=0
h=1
for i in range(m-1):
    h = (h*d)%q
for i in range(m):
    p = (d*p + ord(pattern[i]))%q
    txt = (d*txt + ord(string[i]))%q
for i in range(n-m+1):
    if p==txt:
        match=True
        for j in range(m):
            if pattern[j]!=string[i+j]:
                match=False
                break
        if match:
            print(f"Pattern found at shift {i}")
    if i<n-m:
        txt = (d*(txt-ord(string[i])*h) + ord(string[i+m]))%q