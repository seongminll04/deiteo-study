n=int(input())
lst=list(map(int,input().split()))
lst.sort()

s=0
for i in range(1,n+1):
    s+=sum(lst[:i])
print(s)