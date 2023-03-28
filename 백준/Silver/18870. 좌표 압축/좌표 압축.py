import sys
input=sys.stdin.readline

n=int(input())

lst=list(map(int,input().split()))

cnt=0
tmp='start'

dic={}
for i in sorted(lst):
    if tmp=='start':
        tmp=i
    else:
        if tmp!=i:
            tmp=i
            cnt+=1
    dic[i]=cnt

for i in lst:
    print(dic[i], end=' ')
