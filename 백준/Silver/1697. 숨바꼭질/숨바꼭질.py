import sys
sys.setrecursionlimit(10**9)
n,k=map(int,input().split())

mm=0
ch=[0]*100001

def chk(q, cnt=0):
    global ch, mm
    next_q=[]
    while q:
        x=q.pop()
        if x == k:
            mm = cnt
            return
        else:
            for i in [x*2,x+1,x-1]:
                if 0 <= i <=100000 and ch[i]==0:

                    ch[i]=1
                    next_q.append(i)

    if next_q:
        chk(next_q, cnt+1)

chk([n])
print(mm)