n = int (input())
a = list(map(int,input().split()))

mini = a.index(min(a))
maxi = a.index(max(a))

a[mini],a[maxi] = a[maxi],a[mini]

print(*a)