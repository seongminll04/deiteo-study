lst=[1,2,4]
l=[int(input()) for _ in range(int(input()))]

for i in range(max(l)-2):
    lst.append(lst[i]+lst[i+1]+lst[i+2])

for i in l:
    print(lst[i-1])
