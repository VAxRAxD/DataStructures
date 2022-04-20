"""
ALGORITHM_JOB_SEQUENCING
#n is total number of jobs
#p[1:n] and d[1:n] contains profit and deadline of jobs from 1 to n respectively
#a[1:n] contains the indexes of jobs ordered such that p[a[i]]>=p[a[i+1]]
#dmax=MAX(d) is longest deadline
#x is solution vector

#Initializing timeslot vector where if t[i]=0 then iᵗʰ timeslot is empty else it is full
for i=1 to dmax do
    t[i]=0
j=0 #Count number of jobs done
for i=1 to n do
    if j==dmax then break
    k=d[a[i]] #deadline for particular job
    while k>=1 do
        if t[k]==0 then
            x[k]=a[i]
            t[k]=1
            j=j+1
            break
        k=k-1
return x

"""

n=int(input("Enter number of jobs : "))
profit=list(map(int,input("Enter profits of the jobs : ").split()))
deadline=list(map(int,input("Enter deadline of the jobs : ").split()))
timeslot=[0 for _ in range(max(deadline))]
jobs=list()
for i in range(n):
    dict={}
    dict['Number']=i+1
    dict['Profit']=profit[i]
    dict['Deadline']=deadline[i]
    jobs.append(dict)
jobs=sorted(jobs, key=lambda x:x['Profit'], reverse=True)
gain=0
for i in range(n):
    if 0 not in timeslot:
        break
    index,value,time=jobs[i].values()
    while time>=1:
        if timeslot[time-1]==0:
            timeslot[time-1]=index
            gain+=value
            break
        time-=1

print(timeslot)
print(gain)