n=int(input())
lst=[[0]*1001 for _ in range(1001)]
for _ in range(n):
    a,b,c,d = map(int,input().split())

    for i in range(a,a+c):
        for j in range(b,b+d):
            lst[i][j]= _+1

l=[0]*n
for i in lst:
    for j in i:
        if j!=0:
            l[j-1] += 1

for i in l:
    print(i)
