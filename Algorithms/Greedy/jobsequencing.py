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