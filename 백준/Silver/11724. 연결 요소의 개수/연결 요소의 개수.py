import sys
input=sys.stdin.readline
def chk(q):
    global visited
    next_q=[]
    while q:
        x=q.pop()
        for i in lst[x]:
            if visited[i]==0:
                visited[i]=1
                next_q.append(i)

    if next_q:
        chk(next_q)


n,m=map(int,input().split())

lst=[[] for i in range(n+1)]

for i in range(m):
    u,v = map(int, input().split())
    lst[u].append(v)
    lst[v].append(u)

visited=[0]*(n+1)
cnt=0

for i in range(1,n+1):
    if visited[i]==0:
        visited[i]=1
        chk([i])
        cnt+=1

print(cnt)
