"""
ALGORITHM_RABINKARP
#text[1:n] is the input text of size n
#pattern[1:m] is the pattern of size m
#d is number of character in input set, we can assume any value
#q is a prime number used for modulus operation

d=10
q=13
p=0
t=0
for i=0 to m-1 do
    p=(d*p + ord(pattern[i])) mod q
    t=(d*t + ord(text[i])) mod q

for i=1 to n-m+1 do
    if p==t then
        if p[1:m]==text[i:i+m] then
            PRINT "Pattern found at shift " i
    if i<n-m
        t=((t- v[character to be removed])*d + v[character to be added]) mod q

"""

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