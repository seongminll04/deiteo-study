n=int(input())

lst=[list(map(int, input().split())) for i in range(n)]

l=[]

for i in range(n):
    test=lst[i]
    cnt=1
    for j in lst[:i]+lst[i+1:]:
        if j[0] > test[0] and j[1]>test[1]:
            cnt+=1
    l.append(cnt)
print(' '.join(map(str,l)))

